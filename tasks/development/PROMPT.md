# PROMPT.md

## 任务目标

根据工作文档实现 Python 发票汇总函数，补齐测试，并输出交付说明。

## 必读上下文

1. `docs/PRD.md`
2. `docs/HLD.md`
3. `docs/LLD.md`
4. `src/ledger_totals.py`
5. `tests/test_ledger_totals.py`

## 交付物

- `src/ledger_totals.py`
- `tests/test_ledger_totals.py`
- `docs/DELIVERY.md`

## 验收标准

- `python -m unittest` 通过。
- `python -m unittest tests.test_acceptance_ledger_totals` 通过。
- `docs/DELIVERY.md` 中包含独立一行 `执行结果：通过`。
- 实现符合 PRD/HLD/LLD。
- 不修改 `tasks/development` 目录。

## Handoff

最终回复包含修改摘要、验证命令和结果。
