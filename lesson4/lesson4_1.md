## 更改日期型別和更新字串成為Date

```sql
ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期::DATE;
```