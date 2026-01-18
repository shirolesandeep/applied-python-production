## Goal
Learn how to change application behavior at runtime without changing code.

This is done using **feature flags** controlled by configuration.

---

## What is a Feature Flag?

A feature flag is a boolean switch that:
- Enables or disables behavior
- Is controlled via config (YAML / ENV)
- Does NOT require code changes
- Is safe for production

---

## Feature Flags Used

```yaml
features:
  enable_verbose_output: true
