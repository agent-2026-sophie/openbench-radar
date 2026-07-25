"""Command line interface for OpenBench Radar."""
from __future__ import annotations

import argparse
import logging
import sys

from .config import Config
from .pipeline import Pipeline


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="openbench-agent",
        description="Automated retrieval, research & reporting for open AI/LLM benchmarks.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run the full retrieve -> research -> report pipeline.")
    run.add_argument("--config", default="config/config.yaml", help="Path to config file.")
    run.add_argument("--output", default="reports", help="Output directory for reports.")
    run.add_argument("--topics", help="Comma-separated topics to override config.")
    run.add_argument("--max-items", type=int, help="Max items per source.")
    run.add_argument("--no-llm", action="store_true", help="Force extractive fallback.")
    run.add_argument(
        "--format", choices=["md", "html", "both"], default="both", help="Report format."
    )
    run.add_argument("--dry-run", action="store_true", help="Do everything except write files.")
    run.add_argument("-v", "--verbose", action="store_true", help="Verbose logging.")

    sub.add_parser("version", help="Print version and exit.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "version":
        from . import __version__

        print(f"openbench-radar {__version__}")
        return 0

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    config = Config.load(args.config)
    if args.no_llm:
        config.llm.api_key = None  # force fallback path

    topics = None
    if args.topics:
        topics = [t.strip() for t in args.topics.split(",") if t.strip()]

    pipeline = Pipeline(config)
    result, written = pipeline.run(
        topics=topics,
        output_dir=args.output,
        max_items=args.max_items,
        fmt=args.format,
        dry_run=args.dry_run,
    )

    print("\n" + "=" * 60)
    print(f"  Analyzed {len(result.items)} items "
          f"({'LLM' if result.llm_used else 'extractive'} summary)")
    if written:
        for fmt, path in written.items():
            print(f"  {fmt:>4}: {path}")
    else:
        print("  (dry run — no files written)")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
