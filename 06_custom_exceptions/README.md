# Day 6 – Custom Exceptions & Error Design

## Problem
Generic exceptions hide intent and make error handling unclear.

## Solution
We define domain-specific exceptions to:
- communicate intent
- enable selective handling
- improve debuggability

## Key Takeaways
- Never raise plain Exception
- Use custom exception hierarchies
- Raise early, handle at boundaries