# LLD - Python 发票汇总函数

## 接口

```python
def calculate_invoice_total(items, discount_rate=0, tax_rate=0):
    ...
```

## 规则

| 场景 | 行为 |
| --- | --- |
| 空行项目 | 返回所有金额为 `0.0`。 |
| 非法金额 | 抛出 `ValueError`。 |
| 合法输入 | 返回四个两位小数字段。 |

## 计算公式

| 字段 | 公式 |
| --- | --- |
| `subtotal` | `sum(item["quantity"] * item["unit_price"] for item in items)` |
| `discount` | `subtotal * discount_rate` |
| `tax` | `(subtotal - discount) * tax_rate` |
| `total` | `subtotal - discount + tax` |

## 测试

- 空列表。
- 单行项目。
- 多行项目。
- 折扣与税率。
- 负数输入。
