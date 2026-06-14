# spec-executor-testing-04-python-ledger

Python 开发型独立测试仓库。该仓库用于验证 spec-executor 是否能够驱动 Claude/Codex 完成一个小型 Python 代码任务：实现发票行项目汇总、折扣和税额计算，并补齐测试与交付说明。

## 目录

- `docs/PRD.md`：产品需求。
- `docs/HLD.md`：高层设计。
- `docs/LLD.md`：详细设计。
- `docs/DELIVERY.md`：交付验收说明。
- `src/ledger_totals.py`：待完善的 Python 模块。
- `tests/test_ledger_totals.py`：待补齐的测试。
- `tests/test_acceptance_ledger_totals.py`：固定验收测试。
- `tasks/development/`：spec-executor task package。

## 运行

```bash
spec-executor run --spec tasks/development/spec.yaml --workspace ./workspace
```
