# DELIVERY - Python 发票汇总函数

## 验收用途

本文档用于记录执行者完成 `python-ledger-totals` 后的交付证据。执行者必须在完成实现后更新“执行记录”，否则验收不通过。

## 交付物

| 交付物 | 验收要点 |
| --- | --- |
| `src/ledger_totals.py` | 实现 `calculate_invoice_total`，包含输入校验、折扣、税额和两位小数处理。 |
| `tests/test_ledger_totals.py` | 补齐任务级测试，覆盖 PRD/LLD 中的主要场景。 |
| `docs/DELIVERY.md` | 记录实现摘要、验证命令和执行结果。 |

## 验收命令

```bash
python -m unittest
python -m unittest tests.test_acceptance_ledger_totals
```

## 执行记录

实现摘要：已实现 `calculate_invoice_total`，支持行项目小计、折扣、税额、总价计算，拒绝负数量、负单价、负折扣率和负税率，并将金额四舍五入到两位小数；已补齐任务级单元测试覆盖空列表、单行、多行、折扣税率、舍入和负数输入。

验证命令：`python -m unittest`；`python -m unittest tests.test_acceptance_ledger_totals`

执行结果：通过

## 通过标准

- 两条验收命令均返回 0。
- 计算公式与 PRD/LLD 保持一致。
- 负数量、负单价、负折扣率和负税率均抛出 `ValueError`。
- 执行记录中的 `执行结果` 字段必须更新为通过状态。
