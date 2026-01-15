Day 12 — Configuration & ENV

Core shift today:
- From hardcoded behavior
- To environment-controlled behavior

What students learned:
- Environment variables are runtime inputs
- Same code can behave differently
- Entry point controls configuration
- Services remain pure and reusable

Key teaching points:
- Never change code for dev/prod differences
- Logging level is configuration, not logic
- `.env` is a convenience, not magic
- OS environment is the source of truth

Common confusion to address:
- `.env` does NOT auto-load (until Day 13)
- Running same command twice = same behavior unless env changes

One-line takeaway:
"Production systems change behavior via config, not commits."

This day prepares students for:
- Cloud deployments
- CI/CD pipelines
- Agent runtimes
- API services

Do not rush this concept.
It is foundational.