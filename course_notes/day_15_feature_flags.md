# Day 15 — Feature Flags & Runtime Toggles  

## Why Day 15 Matters

This day introduces **production control without redeployments**.

Most beginners hardcode behavior.
Professionals externalize behavior using configuration.

Feature flags are the bridge.

---

## Core Teaching Objective

Students should understand:

- Behavior should NOT be hardcoded
- Configuration controls runtime behavior
- Feature flags allow safe experimentation
- Systems can evolve without redeploys

---

## What We Implemented

### Feature Flag
```yaml
features:
  enable_verbose_output: true
Wiring Flow
YAML → AppConfig → main.py → service method

This enforces:

Separation of concerns

Clean architecture

Testable code

Key Design Decisions Explained
1. Flags live in config, not code
Avoid if debug: inside services

Flags must be data-driven

2. Entry point controls behavior
main.py decides how services behave

Services stay reusable and clean

3. Services accept behavior as input
process(verbose: bool)

No global flags

No hidden state