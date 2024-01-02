# Sensor Modalities (List of Data Streams)

## Table of Contents

- [Sensor Modalities (List of Data Streams)](#sensor-modalities-list-of-data-streams)
  - [Table of Contents](#table-of-contents)
  - [\[1\] `atr-qags`](#1-atr-qags)
    - [1-1: Relative Path](#1-1-relative-path)
    - [1-2: File Format (`csv`)](#1-2-file-format-csv)
  - [\[2\] `e4-acc`](#2-e4-acc)
    - [2-1: Relative Path](#2-1-relative-path)
    - [2-2: File Format (`csv`)](#2-2-file-format-csv)
  - [\[3\] `e4-bvp`](#3-e4-bvp)
    - [3-1: Relative Path](#3-1-relative-path)
    - [3-2: File Format (`csv`)](#3-2-file-format-csv)
  - [\[4\] `e4-eda`](#4-e4-eda)
    - [4-1: Relative Path](#4-1-relative-path)
    - [4-2: File Format (`csv`)](#4-2-file-format-csv)
  - [\[5\] `e4-temp`](#5-e4-temp)
    - [5-1: Relative Path](#5-1-relative-path)
    - [5-2: File Format (`csv`)](#5-2-file-format-csv)
  - [\[6\] `kinect-2d-kpt`](#6-kinect-2d-kpt)
    - [6-1: Relative Path](#6-1-relative-path)
    - [6-2: File Format (`json`)](#6-2-file-format-json)
  - [\[7\] `kinect-3d-kpt`](#7-kinect-3d-kpt)
    - [7-1: Relative Path](#7-1-relative-path)
    - [7-2: File Format (`json`)](#7-2-file-format-json)
  - [\[8\] `kinect-depth`](#8-kinect-depth)
    - [8-1: Relative Path](#8-1-relative-path)
    - [8-2: File Format (`16bit Grayscal PNG`)](#8-2-file-format-16bit-grayscal-png)
  - [\[9\] `rs02-depth`](#9-rs02-depth)
    - [9-1: Relative Path](#9-1-relative-path)
    - [9-2: File Format (`16bit Grayscal PNG`)](#9-2-file-format-16bit-grayscal-png)
  - [\[10\] `lidar-depth`](#10-lidar-depth)
    - [10-1: Relative Path](#10-1-relative-path)
    - [10-2: File Format (`Point Cloud`)](#10-2-file-format-point-cloud)
  - [\[11\] `system-ht-original`](#11-system-ht-original)
    - [11-1: Relative Path](#11-1-relative-path)
    - [11-2: File Format (`csv`)](#11-2-file-format-csv)
  - [\[12\] `system-order-sheet`](#12-system-order-sheet)
    - [12-1: Path](#12-1-path)
    - [12-2: File Format (`csv`)](#12-2-file-format-csv)
  - [\[13\] `system-printer`](#13-system-printer)
    - [13-1: Relative Path](#13-1-relative-path)
    - [13-1: File Format (`csv`)](#13-1-file-format-csv)

## [1] `atr-qags`

- Config File: [atr-qags.yaml](../configs/dataset/stream/atr-qags.yaml)
- Sensor:
  - Device: [ATR TSND151](http://www.atr-p.com/products/TSND121_151.html)
  - Sensor Type: IMU (Acc + Gyro + Quaternion)
  - Frame Rate: 30 Hz

### 1-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/atr/${device}/${session}.csv
```

### 1-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | unixtime    | milli second |       |      |
| 1   | acc_x       | G            |       |      |
| 2   | acc_y       | G            |       |      |
| 3   | acc_z       | G            |       |      |
| 4   | gyro_x      | dps          |       |      |
| 5   | gyro_y      | dps          |       |      |
| 6   | gyro_z      | dps          |       |      |
| 7   | quat_w      |              |       |      |
| 8   | quat_x      |              |       |      |
| 9   | quat_y      |              |       |      |
| 10  | quat_z      |              |       |      |

## [2] `e4-acc`

- Config File: [e4-acc.yaml](../configs/dataset/stream/e4-acc.yaml)
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Acc
  - Frame Rate: 32 Hz

### 2-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/acc/${session}.csv
```

### 2-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second |       |      |
| 1   | acc_x       | G            |       |      |
| 2   | acc_y       | G            |       |      |
| 3   | acc_z       | G            |       |      |

## [3] `e4-bvp`

- Config File: [e4-bvp.yaml](../configs/dataset/stream/e4-bvp.yaml)
- Python Module: [`openpack_toolkit.configs.datasets.streams.E4_BVP_STREAM`](../openpack_toolkit/configs/datasets/streams.py)
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Blood Volume Pulse (BVP)
  - Frame Rate: 64 Hz

### 3-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/bvp/${session}.csv
```

### 3-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second |       |      |
| 1   | bvp         | mmHg         |       |      |

## [4] `e4-eda`

- Config File: [e4-eda.yaml](../configs/dataset/stream/e4-eda.yaml)
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: EDA
  - Frame Rate: 4 Hz

### 4-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/eda/${session}.csv
```

### 4-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second |       |      |
| 1   | eda         | microsiemens |       |      |

## [5] `e4-temp`

- Config File: [e4-temp.yaml](../configs/dataset/stream/e4-temp.yaml)
- Sensor
  - Device: [Empatica E4](https://www.empatica.com/en-int/research/e4/)
  - Sensor Type: Temperature
  - Frame Rate: 4 Hz

### 5-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/e4/${device}/temp/${session}.csv
```

### 5-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype | Note |
| --- | ----------- | ------------ | ----- | ---- |
| 0   | time        | milli second |       |      |
| 1   | temp        | microsiemens |       |      |

## [6] `kinect-2d-kpt`

- Config File: [kinect-2d-kpt.yaml](../configs/dataset/stream/kinect-2d-kpt.yaml)
- Sensor
  - Device: [Azure Kinect DK](https://azure.microsoft.com/ja-jp/products/kinect-dk/)
  - Sensor Type: keypoint/2d
  - Frame Rate: 15 Hz
  - 3D Pose Estimation: [mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2](https://github.com/open-mmlab/mmpose/blob/master/configs/body/2d_kpt_sview_rgb_vid/posewarper/posetrack18/hrnet_w48_posetrack18_384x288_posewarper_stage2.py)

### 6-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/kinect/2d-kpt/mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2/single/${session}.json
```

### 6-2: File Format (`json`)

| #   | Column Name               | Unit          | Dtype                             | Note                                      |
| --- | ------------------------- | ------------- | --------------------------------- | ----------------------------------------- |
| 0   | info                      | None          | dict                              |                                           |
| 1   | licences                  | None          | list[dict]                        |                                           |
| 2   | annotations               | None          | list[dict]                        |                                           |
| 3   | annotations/id            | None          | int                               |                                           |
| 4   | annotations/image_id      | milli seconds | int                               | UNIXtime with milli seconds precision     |
| 5   | annotations/category_id   | None          | int                               |                                           |
| 6   | annotations/area          | None          | float                             |                                           |
| 7   | annotations/bbox          | None          | Tuple[float, float, float, float] | [x, y, width, height]                     |
| 8   | annotations/iscrowd       | None          | int                               | iscrowd = 0                               |
| 9   | annotations/keypoints     | px            | list[float]                       | [x1, y1, v1, ...] (v? = confidence score) |
| 10  | annotations/num_keypoints | None          | int                               |                                           |
| 11  | annotations/bbox_score    | None          | float                             | confidence score for the bounding box     |
| 12  | annotations/track_id      | None          | int                               |                                           |
| 13  | category                  | None          | list                              |                                           |

## [7] `kinect-3d-kpt`

- Config File: [kinect-3d-kpt.yaml](../configs/dataset/stream/kinect-3d-kpt.yaml)
- Sensor
  - Device: [Azure Kinect DK](https://azure.microsoft.com/ja-jp/products/kinect-dk/)
  - Sensor Type: keypoint/3d
  - Frame Rate: 15 Hz
  - 3D Pose Estimation: [k4abt](https://learn.microsoft.com/ja-jp/azure/kinect-dk/build-first-body-app)

### 7-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/kinect/3d-kpt/k4abt/${preprocessing}/${session}.json
```

### 7-2: File Format (`json`)

| #   | Column Name               | Unit          | Dtype                             | Note                                      |
| --- | ------------------------- | ------------- | --------------------------------- | ----------------------------------------- |
| 0   | info                      | None          | dict                              |                                           |
| 1   | licences                  | None          | list[dict]                        |                                           |
| 2   | annotations               | None          | list[dict]                        |                                           |
| 3   | annotations/id            | None          | int                               |                                           |
| 4   | annotations/image_id      | milli seconds | int                               | UNIXtime with milli seconds precision     |
| 5   | annotations/category_id   | None          | int                               |                                           |
| 6   | annotations/area          | None          | float                             |                                           |
| 7   | annotations/bbox          | None          | Tuple[float, float, float, float] | [x, y, width, height]                     |
| 8   | annotations/iscrowd       | None          | int                               | iscrowd = 0                               |
| 9   | annotations/keypoints     | px            | list[float]                       | [x1, y1, v1, ...] (v? = confidence score) |
| 10  | annotations/num_keypoints | None          | int                               |                                           |
| 11  | annotations/bbox_score    | None          | float                             | confidence score for the bounding box     |
| 12  | annotations/track_id      | None          | int                               |                                           |
| 13  | category                  | None          | list                              |                                           |

## [8] `kinect-depth`

- Config File: [kinect-depth.yaml](../configs/dataset/stream/kinect-depth.yaml)
- Sensor
  - Device: [Azure Kinect DK](https://azure.microsoft.com/ja-jp/products/kinect-dk/)
  - Sensor Type: depth/16bit-png (front-view)
  - Frame Rate: 15 Hz
  - Preprocessing:
    - Coordinate Transoformation: [k4a_transformation_depth_image_to_color_camera()](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/group___functions_gafacffb5f781a9c2df30d4a16241cd514.html)

### 8-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/kinect/depth/frames/${session}
```

### 8-2: File Format (`16bit Grayscal PNG`)

## [9] `rs02-depth`

- Config File: [rs02-depth.yaml](../configs/dataset/stream/rs02-depth.yaml)
- Sensor
  - Device: [Realsense](https://www.intel.com/content/www/us/en/products/sku/190004/intel-realsense-depth-camera-d435i/specifications.html)
  - Sensor Type: depth/16bit-png (top-view)
  - Frame Rate: 15 Hz

### 9-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/rs02/depth/frames/${session}
```

### 9-2: File Format (`16bit Grayscal PNG`)

## [10] `lidar-depth`

- Config File: [lidar-depth.yaml](../configs/dataset/stream/lidar-depth.yaml)
- Sensor
  - Device: [ULTRA PUCK(VLP-32C)-Veloidne](https://velodynelidar.com/products/ultra-puck/)
  - Sensor Type: lidar/point-cloud (front-view)

### 10-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/lidar/frames/${session}
```

### 10-2: File Format (`Point Cloud`)

## [11] `system-ht-original`

- Config File: [system-ht-original.yaml](../configs/dataset/stream/system-ht-original.yaml)
- Sensor
  - Device: [8001-C Portable Terminal](https://shop.e-welcom.com/shop/g/g8001C-02/)
  - Sensor Type: IoT/handheld-scanner

### 11-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/system/ht/${session}.csv
```

### 11-2: File Format (`csv`)

| #   | Column Name | Unit         | Dtype            | Note |
| --- | ----------- | ------------ | ---------------- | ---- |
| 0   | unixtime    | milli second | int              |      |
| 1   | datetime    | None         | str (ISO format) |      |
| 2   | order_sheet | None         | str              |      |
| 3   | box         | None         | str              |      |
| 4   | item        | None         | str              |      |

## [12] `system-order-sheet`

- Config File: [system-order-sheet.yaml](../configs/dataset/stream/system-order-sheet.yaml)
- Sensor
  - Data Type: system/order-sheet

### 12-1: Path

```txt
${path.openpack.rootdir}/${user.name}/system/order-sheet//${session}.csv
```

### 12-2: File Format (`csv`)

| #   | Column Name  | Unit | Dtype | Note                                     |
| --- | ------------ | ---- | ----- | ---------------------------------------- |
| 0   | sheet_no     | None | str   | format = DEN{session_no:0=4}{box_no:0=2} |
| 1   | session      | None | str   |                                          |
| 2   | box          | None | str   |                                          |
| 3   | pattern      | None | str   |                                          |
| 4   | total_amount | None | str   |                                          |
| 5   | item1        | None | str   |                                          |
| 6   | item2        | None | str   |                                          |
| 7   | item3        | None | str   |                                          |
| 8   | item4        | None | str   |                                          |
| 9   | item5        | None | str   |                                          |
| 10  | amount1      | None | str   |                                          |
| 11  | amount2      | None | str   |                                          |
| 12  | amount3      | None | str   |                                          |
| 13  | amount4      | None | str   |                                          |
| 14  | amount5      | None | str   |                                          |

## [13] `system-printer`

- Config File: [system-printer.yaml](../configs/dataset/stream/system-printer.yaml)
- Sensor
  - Device: [QL-820NWB](https://www.brother.co.jp/product/labelprinter/ql820nwb/index.aspx) (pesudo log data)
  - Data Type: IoT/printer/pseudo-data

### 13-1: Relative Path

```txt
${path.openpack.rootdir}/${user.name}/system/printer/${session}.csv
```

### 13-1: File Format (`csv`)

| #   | Column Name | Unit         | Dtype            | Note |
| --- | ----------- | ------------ | ---------------- | ---- |
| 0   | unixtime    | milli second | int              |      |
| 1   | datetime    | None         | str (ISO format) |      |
| 2   | order_sheet | None         | str              |      |
