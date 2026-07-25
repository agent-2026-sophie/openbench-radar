# Cloudflare Worker：LLM CORS 代理部署指南

OpenBench Radar 的前端页面（`web/index.html`）跑在浏览器里。浏览器直连大模型 API 常常失败，原因有二：

1. **CORS**：多数 LLM 网关（含 ARK、部分自建网关）没有开放浏览器跨域访问。
2. **Mixed Content / 内网**：GitHub Pages 是 HTTPS 页面，无法直接请求 `http://` 或内网地址（如 `http://ark-cn-beijing.bytedance.net/api/v3`）。

解决办法：部署一个 **Cloudflare Worker** 作为转发代理。浏览器 → Worker（HTTPS，带 CORS）→ 上游 LLM。前端只需在「⚙️ 模型配置」里填入 Worker 地址即可实时调用模型。

```
浏览器  --HTTPS POST-->  Cloudflare Worker  --POST-->  上游 LLM（ARK / OpenAI 兼容）
         X-Target-Url: <真实上游地址>
         Authorization: Bearer <你的 Key>
```

---

## 一、部署 Worker（Dashboard 手动方式，最简单）

1. 打开 <https://dash.cloudflare.com/>，用你的账号登录（你已用 GitHub 账号关联注册）。
2. 左侧进入 **Workers & Pages** → **Create application** → **Create Worker**。
3. 给 Worker 取个名字（例如 `obr-llm-proxy`），点 **Deploy** 先创建一个默认 Worker。
4. 部署完成后点 **Edit code**（编辑代码）。
5. 删除编辑器里的默认内容，把本仓库 [`web/worker/llm-cors-proxy.js`](../web/worker/llm-cors-proxy.js) 的**全部内容**粘贴进去。
6. 点右上角 **Deploy**（部署）。
7. 复制你的 Worker 访问地址，形如：
   ```
   https://obr-llm-proxy.<你的子域>.workers.dev
   ```

> 进阶（可选）：想用 CLI 部署，可用 [wrangler](https://developers.cloudflare.com/workers/wrangler/)：
> `npm i -g wrangler && wrangler login && wrangler deploy web/worker/llm-cors-proxy.js`

---

## 二、在前端填写配置

打开你的站点 `https://agent-2026-sophie.github.io/openbench-radar/`，点右上角 **⚙️ 模型配置**：

| 字段 | 填写内容（以 ARK 为例） |
| --- | --- |
| API Key | 你的 ARK / OpenAI API Key（仅存本地浏览器，不上传仓库） |
| Base URL | `http://ark-cn-beijing.bytedance.net/api/v3` |
| 模型 | `ep-20260623142718-7q245`（选「自定义模型名」填入） |
| **LLM 代理地址（Cloudflare Worker URL）** | 第一步复制的 `https://obr-llm-proxy.xxx.workers.dev` |
| arXiv CORS 代理 | 保持默认即可 |

保存后点「测试连接」，出现 `✅ 连接成功（经 Worker 代理）` 即成功。之后勾选检索区的「浏览器内实时 LLM 摘要」，生成报告时就会调用模型产出 AI 执行摘要。

---

## 三、工作原理与安全说明

- 前端把**真实上游地址**放在 `X-Target-Url` 请求头，把 Key 放在标准 `Authorization: Bearer` 头，请求发给 Worker。
- Worker 校验 `X-Target-Url` 后原样转发请求体，并给响应补上 CORS 头返回浏览器。
- **API Key 只在浏览器 → Worker → 上游之间传递，不会写入仓库**；Worker 本身不存储 Key。
- 该 Worker 默认允许转发到任意上游。若担心被他人滥用，建议在 `llm-cors-proxy.js` 中取消注释 `ALLOW` 白名单段落，只允许你的上游主机：
  ```js
  const ALLOW = ["ark-cn-beijing.bytedance.net", "api.openai.com"];
  ```
  改完重新 Deploy 即可。

---

## 四、上游是内网地址怎么办？

Cloudflare Worker 运行在 Cloudflare 公网边缘节点，**无法访问只在公司内网可达的地址**。如果 `ark-cn-beijing.bytedance.net` 只能内网访问，则：

- Worker 会返回 `502 Upstream fetch failed`；
- 此时请改用一个**公网可达**的 OpenAI 兼容网关地址作为 Base URL；
- 或者仍走「方案一」——由 GitHub Actions 在服务端生成每日 AI 报告（见 [`DEPLOYMENT.md`](./DEPLOYMENT.md)），前端只做检索展示。

浏览器内实时 LLM 与服务端每日报告两条路径可以并存，互不影响。
