# OpenPack Dataset

[OpenPack Dataset](https://open-pack.github.io/) is a new large-scale multi-modal dataset of packing processes.
This repository provides download instruction and technical details for the OpenPack Dataset.

## Contents

- [What is OpenPack dataset?](#what-is-openpack-dataset)
- [Download](#download)

## What is OpenPack dataset?

OpenPack is an open access logistics-dataset for human activity recognition, which contains 53 hours of human movement data with 20,129 instances of work operation annotation.
In addition, OpenPack dataset contains data from IoT-enabled devices and rich metadata such as error annotation and order information.

![OpenPack__KeyVisual](./assets/dataset/OpenPack__KeyVisual.png)

### Large Scale activity dataset in Industrial Domain

OpenPack is the first large-scale dataset for packaging work recognition.
16 distinct subjects packed 3956 items in 2048 shipping boxes in total and the total recording length is more than 53 hours.
The work operations and actions were annotated by the professional annotators.
The total number of annotated work operations and actions are 20,129 and 52,529 respectively.

### Rich Modalities - Vision + Wearable + IoT Device

OpenPack provides 9 data modalities including acceleration, gyroscope, quaternion, blood volume pulse (BVP), and electrodermal activity (EDA) data, as well as keypoints, a LiDAR point cloud, and depth images.
As for the wearable sensor modality, we collected data with 4 IMUs and 2 E4 sensors.
For the vision modality, 2 depth cameras (front view and top view) and 1 LiDAR sensor were installed to our environment.
In addition, we collected data from IoT devices which are sparse but have strong relation with specific activity classes.

### Rich Meta Data

OpenPack also provides a rich set of metadata such as subject’s experience in packaging work and physical traits of subjects, enabling designs of various research tasks such as assessment of worker’s performance in addition to basic work activity recognition.
In addition, we made a list of irregular activities which can be used for developing normal detection technologies.

## Data Repository

OpenPack dataset is available in 3 repository.
Different repositories provide different sets of data with different licenses.
Please refer to the table below to select the repository best fit for your requirements.
Instructions for downloading each dataset are provided in the next section.

| -                       | GitHub (openpack-dataset) | Zenodo          | Google Drive    | Google Drive (RGB)              |
| ----------------------- | ------------------------- | --------------- | --------------- | ------------------------------- |
| **Modality (Wearable)** |                           |                 |                 |                                 |
| Acceleration            | x                         | o               | o               | x                               |
| Gyroscope               | x                         | o               | o               | x                               |
| Orientation             | x                         | o               | o               | x                               |
| EDA                     | x                         | o               | o               | x                               |
| BVP                     | x                         | o               | o               | x                               |
| Temperature             | x                         | o               | o               | x                               |
|                         |                           |                 |                 |                                 |
| **Modality (Vision)**   |                           |                 |                 |                                 |
| Keypoints               | x                         | o               | o               | x                               |
| Depth (PNG)             | x                         | x               | o               | x                               |
| Depth (LiDAR)           | x                         | x               | o               | x                               |
| RGB Images              | x                         | x               | x               | o                               |
|                         |                           |                 |                 |                                 |
| **Modality (Others)**   |                           |                 |                 |                                 |
| IoT Device              | x                         | o               | o               | x                               |
| Meta Data               | x                         | o               | o               | x                               |
| Annotation              | x                         | o               | o               | x                               |
|                         |                           |                 |                 |                                 |
| **License**             | CC BY-NC-SA 4.0           | CC BY-NC-SA 4.0 | CC BY-NC-SA 4.0 | OpenPack Dataset (+RGB) License |

## Download

TBA

## License

[OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
However, [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md) is applied to "OpenPack Dataset (+RGB)" which includs RGB data.
