# Data Stream: Wearables

- [1. `atr-qags`](#1-atr-qags)
  - [1.1. Relative Path](#11-relative-path)
  - [1.2. File Format (CSV)](#12-file-format-csv)
  - [1.3. Sample Data](#13-sample-data)
- [2. `e4-acc`](#2-e4-acc)
  - [2.1. Relative Path](#21-relative-path)
  - [2.2. File Format (CSV)](#22-file-format-csv)
  - [2.3. Sample Data](#23-sample-data)
- [3. `e4-bvp`](#3-e4-bvp)
  - [3.1. Relative Path](#31-relative-path)
  - [3.2. File Format (CSV)](#32-file-format-csv)
  - [3.3. Sample Data](#33-sample-data)
- [4. `e4-eda`](#4-e4-eda)
  - [4.1. Relative Path](#41-relative-path)
  - [4.2. File Format (CSV)](#42-file-format-csv)
  - [4.3. Sample Data](#43-sample-data)
- [5. `e4-temp`](#5-e4-temp)
  - [5.1. Relative Path](#51-relative-path)
  - [5.2. File Format (CSV)](#52-file-format-csv)
  - [5.3. Sample Data](#53-sample-data)

## 1. `atr-qags`

- Data Stream ID: `D0101`, `D0201`, `D0301`, `D0401`
- Sensor:
  - Device: [ATR TSND151](http://www.atr-p.com/products/TSND121_151.html)
  - Sensor Type: IMU (Acc + Gyro + Quaternion)
  - Frame Rate: 30 Hz
- Config File: [atr-qags.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/atr-qags.yaml)

### 1.1. Relative Path

- device: `atr01` for `D0101`, `atr02` for `D0201`, `atr03` for `D0301`, `atr04` for `D0401`

```text
${path.openpack.rootdir}/${user.name}/atr/${device}/${session}.csv
```

### 1.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | unixtime    | milli second | int   |      |
| 1   | acc_x       | G            | float |      |
| 2   | acc_y       | G            | float |      |
| 3   | acc_z       | G            | float |      |
| 4   | gyro_x      | dps          | float |      |
| 5   | gyro_y      | dps          | float |      |
| 6   | gyro_z      | dps          | float |      |
| 7   | quat_w      |              | float |      |
| 8   | quat_x      |              | float |      |
| 9   | quat_y      |              | float |      |
| 10  | quat_z      |              | float |      |

### 1.3. Sample Data

| unixtime      | acc_x  | acc_y  | acc_z  | gyro_x | gyro_y | gyro_z | quat_w | quat_x  | quat_y  | quat_z |
| ------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------- | ------- | ------ |
| 1648531521000 | 0.3795 | 0.9069 | 0.1097 | 0.67   | 1.76   | -0.24  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521030 | 0.3728 | 0.9221 | 0.1092 | 0.36   | 0.6    | -1.21  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521060 | 0.3946 | 0.9261 | 0.0999 | -0.06  | -1.21  | -1.28  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521090 | 0.3924 | 0.9162 | 0.0982 | 0.3    | 0.54   | -0.48  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521120 | 0.3835 | 0.9146 | 0.1037 | 0.42   | 0.42   | -0.42  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521150 | 0.3916 | 0.914  | 0.1074 | 0.42   | -0.12  | -1.03  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521180 | 0.3916 | 0.9196 | 0.1109 | 0.73   | 0.73   | -0.91  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521210 | 0.3902 | 0.9201 | 0.1083 | 0.6    | 1.4    | -0.54  | 0.5312 | -0.6406 | -0.2343 | 0.5    |
| 1648531521240 | 0.3809 | 0.9228 | 0.108  | 0.54   | 1.52   | -0.54  | 0.5312 | -0.6406 | -0.2343 | 0.5    |

## 2. `e4-acc`

- Data Stream ID: `D0501`, `D0601`
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Acc
  - Frame Rate: 32 Hz
- Config File: [e4-acc.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/e4-acc.yaml)

### 2.1. Relative Path

- device: `e401` for `D0501`, `e402` for `D0601`

```text
${path.openpack.rootdir}/${user.name}/e4/${device}/acc/${session}.csv
```

### 2.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second | int   |      |
| 1   | acc_x       | G            | float |      |
| 2   | acc_y       | G            | float |      |
| 3   | acc_z       | G            | float |      |

### 2.3. Sample Data

| time          | acc_x                | acc_y                | acc_z                |
| ------------- | -------------------- | -------------------- | -------------------- |
| 1648531510031 | -0.04142597115222834 | -0.09241178180112475 | 0.011153146079446091 |
| 1648531510062 | -0.04142597115222834 | -0.09241178180112475 | 0.011153146079446091 |
| 1648531510093 | -0.04301927773500635 | -0.09241178180112475 | 0.007966532913890064 |
| 1648531510124 | -0.04142597115222834 | -0.09400508838390277 | 0.007966532913890064 |
| 1648531510156 | -0.04142597115222834 | -0.09241178180112475 | 0.007966532913890064 |
| 1648531510187 | -0.04142597115222834 | -0.09400508838390277 | 0.007966532913890064 |
| 1648531510218 | -0.04301927773500635 | -0.09400508838390277 | 0.007966532913890064 |
| 1648531510249 | -0.04142597115222834 | -0.09400508838390277 | 0.007966532913890064 |
| 1648531510281 | -0.04142597115222834 | -0.09400508838390277 | 0.006373226331112052 |

## 3. `e4-bvp`

- Data Stream ID: `D0502`, `D0602`
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Blood Volume Pulse (BVP)
  - Frame Rate: 64 Hz
- Config File: [e4-bvp.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/e4-bvp.yaml)

### 3.1. Relative Path

- - device: `e401` for `D0502`, `e402` for `D0602`

```text
${path.openpack.rootdir}/${user.name}/e4/${device}/bvp/${session}.csv
```

### 3.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second | int   |      |
| 1   | bvp         | mmHg         | float |      |

### 3.3. Sample Data

| time          | bvp     |
| ------------- | ------- |
| 1648531510011 | -110.82 |
| 1648531510027 | -111.75 |
| 1648531510043 | -111.07 |
| 1648531510058 | -107.78 |
| 1648531510074 | -101.5  |
| 1648531510089 | -92.49  |
| 1648531510105 | -81.53  |
| 1648531510121 | -69.63  |
| 1648531510136 | -57.81  |

## 4. `e4-eda`

- Data Stream ID: `D0503`, `D0603`
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: EDA
  - Frame Rate: 4 Hz
- Config File: [e4-eda.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/e4-eda.yaml)

### 4.1. Relative Path

- device: `e401` for `D0503`, `e402` for `D0603`

```text
${path.openpack.rootdir}/${user.name}/e4/${device}/eda/${session}.csv
```

### 4.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second | int   |      |
| 1   | eda         | microsiemens | float |      |

### 4.3. Sample Data

| time          | eda      |
| ------------- | -------- |
| 1648531510238 | 0.589199 |
| 1648531510488 | 0.585357 |
| 1648531510738 | 0.585357 |
| 1648531510988 | 0.587919 |
| 1648531511238 | 0.586638 |
| 1648531511489 | 0.589199 |
| 1648531511739 | 0.59048  |
| 1648531511989 | 0.589199 |
| 1648531512239 | 0.589199 |

## 5. `e4-temp`

- Data Stream ID: `D0504`, `D0604`
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Temperature
  - Frame Rate: 4 Hz
- Config File: [e4-temp.yaml](https://github.com/open-pack/openpack-toolkit/tree/main/configs/dataset/stream/e4-temp.yaml)

### 5.1. Relative Path

- device: `e401` for `D0504`, `e402` for `D0604`

```text
${path.openpack.rootdir}/${user.name}/e4/${device}/temp/${session}.csv
```

### 5.2. File Format (CSV)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second | int   |      |
| 1   | temp        | microsiemens | float |      |

### 5.3. Sample Data

| time          | temp  |
| ------------- | ----- |
| 1648531510238 | 33.0  |
| 1648531510488 | 33.0  |
| 1648531510738 | 33.0  |
| 1648531510988 | 33.0  |
| 1648531511238 | 33.03 |
| 1648531511489 | 33.03 |
| 1648531511739 | 33.03 |
| 1648531511989 | 33.03 |
| 1648531512239 | 33.0  |
