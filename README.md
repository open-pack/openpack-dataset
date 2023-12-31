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

Please follow the instructions below for downloading **OpenPack datasets (v1.0.0)** from each repository.

### Zenodo

Data except images is available in [zenodo](https://zenodo.org/records/8145223).
Go to the following page and download the files one by one.

- Zenodo: [OpenPack: Public multi-modal dataset for packaging work recognition in logistics domain (DOI: 10.5281/zenodo.8145223)](https://zenodo.org/records/8145223)

Alternatively, you can use this command to download and extract the all files at the same time.
(Ref: [Download Shell Script](./release/v1.0.0/download_from_zenodo.sh))

```bash
bash ./release/v1.0.0/download_from_zenodo.sh <PATH TO YOUR DATASET ROOT DIRECTORY>

# Example:
bash ./release/v1.0.0/download_from_zenodo.sh ../data/datasets
```

The data on the zenodo is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Google Drive

Dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/10hYJYkhPRgf-uTToUm5KR99EHkH2v9GB?usp=drive_link).
Inside this folder you will find one zip file for each subject. Please download them manually one by one.

The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Google Drive (RGB)

For some subjects, RGB images can also be available.
However, RGB images are distributed under [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md).
The usage of this dataset is limited to the academic research ONLY, any direct or indirect commercial use is NOT allowed.

You must first apply through Google Form below and we will confirm your qualification.
Once approved, we will share the data with Read Only access to your google account.

- [OpenPack Dataset - Access Request Form](https://docs.google.com/forms/d/e/1FAIpQLScrRWe-qTQV5CKTBxtLQZ7ScgLsHFWxXRmD5he04qXRVBAtqg/viewform?usp=sf_link)

## License

[OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
However, [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md) is applied to "OpenPack Dataset (+RGB)" which includs RGB data.
