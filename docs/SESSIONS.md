# Data Collection Scenarios and Available Sessions

## Data Collection Scenarios

It is very difficult to perform work activity recognition in-the-wild.
Therefore, we created four scenarios that allow us to gradually advance the level of the work activity recognition algorithm while reproducing situations that may occur in a distribution center.
Details of each scenario are as follows.

### Scenario.1 (S1)

In this scenario, we asked the subjects to follow the work instructions as much as possible. A list of items in an order was determined based on order sheets collected in actual logistics centers, and the probabilities with which very large or small items were included in an order were higher than the actual probabilities. In addition, the variety of items to be packed was limited (54 items). The number of items in an order was 1.83 on average.

### Scenario.2 (S2)

In this scenario, we encouraged the subjects to alter the procedure of operations at their discretion. In addition, the probabilities with which quite large or small items were included in an order were lower than those of Scenario 1 (similar to actual probabilities), which made recognizing related operations with supervised learning difficult due to the data imbalance issue. The number of items in an order was 2.04 on average. In addition, we added 21 new items.

### Scenario.3 (S3)

In this scenario, irregular situations/actions were added to Scenario 2. (i) Some shipping boxes were already assembled (because of mistakes, for example) and were available for workers to use. (ii) When small items (such as dry-cell batteries) were included in an order, a subject was also asked to put them in a paper bag. (iii) When multiple consecutive orders included only small items, a subject could bring them from the back table to the workbench at the same time.

### Scenario.4 (S4)

To simulate a busy working time, we rushed the subjects by introducing an auditory alarm in Scenario 3. We measured the average duration of a work period performed by a subject in prior sessions, and we started periodic alarms (30-45 s interval) when the elapsed time of a period exceeded about 80\% of the average duration.

## Recording Sessions

This is a list of recorded sessions.
Each subjects peformed up to 5 sessions and each session has ID like `S0100`.
The pair of user ID and session ID can be used to identify the unique data segments.
The segment between `Start` and `End` specifies the start and end points of the annotation.

| Subject | Session | Scenario | Duration | Periods | Start                     | End                       |
| ------- | ------- | -------- | -------- | ------- | ------------------------- | ------------------------- |
| U0101   | S0100   | S1       | 35m36s   | 20      | 2021-10-14 11:25:34+09:00 | 2021-10-14 12:01:10+09:00 |
| U0101   | S0200   | S1       | 28m54s   | 20      | 2021-10-14 13:17:42+09:00 | 2021-10-14 13:46:36+09:00 |
| U0101   | S0300   | S1       | 28m58s   | 20      | 2021-10-14 14:09:10+09:00 | 2021-10-14 14:38:08+09:00 |
| U0101   | S0400   | S1       | 30m55s   | 20      | 2021-10-14 14:59:48+09:00 | 2021-10-14 15:30:43+09:00 |
| U0101   | S0500   | S1       | 27m35s   | 20      | 2021-10-14 15:54:05+09:00 | 2021-10-14 16:21:40+09:00 |
| U0102   | S0100   | S1       | 50m13s   | 20      | 2021-10-22 11:19:54+09:00 | 2021-10-22 12:10:07+09:00 |
| U0102   | S0200   | S1       | 39m08s   | 20      | 2021-10-22 12:31:14+09:00 | 2021-10-22 13:10:22+09:00 |
| U0102   | S0300   | S1       | 36m44s   | 20      | 2021-10-22 14:14:44+09:00 | 2021-10-22 14:51:28+09:00 |
| U0102   | S0400   | S1       | 33m18s   | 20      | 2021-10-22 15:08:18+09:00 | 2021-10-22 15:41:36+09:00 |
| U0102   | S0500   | S1       | 30m22s   | 14      | 2021-10-22 15:56:26+09:00 | 2021-10-22 16:26:48+09:00 |
| U0103   | S0100   | S1       | 19m58s   | 10      | 2021-11-12 12:39:05+09:00 | 2021-11-12 12:59:03+09:00 |
| U0103   | S0200   | S1       | 35m46s   | 20      | 2021-11-12 14:11:27+09:00 | 2021-11-12 14:47:13+09:00 |
| U0103   | S0300   | S1       | 33m58s   | 20      | 2021-11-12 15:11:14+09:00 | 2021-11-12 15:45:12+09:00 |
| U0103   | S0400   | S1       | 31m48s   | 20      | 2021-11-12 16:07:15+09:00 | 2021-11-12 16:39:03+09:00 |
| U0103   | S0500   | S1       | 30m11s   | 20      | 2021-11-12 17:19:24+09:00 | 2021-11-12 17:49:35+09:00 |
| U0104   | S0100   | S1       | 50m04s   | 20      | 2021-11-16 12:17:55+09:00 | 2021-11-16 13:07:59+09:00 |
| U0104   | S0200   | S1       | 47m03s   | 20      | 2021-11-16 14:22:07+09:00 | 2021-11-16 15:09:10+09:00 |
| U0104   | S0300   | S1       | 37m56s   | 19      | 2021-11-16 15:30:49+09:00 | 2021-11-16 16:08:45+09:00 |
| U0104   | S0400   | S1       | 17m54s   | 10      | 2021-11-16 16:26:44+09:00 | 2021-11-16 16:44:38+09:00 |
| U0105   | S0100   | S1       | 40m46s   | 20      | 2021-11-19 11:20:22+09:00 | 2021-11-19 12:01:08+09:00 |
| U0105   | S0200   | S1       | 37m00s   | 20      | 2021-11-19 12:19:30+09:00 | 2021-11-19 12:56:30+09:00 |
| U0105   | S0300   | S1       | 33m36s   | 20      | 2021-11-19 14:04:16+09:00 | 2021-11-19 14:37:52+09:00 |
| U0105   | S0400   | S1       | 33m34s   | 20      | 2021-11-19 14:59:11+09:00 | 2021-11-19 15:32:45+09:00 |
| U0105   | S0500   | S1       | 33m27s   | 20      | 2021-11-19 15:51:15+09:00 | 2021-11-19 16:24:42+09:00 |
| U0106   | S0100   | S1       | 49m06s   | 20      | 2021-11-26 11:12:26+09:00 | 2021-11-26 12:01:32+09:00 |
| U0106   | S0200   | S1       | 35m00s   | 20      | 2021-11-26 12:22:04+09:00 | 2021-11-26 12:57:04+09:00 |
| U0106   | S0300   | S1       | 34m18s   | 20      | 2021-11-26 14:14:41+09:00 | 2021-11-26 14:48:59+09:00 |
| U0106   | S0400   | S1       | 36m24s   | 20      | 2021-11-26 15:06:35+09:00 | 2021-11-26 15:42:59+09:00 |
| U0106   | S0500   | S1       | 17m09s   | 10      | 2021-11-26 16:01:46+09:00 | 2021-11-26 16:18:55+09:00 |
| U0107   | S0100   | S1       | 37m18s   | 20      | 2021-12-03 11:10:06+09:00 | 2021-12-03 11:47:24+09:00 |
| U0107   | S0200   | S1       | 35m26s   | 20      | 2021-12-03 12:07:50+09:00 | 2021-12-03 12:43:16+09:00 |
| U0107   | S0300   | S1       | 14m00s   | 9       | 2021-12-03 13:52:41+09:00 | 2021-12-03 14:06:41+09:00 |
| U0107   | S0400   | S1       | 30m17s   | 20      | 2021-12-03 14:43:09+09:00 | 2021-12-03 15:13:26+09:00 |
| U0107   | S0500   | S1       | 30m06s   | 20      | 2021-12-03 15:32:26+09:00 | 2021-12-03 16:02:32+09:00 |
| U0108   | S0100   | S1       | 35m54s   | 20      | 2021-12-09 10:06:05+09:00 | 2021-12-09 10:41:59+09:00 |
| U0108   | S0200   | S1       | 39m05s   | 20      | 2021-12-09 11:02:04+09:00 | 2021-12-09 11:41:09+09:00 |
| U0108   | S0300   | S1       | 34m40s   | 20      | 2021-12-09 12:00:31+09:00 | 2021-12-09 12:35:11+09:00 |
| U0108   | S0400   | S1       | 38m37s   | 20      | 2021-12-09 13:42:47+09:00 | 2021-12-09 14:21:24+09:00 |
| U0108   | S0500   | S1       | 34m23s   | 20      | 2021-12-09 14:42:38+09:00 | 2021-12-09 15:17:01+09:00 |
| U0109   | S0100   | S1       | 36m53s   | 16      | 2021-12-17 12:34:27+09:00 | 2021-12-17 13:11:20+09:00 |
| U0109   | S0200   | S1       | 45m28s   | 20      | 2021-12-17 13:43:53+09:00 | 2021-12-17 14:29:21+09:00 |
| U0109   | S0300   | S1       | 35m26s   | 20      | 2021-12-17 14:47:25+09:00 | 2021-12-17 15:22:51+09:00 |
| U0109   | S0400   | S1       | 33m38s   | 20      | 2021-12-17 16:02:12+09:00 | 2021-12-17 16:35:50+09:00 |
| U0109   | S0500   | S1       | 33m18s   | 20      | 2021-12-17 16:58:26+09:00 | 2021-12-17 17:31:44+09:00 |
| U0110   | S0100   | S1       | 29m55s   | 20      | 2021-12-22 10:58:06+09:00 | 2021-12-22 11:28:01+09:00 |
| U0110   | S0200   | S1       | 24m16s   | 20      | 2021-12-22 11:49:00+09:00 | 2021-12-22 12:13:16+09:00 |
| U0110   | S0300   | S1       | 24m35s   | 20      | 2021-12-22 13:18:29+09:00 | 2021-12-22 13:43:04+09:00 |
| U0110   | S0400   | S1       | 23m41s   | 20      | 2021-12-22 14:02:58+09:00 | 2021-12-22 14:26:39+09:00 |
| U0110   | S0500   | S1       | 22m22s   | 20      | 2021-12-22 14:46:36+09:00 | 2021-12-22 15:08:58+09:00 |
| U0111   | S0100   | S1       | 44m43s   | 20      | 2021-12-27 11:11:59+09:00 | 2021-12-27 11:56:42+09:00 |
| U0111   | S0200   | S1       | 34m51s   | 20      | 2021-12-27 12:17:29+09:00 | 2021-12-27 12:52:20+09:00 |
| U0111   | S0300   | S1       | 35m07s   | 20      | 2021-12-27 14:03:51+09:00 | 2021-12-27 14:38:58+09:00 |
| U0111   | S0400   | S1       | 34m18s   | 20      | 2021-12-27 14:57:04+09:00 | 2021-12-27 15:31:22+09:00 |
| U0111   | S0500   | S1       | 32m44s   | 20      | 2021-12-27 15:52:42+09:00 | 2021-12-27 16:25:26+09:00 |
| U0201   | S0100   | S2       | 39m33s   | 20      | 2022-03-01 11:51:11+09:00 | 2022-03-01 12:30:44+09:00 |
| U0201   | S0200   | S3       | 22m26s   | 12      | 2022-03-01 14:17:59+09:00 | 2022-03-01 14:40:25+09:00 |
| U0201   | S0300   | S3       | 36m14s   | 20      | 2022-03-01 15:27:12+09:00 | 2022-03-01 16:03:26+09:00 |
| U0201   | S0400   | S4       | 28m18s   | 20      | 2022-03-15 15:26:02+09:00 | 2022-03-15 15:54:20+09:00 |
| U0201   | S0500   | S2       | 25m27s   | 20      | 2022-03-22 15:11:48+09:00 | 2022-03-22 15:37:15+09:00 |
| U0202   | S0100   | S2       | 37m16s   | 20      | 2022-03-04 10:15:01+09:00 | 2022-03-04 10:52:17+09:00 |
| U0202   | S0200   | S2       | 29m27s   | 20      | 2022-03-04 11:17:46+09:00 | 2022-03-04 11:47:13+09:00 |
| U0202   | S0300   | S3       | 34m10s   | 20      | 2022-03-04 13:13:18+09:00 | 2022-03-04 13:47:28+09:00 |
| U0202   | S0400   | S3       | 32m13s   | 20      | 2022-03-04 14:11:16+09:00 | 2022-03-04 14:43:29+09:00 |
| U0202   | S0500   | S4       | 17m54s   | 15      | 2022-03-04 15:06:58+09:00 | 2022-03-04 15:24:52+09:00 |
| U0203   | S0100   | S2       | 36m08s   | 20      | 2022-03-09 10:01:21+09:00 | 2022-03-09 10:37:29+09:00 |
| U0203   | S0200   | S2       | 34m25s   | 20      | 2022-03-09 11:00:45+09:00 | 2022-03-09 11:35:10+09:00 |
| U0203   | S0300   | S3       | 33m14s   | 20      | 2022-03-09 12:02:22+09:00 | 2022-03-09 12:35:36+09:00 |
| U0203   | S0400   | S3       | 31m57s   | 20      | 2022-03-09 13:53:47+09:00 | 2022-03-09 14:25:44+09:00 |
| U0203   | S0500   | S4       | 25m59s   | 20      | 2022-03-09 14:57:47+09:00 | 2022-03-09 15:23:46+09:00 |
| U0204   | S0100   | S2       | 26m04s   | 20      | 2022-03-11 10:03:22+09:00 | 2022-03-11 10:29:26+09:00 |
| U0204   | S0200   | S2       | 22m29s   | 20      | 2022-03-11 10:49:10+09:00 | 2022-03-11 11:11:39+09:00 |
| U0204   | S0300   | S3       | 24m52s   | 20      | 2022-03-11 11:37:19+09:00 | 2022-03-11 12:02:11+09:00 |
| U0204   | S0400   | S3       | 22m47s   | 20      | 2022-03-11 13:11:35+09:00 | 2022-03-11 13:34:22+09:00 |
| U0204   | S0500   | S4       | 20m31s   | 20      | 2022-03-11 13:56:23+09:00 | 2022-03-11 14:16:54+09:00 |
| U0205   | S0100   | S2       | 36m05s   | 20      | 2022-03-15 10:07:01+09:00 | 2022-03-15 10:43:06+09:00 |
| U0205   | S0200   | S2       | 32m09s   | 20      | 2022-03-15 11:04:15+09:00 | 2022-03-15 11:36:24+09:00 |
| U0205   | S0300   | S3       | 33m07s   | 20      | 2022-03-15 12:00:07+09:00 | 2022-03-15 12:33:14+09:00 |
| U0205   | S0400   | S3       | 29m27s   | 20      | 2022-03-15 13:41:19+09:00 | 2022-03-15 14:10:46+09:00 |
| U0205   | S0500   | S4       | 24m39s   | 20      | 2022-03-15 14:32:07+09:00 | 2022-03-15 14:56:46+09:00 |
| U0206   | S0100   | S2       | 34m33s   | 20      | 2022-03-18 09:51:15+09:00 | 2022-03-18 10:25:48+09:00 |
| U0206   | S0200   | S2       | 29m45s   | 20      | 2022-03-18 10:49:15+09:00 | 2022-03-18 11:19:00+09:00 |
| U0206   | S0300   | S3       | 24m12s   | 20      | 2022-03-18 11:41:59+09:00 | 2022-03-18 12:06:11+09:00 |
| U0206   | S0400   | S3       | 26m29s   | 20      | 2022-03-18 13:20:21+09:00 | 2022-03-18 13:46:50+09:00 |
| U0206   | S0500   | S4       | 28m15s   | 20      | 2022-03-18 14:11:02+09:00 | 2022-03-18 14:39:17+09:00 |
| U0207   | S0100   | S2       | 29m23s   | 20      | 2022-03-22 10:19:53+09:00 | 2022-03-22 10:49:16+09:00 |
| U0207   | S0200   | S2       | 23m06s   | 20      | 2022-03-22 11:12:38+09:00 | 2022-03-22 11:35:44+09:00 |
| U0207   | S0300   | S3       | 23m45s   | 20      | 2022-03-22 11:59:39+09:00 | 2022-03-22 12:23:24+09:00 |
| U0207   | S0400   | S3       | 23m09s   | 20      | 2022-03-22 13:40:07+09:00 | 2022-03-22 14:03:16+09:00 |
| U0207   | S0500   | S4       | 20m41s   | 20      | 2022-03-22 14:27:39+09:00 | 2022-03-22 14:48:20+09:00 |
| U0208   | S0100   | S2       | 31m52s   | 20      | 2022-03-25 09:58:21+09:00 | 2022-03-25 10:30:13+09:00 |
| U0208   | S0200   | S2       | 27m37s   | 20      | 2022-03-25 10:54:01+09:00 | 2022-03-25 11:21:38+09:00 |
| U0208   | S0300   | S3       | 26m59s   | 20      | 2022-03-25 11:47:09+09:00 | 2022-03-25 12:14:08+09:00 |
| U0208   | S0400   | S3       | 27m10s   | 20      | 2022-03-25 13:36:58+09:00 | 2022-03-25 14:04:08+09:00 |
| U0208   | S0500   | S4       | 20m21s   | 20      | 2022-03-25 14:28:24+09:00 | 2022-03-25 14:48:45+09:00 |
| U0209   | S0100   | S2       | 36m54s   | 20      | 2022-03-29 09:53:59+09:00 | 2022-03-29 10:30:53+09:00 |
| U0209   | S0200   | S2       | 29m33s   | 20      | 2022-03-29 10:55:20+09:00 | 2022-03-29 11:24:53+09:00 |
| U0209   | S0300   | S3       | 28m52s   | 20      | 2022-03-29 11:52:39+09:00 | 2022-03-29 12:21:31+09:00 |
| U0209   | S0400   | S3       | 29m29s   | 20      | 2022-03-29 13:31:48+09:00 | 2022-03-29 14:01:17+09:00 |
| U0209   | S0500   | S4       | 23m22s   | 20      | 2022-03-29 14:25:22+09:00 | 2022-03-29 14:48:44+09:00 |
| U0210   | S0100   | S2       | 28m02s   | 20      | 2022-04-01 09:38:12+09:00 | 2022-04-01 10:06:14+09:00 |
| U0210   | S0200   | S2       | 25m39s   | 20      | 2022-04-01 10:28:23+09:00 | 2022-04-01 10:54:02+09:00 |
| U0210   | S0300   | S3       | 29m11s   | 20      | 2022-04-01 11:19:27+09:00 | 2022-04-01 11:48:38+09:00 |
| U0210   | S0400   | S3       | 26m18s   | 20      | 2022-04-01 13:03:35+09:00 | 2022-04-01 13:29:53+09:00 |
| U0210   | S0500   | S4       | 21m26s   | 20      | 2022-04-01 13:53:29+09:00 | 2022-04-01 14:14:55+09:00 |

NOTE: `Period` is a number of packed boxes (or repetitions) that have been already annotated.
Due to sensor data issues, some periods are not annotated.
We are working hard to fix these problems. Thank you for your patience.

## Kwown Recording Errors

Here is a list of known recording errors.
It is recommended that this list be checked carefully and, if necessary, excluded from the experiment.

| Subject | Sessions | Box                               | Stream                          | Error                                                                                                             | Status             |
| ------- | -------- | --------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------ |
| U0101   | S0100    | ALL                               | rs02,                           | Original bag file of rs02 is borken and unable to read.                                                           | `NO FIX AVAILABLE` |
| U0101   | S0200    | ALL                               | rs02,                           | Original bag file of rs02 is borken and unable to read.                                                           | `NO FIX AVAILABLE` |
| U0103   | S0100    | 1,2,3,4,5,6,7,8,9,10,             | atr01,atr02,atr03,atr04,        | ATR sensors were not working. Annotation process is suspended.                                                    | `PENDING`          |
| U0103   | S0300    | ALL                               | atr03,                          | ATR03 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0103   | S0400    | ALL                               | atr03,                          | ATR03 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0104   | S0200    | ALL                               | atr03,atr04,                    | The position of ATR03 and ATR04 seem to be swapped.                                                               | `PENDING`          |
| U0104   | S0400    | ALL                               | atr03,atr04,                    | The position of ATR03 and ATR04 seem to be swapped.                                                               | `PENDING`          |
| U0106   | S0400    | ALL                               | lidar,                          | An error occurs when loading data, and the frame extraction process has not been completed.                       | `PENDING`          |
| U0106   | S0500    | ALL                               | lidar,                          | An error occurs when loading data, and the frame extraction process has not been completed.                       | `PENDING`          |
| U0107   | S0400    | ALL                               | atr03,                          | ATR01 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0107   | S0300    | 10,11,12,13,14,15,16,17,18,19,20, | kinect,                         | Video data (kinect) is missing. Annotation process is suspended.                                                  | `PENDING`          |
| U0108   | S0400    | 1,2,3,4,5,6,7,8,9,10,             | atr01,atr02,atr03,atr04,        | ATR was not working for these boxes. The timestamps of the ATR data sequences in the data set are not consistent. | `NO FIX AVAILABLE` |
| U0109   | S0100    | 17,18,19,20,                      | kinect,atr01,atr02,atr03,atr04, | ATR was not available. Annotation process is suspended.                                                           | `PENDING`          |
| U0204   | S0100    | ALL                               | atr02,                          | ATR02 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0204   | S0500    | ALL                               | atr02,                          | ATR02 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0207   | S0100    | ALL                               | atr02,                          | ATR02 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0207   | S0200    | ALL                               | atr03,                          | ATR03 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0209   | S0400    | ALL                               | atr03,                          | ATR03 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |
| U0209   | S0500    | ALL                               | atr03,                          | ATR03 was attached in the wrong direction.                                                                        | `NO FIX AVAILABLE` |

## Links

- [Subjects Metadata](./SUBJECTS.md)
