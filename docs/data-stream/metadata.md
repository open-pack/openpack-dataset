# Data Stream: Metadata

- [1. `item-list`](#1-item-list)
  - [1.1. Data Location](#11-data-location)
  - [1.2. File Format (CSV)](#12-file-format-csv)
- [2. `subject-attribute`](#2-subject-attribute)
  - [2.1. Data Location](#21-data-location)
- [3. `system-order-sheet`](#3-system-order-sheet)
  - [3.1. Relative Path](#31-relative-path)
  - [3.2. File Format (CSV)](#32-file-format-csv)
  - [3.3. Sample Data](#33-sample-data)

## 1. `item-list`

The information about products that are used in the experiment.
This data includes the product name, product code (JAN code), and size.

- Data Stream ID: `D3101`
- Config File: None
- Sensor: None

### 1.1. Data Location

The data is available on this repo. See [data/items.csv](../../data/items.csv)

### 1.2. File Format (CSV)

| #   | Column Name   | Unit | Dtype | Note |
| --- | ------------- | ---- | ----- | ---- |
| 0   | item_id       | None | str   |      |
| 1   | name          | None | str   |      |
| 1   | JAN_code      | None | str   |      |
| 1   | height\_\_cm  | cm   | int   |      |
| 1   | width\_\_cm   | cm   | int   |      |
| 1   | depth\_\_cm   | cm   | int   |      |
| 1   | size_category | None | str   |      |
| 1   | amount        | None | int   |      |
| 1   | url           | None | str   |      |

## 2. `subject-attribute`

- Data Stream ID: `D3201`
- Config File: None
- Sensor: None (Information collected through surveys)

### 2.1. Data Location

This data is available on this repo. See [docs/SUBJECT.md](../SUBJECTS.md).

## 3. `system-order-sheet`

This data includes item IDs to be shipped in each box.

- Data Stream ID: `D3301`
- Config File: [system-order-sheet.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/system-order-sheet.yaml)
- Sensor
  - Data Type: system/order-sheet

### 3.1. Relative Path

```text
${path.openpack.rootdir}/${user.name}/system/order-sheet//${session}.csv
```

### 3.2. File Format (CSV)

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

### 3.3. Sample Data

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
