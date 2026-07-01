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

## spec-executor 2.3 Agent Task Lifecycle 约束

- 本任务包通过 `spec.yaml` 的 `execution.agent` 声明 Agent 角色、上下文、工具和权限边界。
- `ENV` 仅用于 tmux session 环境变量注入，不作为普通上下文文件读取、总结或输出。
- 默认输出、报告和交付说明不得包含 `ENV` 变量值。
- `spec.yaml` 中存在 review items 时，必须在同一 JOB 内逐条完成修复、验证和交付记录。
- 运行过程必须保持 log-first detection 边界；screen capture 只作为显式查看或失败证据。
