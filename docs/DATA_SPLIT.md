# Recommended Data Split

## Table of Contents

- [Recommended Data Split](#recommended-data-split)
  - [Table of Contents](#table-of-contents)
  - [Debug Split](#debug-split)
  - [Pilot Challenge Split](#pilot-challenge-split)
  - [Openpack Challenge 2022 Split](#openpack-challenge-2022-split)

## Debug Split

This split is for debugging.
You can test your pipeline with the minimum amount of data.

- Config File: [debug.yaml](https://github.com/open-pack/openpack-toolkit/blob/main/configs/dataset/split/debug.yaml)
- Python Class: [`openpack_toolkit.configs.datasets.splits.DEBUG_SPLIT`](https://github.com/open-pack/openpack-toolkit/blob/main/openpack_toolkit/configs/datasets/splits.py)

| #   | Usage      | User  | Session |
| --- | ---------- | ----- | ------- |
| 1   | TRAIN      | U0102 | S0100   |
| 2   | TRAIN      | U0102 | S0200   |
| 3   | TRAIN      | U0102 | S0300   |
|     |            |       |         |
| 1   | VAL        | U0102 | S0400   |
|     |            |       |         |
| 1   | TEST       | U0102 | S0500   |
|     |            |       |         |
| 1   | SUBMISSION | U0102 | S0500   |

## Pilot Challenge Split

This split is for OpenPack Pilot Challenge (private competition).

- Config File: [pilot-challenge.yaml](https://github.com/open-pack/openpack-toolkit/blob/main/configs/dataset/split/pilot-challenge.yaml)
- Python Class: [`openpack_toolkit.configs.datasets.splits.PILOT_CHALLENGE_SPLIT`](https://github.com/open-pack/openpack-toolkit/blob/main/openpack_toolkit/configs/datasets/splits.py)

| #   | Usage      | User  | Session |
| --- | ---------- | ----- | ------- |
| 1   | TRAIN      | U0102 | S0100   |
| 2   | TRAIN      | U0102 | S0200   |
| 3   | TRAIN      | U0102 | S0300   |
| 4   | TRAIN      | U0102 | S0400   |
| 5   | TRAIN      | U0102 | S0500   |
| 6   | TRAIN      | U0103 | S0100   |
| 7   | TRAIN      | U0103 | S0200   |
| 8   | TRAIN      | U0103 | S0300   |
| 9   | TRAIN      | U0103 | S0400   |
| 10  | TRAIN      | U0103 | S0500   |
| 11  | TRAIN      | U0105 | S0100   |
| 12  | TRAIN      | U0105 | S0200   |
| 13  | TRAIN      | U0105 | S0300   |
| 14  | TRAIN      | U0105 | S0400   |
| 15  | TRAIN      | U0105 | S0500   |
|     |            |       |         |
| 1   | VAL        | U0106 | S0200   |
| 2   | VAL        | U0106 | S0400   |
|     |            |       |         |
| 1   | TEST       | U0106 | S0100   |
| 2   | TEST       | U0106 | S0300   |
| 3   | TEST       | U0106 | S0500   |
|     |            |       |         |
| 1   | SUBMISSION | U0107 | S0100   |
| 2   | SUBMISSION | U0107 | S0200   |
| 3   | SUBMISSION | U0107 | S0300   |
| 4   | SUBMISSION | U0107 | S0500   |

## Openpack Challenge 2022 Split

Train/val/test/submission Split for OpenPack Challenge. Train/val/test data is set for convenience; feel free to change the entries among them. Challengers should submit predictions for submission set.
For more information, please go to [OpenPack Challenge](./OPENPACK_CHALLENGE/).

- Config File: [openpack-challenge-2022.yaml](https://github.com/open-pack/openpack-toolkit/blob/main/configs/dataset/split/openpack-challenge-2022.yaml)
- Python Class: [`openpack_toolkit.configs.datasets.splits.OPENPACK_CHALLENGE_2022_SPLIT`](https://github.com/open-pack/openpack-toolkit/blob/main/openpack_toolkit/configs/datasets/splits.py)

| #   | Usage      | User  | Session |
| --- | ---------- | ----- | ------- |
| 1   | TRAIN      | U0101 | S0100   |
| 2   | TRAIN      | U0101 | S0200   |
| 3   | TRAIN      | U0101 | S0400   |
| 4   | TRAIN      | U0101 | S0500   |
| 5   | TRAIN      | U0102 | S0100   |
| 6   | TRAIN      | U0102 | S0200   |
| 7   | TRAIN      | U0102 | S0400   |
| 8   | TRAIN      | U0102 | S0500   |
| 9   | TRAIN      | U0103 | S0100   |
| 10  | TRAIN      | U0103 | S0200   |
| 11  | TRAIN      | U0103 | S0400   |
| 12  | TRAIN      | U0103 | S0500   |
| 13  | TRAIN      | U0105 | S0100   |
| 14  | TRAIN      | U0105 | S0200   |
| 15  | TRAIN      | U0105 | S0400   |
| 16  | TRAIN      | U0105 | S0500   |
| 17  | TRAIN      | U0106 | S0100   |
| 18  | TRAIN      | U0106 | S0200   |
| 19  | TRAIN      | U0106 | S0400   |
| 20  | TRAIN      | U0106 | S0500   |
| 21  | TRAIN      | U0107 | S0100   |
| 22  | TRAIN      | U0107 | S0200   |
| 23  | TRAIN      | U0107 | S0400   |
| 24  | TRAIN      | U0107 | S0500   |
| 25  | TRAIN      | U0109 | S0100   |
| 26  | TRAIN      | U0109 | S0200   |
| 27  | TRAIN      | U0109 | S0400   |
| 28  | TRAIN      | U0109 | S0500   |
| 29  | TRAIN      | U0111 | S0100   |
| 30  | TRAIN      | U0111 | S0200   |
| 31  | TRAIN      | U0111 | S0400   |
| 32  | TRAIN      | U0111 | S0500   |
| 33  | TRAIN      | U0202 | S0100   |
| 34  | TRAIN      | U0202 | S0200   |
| 35  | TRAIN      | U0202 | S0400   |
| 36  | TRAIN      | U0202 | S0500   |
| 37  | TRAIN      | U0205 | S0100   |
| 38  | TRAIN      | U0205 | S0200   |
| 39  | TRAIN      | U0205 | S0400   |
| 40  | TRAIN      | U0205 | S0500   |
| 41  | TRAIN      | U0210 | S0100   |
| 42  | TRAIN      | U0210 | S0200   |
| 43  | TRAIN      | U0210 | S0400   |
| 44  | TRAIN      | U0210 | S0500   |
|     |            |       |         |
| 1   | VAL        | U0101 | S0300   |
| 2   | VAL        | U0103 | S0300   |
| 3   | VAL        | U0105 | S0300   |
| 4   | VAL        | U0107 | S0300   |
| 5   | VAL        | U0109 | S0300   |
| 6   | VAL        | U0111 | S0300   |
| 7   | VAL        | U0205 | S0300   |
|     |            |       |         |
| 1   | TEST       | U0102 | S0300   |
| 2   | TEST       | U0106 | S0300   |
| 3   | TEST       | U0202 | S0300   |
| 4   | TEST       | U0210 | S0300   |
|     |            |       |         |
| 1   | SUBMISSION | U0104 | S0100   |
| 2   | SUBMISSION | U0104 | S0300   |
| 3   | SUBMISSION | U0108 | S0100   |
| 4   | SUBMISSION | U0108 | S0200   |
| 5   | SUBMISSION | U0108 | S0300   |
| 6   | SUBMISSION | U0108 | S0500   |
| 7   | SUBMISSION | U0110 | S0100   |
| 8   | SUBMISSION | U0110 | S0200   |
| 9   | SUBMISSION | U0110 | S0300   |
| 10  | SUBMISSION | U0110 | S0400   |
| 11  | SUBMISSION | U0110 | S0500   |
| 12  | SUBMISSION | U0203 | S0100   |
| 13  | SUBMISSION | U0203 | S0200   |
| 14  | SUBMISSION | U0203 | S0300   |
| 15  | SUBMISSION | U0203 | S0400   |
| 16  | SUBMISSION | U0203 | S0500   |
| 17  | SUBMISSION | U0204 | S0200   |
| 18  | SUBMISSION | U0204 | S0300   |
| 19  | SUBMISSION | U0204 | S0400   |
| 20  | SUBMISSION | U0207 | S0300   |
| 21  | SUBMISSION | U0207 | S0400   |
| 22  | SUBMISSION | U0207 | S0500   |
