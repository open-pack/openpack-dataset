# Download

## Table of Contents

- [Download](#download)
  - [Table of Contents](#table-of-contents)
  - [Data Repositories](#data-repositories)
  - [How to download the latest OpenPack dataset?](#how-to-download-the-latest-openpack-dataset)
    - [Sample Data on GitHub](#sample-data-on-github)
    - [Download from Zenodo](#download-from-zenodo)
    - [Donwload from Google Drive](#donwload-from-google-drive)
    - [Download from Google Drive (RGB)](#download-from-google-drive-rgb)
  - [How to check the downloaded files?](#how-to-check-the-downloaded-files)
  - [File Structure](#file-structure)

## Data Repositories

OpenPack dataset is available in 3 repositories.
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

### Sample Data on GitHub

Sample data for U0209 (Session 5) is available [here](../data/openpack/).

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

The dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/10hYJYkhPRgf-uTToUm5KR99EHkH2v9GB?usp=drive_link).
Inside this folder, you will find one zip file for each subject. Please download them manually one by one.

The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Download from Google Drive (RGB)

For some subjects, RGB images can also be available.
However, RGB images are distributed under [OpenPack Dataset (+RGB) License](https://github.com/open-pack/openpack-dataset/blob/main/licenses/OPENPACK_DATASET_RGB_LICENSE.md).
The usage of this dataset is limited to academic research ONLY, any direct or indirect commercial use is NOT allowed.

You must first apply through ["OpenPack Dataset - Access Request Form"](https://docs.google.com/forms/d/e/1FAIpQLScrRWe-qTQV5CKTBxtLQZ7ScgLsHFWxXRmD5he04qXRVBAtqg/viewform?usp=sf_link) and we will confirm your qualification.
Once approved, we will share the data with Read Only access to your Google account.

## How to check the downloaded files?

A file index of the OpenPack dataset is available in [release/v1.0.0/)](../release/v1.0.0/).
By comparing this file index with your dataset folder, you can confirm that all data is correctly downloaded and placed in the correct place.
In [openpack-toolkit](https://github.com/open-pack/openpack-toolkit), there is a tool to automatically check the downloaded files with the file index on the GitHub.
Use this command to check your dataset directory. (Requirements: `Python>=3.9`)

```bash
#!/bin/bash
pip install openpack-toolkit
optk-file check -r ./data/datasets/openpack/
```

If there are any missing files, a list of them are shown in your terminal.
Also, the scan results are saved in `file_index_OpenPack_v1.0.0_zenodo.csv`, and if a file exists, True is marked in the `file_exists` column. Here is an example of the output.

| path                                            | size      | is_dir | file_exists |
| ----------------------------------------------- | --------- | ------ | ----------- |
| U0101/annotation/openpack-actions-1hz/S0100.csv | 382.24 KB | False  | True        |
| U0101/annotation/openpack-actions-1hz/S0200.csv | 312.42 KB | False  | True        |
| U0101/annotation/openpack-actions-1hz/S0300.csv | 312.67 KB | False  | True        |
| U0101/annotation/openpack-actions-1hz/S0400.csv | 333.41 KB | False  | True        |
| U0101/annotation/openpack-actions-1hz/S0500.csv | 298.35 KB | False  | True        |

## File Structure

Data are stored in separate files for each modality and each session.
This is because the OpenPack is a multimodal dataset and each sensor has different sampling rate.

The basic path structure is as follows.
In each folder corresponding to a subject (e.g., U0101), there are subfolders for each sensor (e.g., annotation, atr).
In the lower level, you can find subfolders for the sensor modalities.
Sensor data for each session is stored in the subfolder in text format (e.g., CSV, JSON).
Therefore, data files must be concatenated when they are used. How to combine data in the separate files is explained in [tutorials](./tutorials/load-imu-with-operation-labels.md).

```text
${path.openpack.rootdir}/${user}/${sensor}[/${device}][/${method}]/${session}
```

Here is a sample of the standard file structure of the OpenPack dataset.

```text
openpack/
└── v1.0.0
    ├── U0101
    │   ├── annotation
    │   │   ├── openpack-actions
    │   │   │   ├── S0100.csv
    │   │   │   ├── S0200.csv
    │   │   │   ├── S0300.csv
    │   │   │   ├── S0400.csv
    │   │   │   └── S0500.csv
    │   │   ├── openpack-operations
    │   │   ├── openpack-outliers
    │   │   └── ...
    │   ├── atr
    │   │   ├── atr01
    │   │   │   ├── S0100.csv
    │   │   │   └── ...
    │   │   ├── atr02
    │   │   ├── atr03
    │   │   └── atr04
    │   ├── ...
    ├── U0102
    ├── ...
```
