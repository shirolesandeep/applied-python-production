Day 2 Notes – Execution Safety & Imports

Key Concept:
Importing a Python file should NEVER execute business logic.

What Students Usually Do:
- Write logic at top level
- Assume code only runs when executed directly
- Forget that import also executes code

What We Taught:
- Python executes files top-to-bottom
- Importing a file runs all top-level code
- This causes hidden side effects in production

Core Solution:
- Move logic into functions
- Use `if __name__ == "__main__":` as a safety gate

Important Rules:
- Only definitions (functions, classes, constants) at import time
- No database calls, prints, or API calls on import
- Execution must be explicit and controlled

One-Line Teaching Statement:
"If importing a file can change system state, it is a bug."

Outcome:
Students now understand how to write import-safe,
reusable Python modules for APIs, tests, and services.
