# Data Stream: Preprocessed

- [1. `imu-with-operation-label`](#1-imu-with-operation-label)
  - [1.1. Data Location](#11-data-location)
  - [1.2. File Format (CSV)](#12-file-format-csv)

## 1. `imu-with-operation-label`

It's not easy to combine sensor data and annotations for bigginers.
Therefore we prepared this data stream for quick start.

In this data stream, IMU data from 4 ATR sensors and work operation labels are combined in advance.
So you can start analysis and model training immediately.
The files are available in [zenodo](https://zenodo.org/records/8145223/files/preprocessed-IMU-with-operation-labels.zip?download=1).

- Data Stream ID: `D4101`
- Config File: None
- Sensor:
  - Device: [ATR TSND151](http://www.atr-p.com/products/TSND121_151.html) + Annotation
  - Sensor Type: IMU (Acc + Gyro + Quaternion) + Work Operation Label
  - Frame Rate: 30 Hz

### 1.1. Data Location

```text
${path.openpack.rootdir}/preprocessed/imuWithOperationLabel/${user}-${session}.csv
```

### 1.2. File Format (CSV)

| #   | Column Name  | Unit         | Dtype | Note                    |
| --- | ------------ | ------------ | ----- | ----------------------- |
| 0   | unixtime     | milli second | int   |                         |
| 1   | operation    |              | int   | Work Operatopn Class ID |
| 2   | atr01/acc_x  | G            | float |                         |
| 3   | atr01/acc_y  | G            | float |                         |
| 4   | atr01/acc_z  | G            | float |                         |
| 5   | atr01/gyro_x | dps          | float |                         |
| 6   | atr01/gyro_y | dps          | float |                         |
| 7   | atr01/gyro_z | dps          | float |                         |
| 8   | atr01/quat_w |              | float |                         |
| 9   | atr01/quat_x |              | float |                         |
| 10  | atr01/quat_y |              | float |                         |
| 11  | atr01/quat_z |              | float |                         |
| 12  | atr02/acc_x  | G            | float |                         |
| 13  | atr02/acc_y  | G            | float |                         |
| 14  | atr02/acc_z  | G            | float |                         |
| 15  | atr02/gyro_x | dps          | float |                         |
| 16  | atr02/gyro_y | dps          | float |                         |
| 17  | atr02/gyro_z | dps          | float |                         |
| 18  | atr02/quat_w |              | float |                         |
| 19  | atr02/quat_x |              | float |                         |
| 20  | atr02/quat_y |              | float |                         |
| 21  | atr02/quat_z |              | float |                         |
| 22  | atr03/acc_x  | G            | float |                         |
| 23  | atr03/acc_y  | G            | float |                         |
| 24  | atr03/acc_z  | G            | float |                         |
| 25  | atr03/gyro_x | dps          | float |                         |
| 26  | atr03/gyro_y | dps          | float |                         |
| 27  | atr03/gyro_z | dps          | float |                         |
| 28  | atr03/quat_w |              | float |                         |
| 29  | atr03/quat_x |              | float |                         |
| 30  | atr03/quat_y |              | float |                         |
| 31  | atr03/quat_z |              | float |                         |
| 32  | atr04/acc_x  | G            | float |                         |
| 33  | atr04/acc_y  | G            | float |                         |
| 34  | atr04/acc_z  | G            | float |                         |
| 35  | atr04/gyro_x | dps          | float |                         |
| 36  | atr04/gyro_y | dps          | float |                         |
| 37  | atr04/gyro_z | dps          | float |                         |
| 38  | atr04/quat_w |              | float |                         |
| 39  | atr04/quat_x |              | float |                         |
| 40  | atr04/quat_y |              | float |                         |
| 41  | atr04/quat_z |              | float |                         |
