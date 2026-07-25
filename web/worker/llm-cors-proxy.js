// Cloudflare Worker — CORS proxy for OpenAI-compatible LLM APIs (e.g. ARK).
//
// How it works:
//   Browser  --POST-->  this Worker  --POST-->  upstream LLM endpoint
//   The browser puts the REAL upstream URL in the `X-Target-Url` header and its
//   API key in the normal `Authorization: Bearer <key>` header. The Worker
//   forwards the request and adds permissive CORS headers to the response, so the
//   browser (which cannot call the upstream directly due to CORS/HTTP) succeeds.
//
// Deploy: paste this into a new Worker in the Cloudflare dashboard (see README.md).

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Target-Url",
  "Access-Control-Max-Age": "86400",
};

export default {
  async fetch(request) {
    // CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS });
    }
    if (request.method !== "POST") {
      return json({ error: "Only POST is supported" }, 405);
    }

    const target = request.headers.get("X-Target-Url");
    if (!target || !/^https?:\/\//.test(target)) {
      return json({ error: "Missing or invalid X-Target-Url header" }, 400);
    }

    // OPTIONAL security allowlist — recommended for a public Worker.
    // Uncomment and edit to restrict which upstream hosts may be proxied:
    // const ALLOW = ["ark-cn-beijing.bytedance.net", "api.openai.com"];
    // if (!ALLOW.some((h) => target.includes(h))) {
    //   return json({ error: "Upstream host not allowed" }, 403);
    // }

    const headers = new Headers();
    headers.set("Content-Type", request.headers.get("Content-Type") || "application/json");
    const auth = request.headers.get("Authorization");
    if (auth) headers.set("Authorization", auth);

    const body = await request.text();

    let upstream;
    try {
      upstream = await fetch(target, { method: "POST", headers, body });
    } catch (e) {
      return json({ error: "Upstream fetch failed: " + e.message }, 502);
    }

    const respHeaders = new Headers(upstream.headers);
    for (const [k, v] of Object.entries(CORS)) respHeaders.set(k, v);
    // Content-Encoding from upstream can conflict after re-streaming; drop it.
    respHeaders.delete("content-encoding");
    return new Response(upstream.body, { status: upstream.status, headers: respHeaders });
  },
};

function json(obj, status) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...CORS },
  });
}
