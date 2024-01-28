# Release Note: OpenPack Dataset (v0.3.0)

## Overview

This release is prepared for OpenPack Challenge 2022 which launches on 15th Oct. This dataset contains data from 17 subjects. Data from vision modalities, i.e., depth images and LiDAR data are newly included in this release.

## Minor Changes :bug:

- Update annotation data for U0109.
- Update pseudo printer log data.

## Download

### Tutorial Dataset (Updated: 2023-03-29)

In the Full Dataset, the data and label files are published in separate files, and we received many comments that it was difficult to combine them.
Therefore, for tutorial purposes, we have created a CSV file containing the four IMU sensor data and the work operation labels.
Before downloading the Full Dataset, please check the contents of the data in this CSV.

Please access Google Drive from the following URL and download the file.
Labels have been slightly changed from those on zenodo (v0.3.1) to correct annotation errors. Please be aware of this.
We plan to integrate the data distribution location into zenodo in the next release.

- Tutorial (ATR & Operation Label)
  - [Google Drive - Sample - Tutorial CSV](https://drive.google.com/drive/folders/1znwBUlT0fKErkJUgp-ak0MI_vi_84RYz?usp=sharing).

### Download from Zenodo

Available at [Zenodo (DOI: 10.5281/zenodo.7213887)](https://zenodo.org/records/7213887).

You can download the dataset with the following command.

```shell
# Download IMU data, Annotation, etc
pip install openpack-toolkit==0.7.0
optk-download -d ../data/datasets -v v0.3.1 -s atr-qags,openpack-operations
```

### Donwload from Google Drive

Dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/1RwZcB6jtdemHUQszqhbO0fuKutBazhux?usp=drive_link).
The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
