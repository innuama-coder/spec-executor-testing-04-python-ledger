# CLAUDE.md

## Assignment

完成 Python 开发任务：根据 `docs/PRD.md`、`docs/HLD.md`、`docs/LLD.md` 实现发票汇总函数，并补齐测试和交付说明。

## Context To Load

- `docs/PRD.md`
- `docs/HLD.md`
- `docs/LLD.md`
- `src/ledger_totals.py`
- `tests/test_ledger_totals.py`

## Constraints

- 不引入第三方依赖。
- 不修改任务包目录。
- 不删除已有测试。

## Acceptance Criteria

- `python -m unittest` 通过。
- `python -m unittest tests.test_acceptance_ledger_totals` 通过。
- 覆盖空列表、多行项目、折扣、税率和非法输入。
- 更新 `docs/DELIVERY.md`，并写入独立一行 `执行结果：通过`。

## Verification Method

运行 `python -m unittest`。

## Handoff

说明修改文件、测试结果和边界条件。
