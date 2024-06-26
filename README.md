# OpenPack Dataset

[![Static Badge](<https://img.shields.io/badge/Paper-IEEE_(PerCom2024)-blue?style=flat>)](https://ieeexplore.ieee.org/abstract/document/10494448)
[![Static Badge](https://img.shields.io/badge/Paper-arXiv:3A3A2212.11152-red?style=flat)](https://arxiv.org/abs/2212.11152)
[![Static Badge](https://img.shields.io/badge/Project-OpenPack_Dataset_Web-lightbrown?style=flat&labelColor=716140&color=eaddcf)](https://open-pack.github.io/)
[![Static Badge](https://img.shields.io/badge/Latest_Release-v1.0.0-lightbrown?style=flat)](https://github.com/open-pack/openpack-dataset/tree/main/release/v1.0.0)

[OpenPack Dataset](https://open-pack.github.io/) is a new large-scale multi-modal dataset of packing processes.
This repository provides download instructions and technical details for the OpenPack Dataset.

![OpenPack Dataset Log](./assets/dataset/OpenPackDataset-black.png)

## What is OpenPack dataset?

OpenPack is an open access logistics-dataset for human activity recognition, which contains 53 hours of human movement data with 20,129 instances of work operation annotation.
In addition, OpenPack dataset contains data from IoT-enabled devices and rich metadata such as error annotation and order information.

This repo focuses on technical documentation.
For more information, including dataset features and visual samples, please visit [OpenPack Dataset Official Web](https://open-pack.github.io/).

![OpenPack__KeyVisual](./assets/dataset/OpenPack__KeyVisual.png)

### Latest Release

[Release Note - OpenPack (v1.0.0)](./release/v1.0.0/)

### Citation

When using the dataset, kindly reference:

> N. Yoshimura, J. Morales, T. Maekawa and T. Hara, "[OpenPack: A Large-Scale Dataset for Recognizing Packaging Works in IoT-Enabled Logistic Environments](https://ieeexplore.ieee.org/abstract/document/10494448)," 2024 IEEE International Conference on Pervasive Computing and Communications (PerCom), Biarritz, France, 2024

```text
@INPROCEEDINGS{10494448,
  author={Yoshimura, Naoya and Morales, Jaime and Maekawa, Takuya and Hara, Takahiro},
  booktitle={2024 IEEE International Conference on Pervasive Computing and Communications (PerCom)},
  title={OpenPack: A Large-Scale Dataset for Recognizing Packaging Works in IoT-Enabled Logistic Environments},
  year={2024},
  volume={},
  number={},
  pages={90-97},
  doi={10.1109/PerCom59722.2024.10494448}}
```

## Documentation

Technical information on this dataset is available under [docs](./docs/) folder.

- [OpenPack Dataset - Documentation](./docs/)
  - [Data Collection](./docs/data-collection/)
    - [Subjects](./docs/data-collection/subjects.md)
    - [Recording Sessions](./docs/data-collection/sessions.md)
    - [Recording Environment & Sensor Coordinates](./docs/data-collection/environment.md)
  - [Data Stream (Sensor Data Types and File Format)](./docs/data-stream/)
    - [Wearable Sensors](./docs/data-stream/wearables.md)
    - [Vision Modalities](./docs/data-stream/vision.md)
    - [IoT Device](./docs/data-stream/iot.md)
    - [Metadata](./docs/data-stream/metadata.md)
  - [Annotation](./docs/annotation/)
    - [Activity Class Definition](./docs/annotation/activity-class.md)
  - [Benchmark](./docs/benchmark/)
    - [Data Split](./docs/benchmark/data-split.md)
  - [Download](./docs/DOWNLOAD.md)
  - [Tutorial](./docs/tutorials/)
    - [Load IMU Sensor Data with Operation Labels](./docs/tutorials/load-imu-with-operation-labels.md)

## Download

### Full Dataset

OpenPack datasets are available in 3 repositories.
Please refer to [DOWNLOAD.md](./docs/DOWNLOAD.md) for the differences between each repository and how to download.

As a quick start guide, here is how to download datasets from zenodo to `./data/datasets`.
You can download all the data from zenodo using [this shell script](./release/v1.0.0/download_from_zenodo.sh). Please run the following commands in your `bash`.
Note that datasets from zenodo do not include depth images, etc.

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

### Preprocessed Dataset

Sensors used in the OpenPack dataset have different sampling rates.
Therefore, each sensor is stored in a separate file. When you use them, you have to combine them using timestamps associated with each record. But we understand that it's not easy for the newcomer.

Therefore, we prepared a pre-processed dataset for the quick trial.
IMU data from 4 sensors and work operation labels are combined into one CSV file.
This pre-processd dataset is available on [zenodo (preprocessed-IMU-with-operation-labels.zip)](https://zenodo.org/records/8145223).

For more details, see [data-stream/preprocessed](./docs/data-stream/preprocessed.md).

### Sample Data

Sample data including RGB images is available in [./data/openpack/](./data/openpack/).
You can use these files to check contents and file formats before downloading the full dataset.

## Tools & Ecosystem

OpenPack offers a variety of tools, including data loading tools and a benchmark pipeline implementation.
Below are links to the available tools.

- [OpenPack Dataset - Official Web](https://open-pack.github.io/)
  - Visual information about the OpenPack dataset.
  - Results of OpenPack Challenge 2022 (@PerCom 2023 WS BiRD)
- [OpenPack Dataset Toolkit (GitHub: openpack-toolkit)](https://github.com/open-pack/openpack-toolkit)
  - Utility to load and transform the OpenPack dataset.
  - It provides functions and snippets for combining sensor data with different sampling rates and ground truth in Python.
  - A sample notebook to visualize the dataset is available.
- [OpenPack Dataset PyTorch Utilities (GitHub: openpack-torch)](https://github.com/open-pack/openpack-torch)
  - PyTorch utilities to work around with OpenPack Dataset.
  - It provides implementations of baseline models such as U-Net, DeepConvLSTM.
  - A pipeline for benchmarking (model training and testing) is implemented with [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning).
  - Tutorial notebooks for U-Net and DeepConvLSTM are available.
- [YouTube: OpenPack Dataset](https://youtube.com/@openpackdataset6864?si=2VemMXqnXexe_f-4)
  - Samples of depth recordings and a tutorial session for OpenPack Challenge 2022 are available.
  - The video of the tutorial session is Japanese, but the English subtitles are available.

## Papers

### Dataset (Citation)

- N. Yoshimura, J. Morales, T. Maekawa and T. Hara, "OpenPack: A Large-Scale Dataset for Recognizing Packaging Works in IoT-Enabled Logistic Environments," 2024 IEEE International Conference on Pervasive Computing and Communications (PerCom), Biarritz, France, 2024 ([link](https://ieeexplore.ieee.org/abstract/document/10494448))

### Related Research

- Q. Xia, T. Maekawa, J. Morales, T. Hara, H. Oshima, M. Fukuda, Y. Namioka, "Preliminary investigation of SSL for Complex Work Activity Recognition in Industrial Domain via MoIL", 2024 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops), Biarritz, France, 2024 (Best WIP Award)

## Contact

If you have any questions about OpenPack dataset, please post them to [Issues](https://github.com/open-pack/openpack-dataset/issues) and assign them to Naoya Yoshimura ([@getty708](https://github.com/getty708)) or Jaime Morales ([@MorJaime](https://github.com/MorJaime)).
We will be happy to help you.

## Acknowledgment

This work is partially supported by JSPS KAKENHI JP21H03428, JP21H05299, JP21J10059, JST ACT-X JPMJAX200T.
We greatly appreciate Chikako Kawabe, Kana Yasuda, and Makiko Otsuka for their efforts in developing the OpenPack dataset.

## License

[OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
However, [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md) is applied to "OpenPack Dataset (+RGB)" which includes RGB data.
