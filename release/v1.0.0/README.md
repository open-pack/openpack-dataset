# Release Note: OpenPack Dataset (v1.0.0)

## Overview

This is the first full dataset release of the OpenPack dataset.
From previous version (v0.3.1), new data streams and annotations are added.
We also received comments about the file structure. Starting with this version, for each user, all data for that user will be combined into one zip file.
Thank you for your comments. We hope this will improve usability very much.

## Major Changes :rocket:

- The following new data stream are added.
  - kinect/3d-kpt/none
  - kinect/3d-kpt/single-ffill-flip-fixed
  - kinect/color-masked/frames
- The following annotation data is added.
  - annotation/openpack-actions
  - annotation/openpack-actions-1hz
  - annotation/openpack-operations
  - annotation/openpack-outliers
- Annotation data `activity-1s` in `v0.3.1` is split into `openpack-actions-1hz` and `openpack-operation-1hz`. In addition, several annotation errors have been corrected for existing data.
- The data of the following users, which was not made available before, is now available to the public.
  - U0104 (annotation)
  - U0108 (annotation)
  - U0110 (annotation)
  - U0201
  - U0203 (annotation)
  - U0204 (annotation)
  - U0206
  - U0207 (annotation)
  - U0208
  - U0209

## Download

### Download from Zenodo

Data except images is available in [zenodo (DOI: 10.5281/zenodo.8145223)](https://zenodo.org/records/8145223).
Go to this page and download the files one by one.

Alternatively, you can use [this command](./release/v1.0.0/download_from_zenodo.sh) to download and extract the all files at the same time.

```bash
bash ./download_from_zenodo.sh <PATH TO YOUR DATASET ROOT DIRECTORY>

# Example:
bash ./download_from_zenodo.sh ../../../data/datasets
```

The data on the zenodo is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Donwload from Google Drive

Dataset including depth images is available at [this Google Drive folder](https://drive.google.com/drive/folders/10hYJYkhPRgf-uTToUm5KR99EHkH2v9GB?usp=drive_link).
Inside this folder you will find one zip file for each subject. Please download them manually one by one.

The data in this Google Drive folder is distributed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.

### Download from Google Drive (RGB)

For some subjects, RGB images can also be available.
However, RGB images are distributed under [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md).
The usage of this dataset is limited to the academic research ONLY, any direct or indirect commercial use is NOT allowed.

You must first apply through ["OpenPack Dataset - Access Request Form"](https://docs.google.com/forms/d/e/1FAIpQLScrRWe-qTQV5CKTBxtLQZ7ScgLsHFWxXRmD5he04qXRVBAtqg/viewform?usp=sf_link) and we will confirm your qualification.
Once approved, we will share the data with Read Only access to your google account.
