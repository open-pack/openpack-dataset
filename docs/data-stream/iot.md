# Data Stream: IoT

- [1. `system-ht-original`](#1-system-ht-original)
  - [1.1. Relative Path](#11-relative-path)
  - [1.2. File Format (CSV)](#12-file-format-csv)
  - [1.3. Sample Data](#13-sample-data)
- [2. `system-printer`](#2-system-printer)
  - [2.1. Relative Path](#21-relative-path)
  - [2.2. File Format (CSV)](#22-file-format-csv)
  - [2.3. Sample Data](#23-sample-data)

## 1. `system-ht-original`

- Data Stream ID: `D2101`
- Sensor
  - Device: [8001-C Portable Terminal](https://shop.e-welcom.com/shop/g/g8001C-02/)
  - Sensor Type: IoT/handheld-scanner
- Config File: [system-ht-original.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/system-ht-original.yaml)

### 1.1. Relative Path

```text
${path.openpack.rootdir}/${user.name}/system/ht/${session}.csv
```

### 1.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype            | Note |
| --- | ----------- | ------------ | ---------------- | ---- |
| 0   | unixtime    | milli second | int              |      |
| 1   | datetime    | None         | str (ISO format) |      |
| 2   | order_sheet | None         | str              |      |
| 3   | box         | None         | str              |      |
| 4   | item        | None         | str              |      |

### 1.3. Sample Data

| unixtime      | datetime                  | order_sheet | box   | item    |
| ------------- | ------------------------- | ----------- | ----- | ------- |
| 1648531583000 | 2022-03-29 14:26:23+09:00 | DEN050001   | BOX01 | ITEM301 |
| 1648531584000 | 2022-03-29 14:26:24+09:00 | DEN050001   | BOX01 | ITEM315 |
| 1648531585000 | 2022-03-29 14:26:25+09:00 | DEN050001   | BOX01 | ITEM403 |
| 1648531585000 | 2022-03-29 14:26:25+09:00 | DEN050001   | BOX01 | ITEM404 |
| 1648531586000 | 2022-03-29 14:26:26+09:00 | DEN050001   | BOX01 | ITEM405 |
| 1648531670000 | 2022-03-29 14:27:50+09:00 | DEN050002   | BOX02 | ITEM402 |
| 1648531757000 | 2022-03-29 14:29:17+09:00 | DEN050003   | BOX03 | ITEM501 |
| 1648531757000 | 2022-03-29 14:29:17+09:00 | DEN050003   | BOX03 | ITEM502 |
| 1648531758000 | 2022-03-29 14:29:18+09:00 | DEN050003   | BOX03 | ITEM503 |

## 2. `system-printer`

- Data Stream ID: `D2201`
- Sensor
  - Device: [QL-820NWB](https://www.brother.co.jp/product/labelprinter/ql820nwb/index.aspx) (pesudo log data)
  - Data Type: IoT/printer/pseudo-data
- Config File: [system-printer.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/system-printer.yaml)

### 2.1. Relative Path

```text
${path.openpack.rootdir}/${user.name}/system/printer/${session}.csv
```

### 2.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype            | Note |
| --- | ----------- | ------------ | ---------------- | ---- |
| 0   | unixtime    | milli second | int              |      |
| 1   | datetime    | None         | str (ISO format) |      |
| 2   | order_sheet | None         | str              |      |

### 2.3. Sample Data

| unixtime      | datetime                  | order_sheet |
| ------------- | ------------------------- | ----------- |
| 1648531589000 | 2022-03-29 14:26:29+09:00 | DEN050001   |
| 1648531674000 | 2022-03-29 14:27:54+09:00 | DEN050002   |
| 1648531762000 | 2022-03-29 14:29:22+09:00 | DEN050003   |
| 1648531826000 | 2022-03-29 14:30:26+09:00 | DEN050004   |
| 1648531905000 | 2022-03-29 14:31:45+09:00 | DEN050005   |
| 1648531952000 | 2022-03-29 14:32:32+09:00 | DEN050006   |
| 1648532024000 | 2022-03-29 14:33:44+09:00 | DEN050007   |
| 1648532101000 | 2022-03-29 14:35:01+09:00 | DEN050008   |
| 1648532174000 | 2022-03-29 14:36:14+09:00 | DEN050009   |
