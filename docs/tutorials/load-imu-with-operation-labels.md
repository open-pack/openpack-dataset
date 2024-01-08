# Load IMU Sensor Data with Operation Labels

The data is saved in separate files for each sensor because the sampling rate differs for each sensor.
Each record has timestamp information and we can combine the multiple data streams using the timestamps.

This tutorial explains how to combine two types of data. As an example, we will merge the IMU data (`atr01`) with the work operation's labels.
Once you know how to combine sensor data with ground truth, you can prepare data for model training.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Sample Script](#sample-script)
- [Step-by-Step Explanation](#step-by-step-explanation)
  - [Step.1 Load IMU Data](#step1-load-imu-data)
  - [Step.2 Load Annotation (Work Operation Label)](#step2-load-annotation-work-operation-label)
  - [Step.3 Combine Operation Labels with IMU DataFrame](#step3-combine-operation-labels-with-imu-dataframe)

## Sample Script

[load_imu_with_operation_labe.py](./scripts/load_imu_with_operation_labe.py)

Usage:

```bash
python load_imu_with_operation_labe.py -i  <PATH to OpenPack DATASET DIR (./data/datasets/openpack/v1.0.0/)>
```

Requirements:

- Python: ^3.9
- Pandas

## Step-by-Step Explanation

### Step.1 Load IMU Data

IMU data from `atr/atr01` (Acc + Gyro at the right wrist) is saved as a CSV file.
Here is a sample implementation to load the data. Pandas is used to read the CSV file.

```python
def load_imu_sensor_data(openpack_rootdir: Path) -> pd.DataFrame:
    """Load sensor data (atr/atr01; IMU on the right wrist) for Subject `U0101` and Sesion `S0100`."""
    path_imu = Path(openpack_rootdir, "U0101/atr/atr01/S0100.csv")
    df_imu = pd.read_csv(path_imu)

    print("Sensor Data (IMU; atr/atr01) from", path_imu)
    print(df_imu.head())

    return df_imu
```

Output:

```txt
Sensor Data (IMU; atr/atr01) from ./data/datasets/openpack/v1.0.0/U0101/atr/atr01/S0100.csv
        unixtime   acc_x   acc_y   acc_z  gyro_x  gyro_y  gyro_z  quat_w  quat_x  quat_y  quat_z
0  1634178333023  0.2838  0.9830  0.0572   -3.21  127.65    7.39     0.0     0.0     0.0     0.0
1  1634178333056  0.2513  0.9357  0.0733   -6.23  155.37   11.12     0.0     0.0     0.0     0.0
2  1634178333089  0.1649  0.9249  0.0713   -6.70  150.33   15.38     0.0     0.0     0.0     0.0
3  1634178333122  0.1222  0.9801  0.1050   -2.93  108.87   20.03     0.0     0.0     0.0     0.0
4  1634178333155  0.1551  1.0636  0.1053   -0.92   77.08   22.49     0.0     0.0     0.0     0.0
```

NOTE: Quaterninon for U0101 is not available. The missing values are filled with `0`.

### Step.2 Load Annotation (Work Operation Label)

Next, let's load the annotation data, which is also saved as CSV.
Unlike other sensor data, the timestamp in annotation data is the ISO format (`str`), not a UNIX timestamp (`int`).
So, added an operation to convert ISO timestamps into UNIX timestamps and save them in columns of `unixtime_start` and `unixtime_end`.

```python
def to_millisecond_timestamp(timestamp_iso: str) -> int:
    """Convert a timestamp (ISO format; string) into a unixtimestamp with millisecond precision.
    For example, `2021-10-14 11:25:35.437000+09:00` will be `1634178335437`.
    """
    return int(datetime.datetime.fromisoformat(timestamp_iso).timestamp() * 1e3)

def load_work_operation_labels(openpack_rootdir: Path) -> pd.DataFrame:
    """Load ground truth label of work operations for for Subject `U0101` and Sesion `S0100`."""
    path_op = Path(openpack_rootdir, "U0101/annotation/openpack-operations/S0100.csv")
    df_op = pd.read_csv(path_op)

    # Timestamps in annotation data are saved in ISO format (e.g., 2021-10-14 11:25:35.437000+09:00) for human
    # readability. So we have to convert them into unixtimestamp (milli-second precision) in advance.
    df_op["unixtime_start"] = df_op["start"].apply(to_millisecond_timestamp)
    df_op["unixtime_end"] = df_op["end"].apply(to_millisecond_timestamp)

    print("Annotation Data (Operation Label) from", path_op)
    print(df_op.head())

    return df_op
```

Output:

```txt
Annotation Data (Operation Label) from ../../../../data/datasets/openpack/v1.0.0/U0101/annotation/openpack-operations/S0100.csv
                                      uuid   user session  box   id            operation                             start                               end                                            actions  unixtime_start   unixtime_end
0  op:da330117-e44b-54cb-b475-086ba0a4e07c  U0101   S0100    1  100              Picking  2021-10-14 11:25:35.437000+09:00  2021-10-14 11:25:48.746000+09:00  act:fede6afd-9b62-58be-9788-cb8189413a78;act:2...   1634178335437  1634178348746
1  op:69ad0c16-3b24-5f19-8fe8-d8f7d3e07ba4  U0101   S0100    1  200  Relocate Item Label  2021-10-14 11:25:48.746000+09:00  2021-10-14 11:25:51.597000+09:00           act:898fed7e-1ee2-5064-8e35-04d4020c4297   1634178348746  1634178351597
2  op:12f44b4c-ac06-572c-a6da-5d93975e30e6  U0101   S0100    1  300         Assemble Box  2021-10-14 11:25:51.597000+09:00  2021-10-14 11:26:12.398000+09:00  act:600df93e-1d80-5f67-b088-7eed8c75e84b;act:5...   1634178351597  1634178372398
3  op:4f5c8dea-09e7-512e-95b3-0917a26652f1  U0101   S0100    1  200  Relocate Item Label  2021-10-14 11:26:12.398000+09:00  2021-10-14 11:26:15.694000+09:00           act:19d31a89-b9ee-5791-b188-4f42161c59d7   1634178372398  1634178375694
4  op:9216f286-efa8-517d-afda-b0c6dc37ec53  U0101   S0100    1  400         Insert Items  2021-10-14 11:26:15.694000+09:00  2021-10-14 11:26:22.250000+09:00           act:de0d2b22-bc8c-5820-b71e-abfc95bcc678   1634178375694  1634178382250
```

### Step.3 Combine Operation Labels with IMU DataFrame

Combines the annotation label with the IMU data using UNIX timestamps.
First, create a new column `operation` in `df_imu` to store operation labels.
The default value should be the ID for the Null class (`8100`, Ref: [ANNOTATION.md](../ANNOTATION.md)).
Extract records obtained between the `unixtime_start` and `unixtime_end` of a label, and update the operation IDs of the records.

```python
NULL_CLASS_ID = 8100

def combine_imu_data_and_operation_label(
    df_imu: pd.DataFrame, df_op: pd.DataFrame
) -> pd.DataFrame:
    df_imu["operation"] = NULL_CLASS_ID
    for _, row in df_op.iterrows():
        timestamp_start = row["unixtime_start"]
        timestamp_end = row["unixtime_end"]
        operation_id = row["id"]

        indices = df_imu[
            (df_imu["unixtime"] >= timestamp_start)
            & (df_imu["unixtime"] < timestamp_end)
        ].index
        df_imu.loc[indices, "operation"] = operation_id

    return df_imu
```

Output: You can see the new column `operation`.

```txt
        unixtime   acc_x   acc_y   acc_z  gyro_x  gyro_y  gyro_z  quat_w  quat_x  quat_y  quat_z  operation
0  1634178333023  0.2838  0.9830  0.0572   -3.21  127.65    7.39     0.0     0.0     0.0     0.0       8100
1  1634178333056  0.2513  0.9357  0.0733   -6.23  155.37   11.12     0.0     0.0     0.0     0.0       8100
2  1634178333089  0.1649  0.9249  0.0713   -6.70  150.33   15.38     0.0     0.0     0.0     0.0       8100
3  1634178333122  0.1222  0.9801  0.1050   -2.93  108.87   20.03     0.0     0.0     0.0     0.0       8100
4  1634178333155  0.1551  1.0636  0.1053   -0.92   77.08   22.49     0.0     0.0     0.0     0.0       8100
```
