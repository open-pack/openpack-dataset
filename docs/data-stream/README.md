# Sensor Modalities (List of Data Streams)

## Sensor Configuration and File Format

- [Wearables](./wearables.md)
- [Vision](./vision.md)
- [IoT](./iot.md)
- [Metadata](./metadata.md)

## Data Streams

### Wearables

| Data Stream ID | Data Stream Type | Sensor    | Modality                 | Note            |
| -------------- | ---------------- | --------- | ------------------------ | --------------- |
| D0101          | atr-qags         | atr/atr01 | Acc + Gyro + Quaterninon | Right Wrist     |
| D0201          | atr-qags         | atr/atr02 | Acc + Gyro + Quaterninon | Left Wrist      |
| D0301          | atr-qags         | atr/atr03 | Acc + Gyro + Quaterninon | Right Upper Arm |
| D0401          | atr-qags         | atr/atr04 | Acc + Gyro + Quaterninon | Left Upper Arm  |
| D0501          | e4-acc           | e4-01     | Acc                      | Right Wrist     |
| D0502          | e4-bvp           | e4-01     | Blood Volume Pulse (BVP) | Right Wrist     |
| D0503          | e4-eda           | e4-01     | EDA                      | Right Wrist     |
| D0504          | e4-temp          | e4-01     | Temperature              | Right Wrist     |
| D0601          | e4-acc           | e4-02     | Acc                      | Left Wrist      |
| D0602          | e4-bvp           | e4-02     | Blood Volume Pulse (BVP) | Left Wrist      |
| D0603          | e4-eda           | e4-02     | EDA                      | Left Wrist      |
| D0604          | e4-temp          | e4-02     | Temperature              | Left Wrist      |

### Vision

| Data Stream ID | Data Stream Key | Sensor | Modality            | Note       |
| -------------- | --------------- | ------ | ------------------- | ---------- |
| D1101          | kinect-2d-kpt   | kinect | Keypoint (2D)       | Front-view |
| D1102          | kinect-3d-kpt   | kinect | Keypoint (3D)       | Front-view |
| D1103          | kinect-depth    | kinect | Depth (Image)       | Front-view |
| D1201          | rs02-depth      | rs02   | Depth (Image)       | Top-view   |
| D1301          | lidar-depth     | LiDAR  | LiDAR (Point Cloud) | Front-view |

### IoT

| Data Stream ID | Data Stream Key    | Sensor               | Modality | Note |
| -------------- | ------------------ | -------------------- | -------- | ---- |
| D2101          | system-ht-original | ht(handheld scanner) | -        | -    |
| D2202          | system-printer     | Label Printer        | -        | -    |

### Metadata

| Data Stream ID | Data Stream Key    | Sensor | Modality | Note |
| -------------- | ------------------ | ------ | -------- | ---- |
| D3101          | items              | -      | -        | -    |
| D3201          | subjects           | -      | -        | -    |
| D3301          | system-order-sheet | -      | -        | -    |
