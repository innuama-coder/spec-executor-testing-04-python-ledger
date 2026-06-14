# PRD - Python 发票汇总函数

## 背景

测试仓库需要一个足够真实但范围可控的 Python 开发任务，用于验证 spec-executor 对代码实现、测试补齐和文档交付的支持。

## 目标

实现 `calculate_invoice_total(items, discount_rate=0, tax_rate=0)`，根据行项目计算小计、折扣、税额和总价。

## 功能需求

| ID | 需求 |
| --- | --- |
| FR-001 | 支持多个行项目，每个行项目包含 `name`、`quantity`、`unit_price`。 |
| FR-002 | 拒绝负数量、负单价、负折扣率和负税率。 |
| FR-003 | 返回 `subtotal`、`discount`、`tax`、`total` 四个数值字段。 |
| FR-004 | 金额四舍五入到两位小数。 |
| FR-005 | 计算顺序为 `subtotal = sum(quantity * unit_price)`、`discount = subtotal * discount_rate`、`tax = (subtotal - discount) * tax_rate`、`total = subtotal - discount + tax`。 |

## 验收

`python -m unittest` 与固定验收测试 `python -m unittest tests.test_acceptance_ledger_totals` 必须通过。
