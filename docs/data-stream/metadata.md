# Data Stream: Metadata

- [1. `system-order-sheet`](#1-system-order-sheet)
  - [1.1. Relative Path](#11-relative-path)
  - [1.2. File Format (CSV)](#12-file-format-csv)
  - [1.3. Sample Data](#13-sample-data)

## 1. `system-order-sheet`

- Data Stream ID: `D3301`
- Config File: [system-order-sheet.yaml](../configs/dataset/stream/system-order-sheet.yaml)
- Sensor
  - Data Type: system/order-sheet

### 1.1. Relative Path

```text
${path.openpack.rootdir}/${user.name}/system/order-sheet//${session}.csv
```

### 1.2. File Format (CSV)

| #   | Column Name  | Unit | Dtype | Note                                       |
| --- | ------------ | ---- | ----- | ------------------------------------------ |
| 0   | sheet_no     | None | str   | format = `DEN{session_no:0=4}{box_no:0=2}` |
| 1   | session      | None | str   |                                            |
| 2   | box          | None | str   |                                            |
| 3   | pattern      | None | str   |                                            |
| 4   | total_amount | None | str   |                                            |
| 5   | item1        | None | str   |                                            |
| 6   | item2        | None | str   |                                            |
| 7   | item3        | None | str   |                                            |
| 8   | item4        | None | str   |                                            |
| 9   | item5        | None | str   |                                            |
| 10  | amount1      | None | str   |                                            |
| 11  | amount2      | None | str   |                                            |
| 12  | amount3      | None | str   |                                            |
| 13  | amount4      | None | str   |                                            |
| 14  | amount5      | None | str   |                                            |

### 1.3. Sample Data

| sheet_no | session   | box   | pattern | total_amount | item1 | item2 | item3 | item4 | item5 | amount1 | amount2 | amount3 | amount4 | amount5 |     |
| -------- | --------- | ----- | ------- | ------------ | ----- | ----- | ----- | ----- | ----- | ------- | ------- | ------- | ------- | ------- | --- |
| 0        | DEN050001 | S0500 | 1       | M5           | 5     | 301   | 315   | 403   | 404   | 405     | 1       | 1       | 1       | 1       | 1   |
| 1        | DEN050002 | S0500 | 2       | M1           | 1     | 402   |       |       |       |         | 1       |         |         |         |     |
| 2        | DEN050003 | S0500 | 3       | L4           | 4     | 501   | 502   | 503   | 601   |         | 1       | 1       | 1       | 1       |     |
| 3        | DEN050004 | S0500 | 4       | S1           | 1     | 203   |       |       |       |         | 1       |         |         |         |     |
| 4        | DEN050005 | S0500 | 5       | S2           | 2     | 107   | 221   |       |       |         | 1       | 1       |         |         |     |
| 5        | DEN050006 | S0500 | 6       | S1           | 1     | 219   |       |       |       |         | 1       |         |         |         |     |
| 6        | DEN050007 | S0500 | 7       | M1           | 1     | 401   |       |       |       |         | 1       |         |         |         |     |
| 7        | DEN050008 | S0500 | 8       | S1           | 2     | 113   |       |       |       |         | 2       |         |         |         |     |
| 8        | DEN050009 | S0500 | 9       | L1           | 1     | 602   |       |       |       |         | 1       |         |         |         |     |
