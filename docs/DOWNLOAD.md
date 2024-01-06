# Download

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Data Repositories](#data-repositories)
- [How to download the latest OpenPack dataset?](#how-to-download-the-latest-openpack-dataset)
  - [Download from Zenodo](#download-from-zenodo)
  - [Donwload from Google Drive](#donwload-from-google-drive)
  - [Download from Google Drive (RGB)](#download-from-google-drive-rgb)

## Data Repositories

OpenPack dataset is available in 3 repository.
Different repositories provide different sets of data with different licenses.
Please refer to the table below to select the repository best fit for your requirements.
Instructions for downloading each dataset come after this table.

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
| Meta Data               | o                         | o               | o               | x                               |
| Annotation              | x                         | o               | o               | x                               |
|                         |                           |                 |                 |                                 |
| **License**             | CC BY-NC-SA 4.0           | CC BY-NC-SA 4.0 | CC BY-NC-SA 4.0 | OpenPack Dataset (+RGB) License |

## How to download the latest OpenPack dataset?

Here we explain how to download the latest OpenPack dataset (v1.0.0).

### Download from Zenodo

Data except images is available in [zenodo (DOI: 10.5281/zenodo.8145223)](https://zenodo.org/records/8145223).
Go to this page and download the files one by one.

Alternatively, you can use [this shell script](https://github.com/open-pack/openpack-dataset/blob/main/release/v1.0.0/download_from_zenodo.sh) to download and extract the all files at the same time.

```bash
#!/bin/bash
# Get a download script.
$ curl -o download_from_zenodo.sh https://raw.githubusercontent.com/open-pack/openpack-dataset/main/release/v1.0.0/download_from_zenodo.sh

# Create dataset root directory. (Please change this path if necessary)
$ export DATASET_ROOTDIR_PATH=./data/datasets
$ mkdir -p $DATASET_ROOTDIR_PATH

# Download the dataset. (It takes time to complete. Please wait with patience...)
$ bash download_from_zenodo.sh $DATASET_ROOTDIR_PATH
```

The data on the zenodo is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Donwload from Google Drive

Dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/10hYJYkhPRgf-uTToUm5KR99EHkH2v9GB?usp=drive_link).
Inside this folder you will find one zip file for each subject. Please download them manually one by one.

The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Download from Google Drive (RGB)

For some subjects, RGB images can also be available.
However, RGB images are distributed under [OpenPack Dataset (+RGB) License](https://github.com/open-pack/openpack-dataset/blob/main/licenses/OPENPACK_DATASET_RGB_LICENSE.md).
The usage of this dataset is limited to the academic research ONLY, any direct or indirect commercial use is NOT allowed.

You must first apply through ["OpenPack Dataset - Access Request Form"](https://docs.google.com/forms/d/e/1FAIpQLScrRWe-qTQV5CKTBxtLQZ7ScgLsHFWxXRmD5he04qXRVBAtqg/viewform?usp=sf_link) and we will confirm your qualification.
Once approved, we will share the data with Read Only access to your google account.
