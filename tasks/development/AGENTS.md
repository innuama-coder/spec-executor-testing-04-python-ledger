# AGENTS.md

## Current Task

Implement the Python ledger total feature described by the repository PRD/HLD/LLD.

## Source Of Truth

- `PROMPT.md`
- `docs/PRD.md`
- `docs/HLD.md`
- `docs/LLD.md`

## Allowed Scope

- `src/ledger_totals.py`
- `tests/test_ledger_totals.py`
- `docs/DELIVERY.md`

## Forbidden Scope

- Do not edit `tasks/development`.
- Do not add external dependencies.

## Completion Criteria

All unit tests and the fixed acceptance test pass. `docs/DELIVERY.md` records the implementation and contains a standalone line `执行结果：通过`.

## Required Verification

Run `python -m unittest`.
Run `python -m unittest tests.test_acceptance_ledger_totals`.
