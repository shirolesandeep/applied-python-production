# Day 18 — Error Taxonomy & Custom Exceptions

## Goal
Design explicit, domain-specific errors.

## Why
Generic exceptions break APIs and agents.

## What We Did
- Created base domain error
- Added specific user errors
- Updated services to raise domain errors
- Updated tests accordingly

## Rule
Errors are part of your contract.
