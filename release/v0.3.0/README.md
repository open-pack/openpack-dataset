# Release Note: OpenPack Dataset (v0.3.0)

## Overview

This release is prepared for OpenPack Challenge 2022 which launches on 15th Oct. This dataset contains data from 17 subjects. Data from vision modalities, i.e., depth images and LiDAR data are newly included in this release.

## Major Changes :rocket:

- Add data from 11 subjects.
  - New Subjects: U0101, U0104, U0108*, U0109, U0110, U0202, U0203*, U0204*, U0205, U0207*, U0210,
  - Subjects with “\*” are test subjects. Therefore annotation data is excluded.
- Add depth images and LiDAR data.
- Add metadata (item list).
- Update annotation data.
  - Action labels are updated into v3 (more detailed annotations).
  - Some subjects TBA are still in progress.

## Download

### Download from Zenodo

Available at [Zenodo (DOI: 10.5281/zenodo.7139262)](https://zenodo.org/records/7139262).

You can download the dataset with the following command.

```shell
# Download IMU data, Annotation, etc
pip install openpack-toolkit==0.7.0
optk-download -d ../data/datasets -v v0.3.0 -s atr-qags,openpack-operations
```

### Donwload from Google Drive

Dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/1RwZcB6jtdemHUQszqhbO0fuKutBazhux?usp=drive_link).
The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

## Note

- The following data is under development. Please wait for the next release.
  - printer log.
  - depth images of top view (realsense) ... Current data format is "8bit RGB PNG". We are preparing to replace them with "16bit PNG" in the future.
