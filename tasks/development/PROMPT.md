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

## spec-executor 2.3 Agent Task Lifecycle 约束

- 本任务包通过 `spec.yaml` 的 `execution.agent` 声明 Agent 角色、上下文、工具和权限边界。
- `ENV` 仅用于 tmux session 环境变量注入，不作为普通上下文文件读取、总结或输出。
- 默认输出、报告和交付说明不得包含 `ENV` 变量值。
- `spec.yaml` 中存在 review items 时，必须在同一 JOB 内逐条完成修复、验证和交付记录。
- 运行过程必须保持 log-first detection 边界；screen capture 只作为显式查看或失败证据。
