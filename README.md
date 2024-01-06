# OpenPack Dataset

[OpenPack Dataset](https://open-pack.github.io/) is a new large-scale multi-modal dataset of packing processes.
This repository provides download instruction and technical details for the OpenPack Dataset.

## Contents

- [Contents](#contents)
- [What is OpenPack dataset?](#what-is-openpack-dataset)
- [Documentation](#documentation)
- [Download](#download)
- [Tools \& Ecosystem](#tools--ecosystem)
- [Contact](#contact)
- [Acknowledgement](#acknowledgement)
- [License](#license)

## What is OpenPack dataset?

OpenPack is an open access logistics-dataset for human activity recognition, which contains 53 hours of human movement data with 20,129 instances of work operation annotation.
In addition, OpenPack dataset contains data from IoT-enabled devices and rich metadata such as error annotation and order information.

This repo focuses on technical documentation.
For more information, including dataset features and visual samples, please visit [OpenPack Dataset Official Web](https://open-pack.github.io/).

![OpenPack__KeyVisual](./assets/dataset/OpenPack__KeyVisual.png)

## Documentation

Detail infomrmation of this dataset is available under [docs/](./docs) folder.

- [OpenPack Dataset - Documentation](./docs/README.md)
  - [Reocrding Sessions](./docs/SESSIONS.md)
  - Data
    - [Sensor Modality (Data Stream)](./docs/DATA_STREAM.md)
    - [Subjects-related Metadata](./docs/SUBJECTS.md)
    - [System Metadata](./docs/METADATA.md)
  - Annotation
    - [Activity Class Definition](./docs/ANNOTATION.md)
  - Benchmark
    - [Data Split](./docs/DATA_SPLIT.md)

## Download

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

## Tools & Ecosystem

OpenPack offers a variety of tools, including data loading tools and a benchmark pipeline implementation.
Below are links to the available tools.

- [OpenPack Dataset - Official Web](https://open-pack.github.io/)
  - Visual information about the OpenPack dataset.
  - Results of OpenPack Challenge 2022 (@PerCom 2023 WS BiRD)
- [OpenPack Dataset Toolkit (GitHub: openpack-toolkit)](https://github.com/open-pack/openpack-toolkit)
  - Utility to load and transoform the OpenPack dataset.
  - It provides functions and snippets for combining sensor data with different sampling rates and ground truth in Python.
  - A sample notebook to visualize dataset is available.
- [OpenPack Dataset PyTorch Utilities (GitHub: openpack-torch)](https://github.com/open-pack/openpack-torch)
  - PyTorch utilities to work around with OpenPack Dataset.
  - It provides implementations of baseline models sich as U-Net, DeepConvLSTM.
  - A pipeline for benchmarking (model training and testing) is implemented with [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning).
  - Tutorial notebooks for U-Net and DeepConvLSTM are available.
- [YouTube: OpenPack Dataset](https://youtube.com/@openpackdataset6864?si=2VemMXqnXexe_f-4)
  - Samples of depth recordings and tutorial session for OpenPack Challenge 2022 are available.

## Contact

If you have any question about OpenPack dataset, please post them to [Issues](https://github.com/open-pack/openpack-dataset/issues) and assign them to Naoya Yoshimura ([@getty708](https://github.com/getty708)) or Jaime Morales ([@MorJaime](https://github.com/MorJaime)).
We will be happy to help you.

## Acknowledgement

This work is partially supported by JSPS KAKENHI JP21H03428, JP21H05299, JP21J10059, JST ACT-X JPMJAX200T.
We greatly appreciate Chikako Kawabe, Kana Yasuda, and Makiko Otsuka for their efforts in developing the OpenPack dataset.


## License

[OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
However, [OpenPack Dataset (+RGB) License](./licenses/OPENPACK_DATASET_RGB_LICENSE.md) is applied to "OpenPack Dataset (+RGB)" which includs RGB data.
