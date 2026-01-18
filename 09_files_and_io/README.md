# Day 9 – Files & Safe I/O

## Problem
Naive file handling causes crashes and silent failures.

## Solution
We use pathlib to:
- validate paths
- handle files safely
- write portable code

## Key Takeaways
- Paths are objects, not strings
- Validate before reading or writing
- Fail fast on missing files
