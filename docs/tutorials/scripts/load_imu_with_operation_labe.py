import datetime
from pathlib import Path

import pandas as pd


START_KEY_NAME = "start"
END_KEY_NAME = "end"
TIMESTAMP_START_KEY_NAME = "timestamp_start"
TIMESTAMP_END_KEY_NAME = "timestamp_end"
OPERATION_ID_KEY_NAME = "id"

UNIXTIME_KEY_NAME = "unixtime"
OPERATION_KEY_NAME = "operation"

NULL_CLASS_ID = 8100


def to_millisecond_timestamp(timestamp_iso: str) -> int:
    """Convert a timestamp (ISO format; string) into a millisecond precision
    timestamp. For example, `2021-10-14 11:25:35.437000+09:00` will be `1634178335437`.
    """
    return int(datetime.datetime.fromisoformat(timestamp_iso).timestamp() * 1e3)


def combine_imu_data_and_operation_label(
    df_imu: pd.DataFrame, df_op: pd.DataFrame
) -> pd.DataFrame:
    df_imu[OPERATION_KEY_NAME] = NULL_CLASS_ID
    for _, row in df_op.iterrows():
        timestamp_start = row[TIMESTAMP_START_KEY_NAME]
        timestamp_end = row[TIMESTAMP_END_KEY_NAME]
        operation_id = row[OPERATION_ID_KEY_NAME]

        indices = df_imu[
            (df_imu[UNIXTIME_KEY_NAME] >= timestamp_start)
            & (df_imu[UNIXTIME_KEY_NAME] < timestamp_end)
        ].index
        df_imu.loc[indices, OPERATION_KEY_NAME] = operation_id

    return df_imu


def main():
    openpack_rootdir = Path("../../data/datasets/openpack/v1.0.0")

    # Load IMU data (atr/atr01)
    path_imu = Path(openpack_rootdir, "U0101/atr/atr01/S0100.csv")
    df_imu = pd.read_csv(path_imu)
    print("Sensor Data (IMU; atr/atr01) from", path_imu)
    print(df_imu.head())

    # Load Operation Labels
    path_op = Path(openpack_rootdir, "U0101/annotation/openpack-operations/S0100.csv")
    df_op = pd.read_csv(path_op)
    df_op[TIMESTAMP_START_KEY_NAME] = df_op[START_KEY_NAME].apply(
        to_millisecond_timestamp
    )
    df_op[TIMESTAMP_END_KEY_NAME] = df_op[END_KEY_NAME].apply(to_millisecond_timestamp)
    print("Annotation Data (Operation Label) from", path_op)
    print(df_op.head())

    # Add operation labels to IMU data.
    df_imu = combine_imu_data_and_operation_label(df_imu, df_op)
    print("Combined DataFrame:")
    print(df_imu.head())


if __name__ == "__main__":
    main()
