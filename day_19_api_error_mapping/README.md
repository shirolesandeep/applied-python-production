# Day 19 — API Error Mapping

## Goal
Translate domain errors into HTTP responses cleanly.

## What We Did
- Added FastAPI boundary
- Mapped domain errors to HTTP errors
- Kept services HTTP-agnostic

## Rule
Services raise errors. APIs translate them.
