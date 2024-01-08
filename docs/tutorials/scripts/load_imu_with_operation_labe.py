import argparse
import datetime
from pathlib import Path

import pandas as pd

NULL_CLASS_ID = 8100


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Load IMU data with operation labels.")
    parser.add_argument(
        "-i",
        "--openpack-rootdir",
        default=Path("./data/datasets/openpack/v1.0.0"),
        type=Path,
        help="path to a openpack dataset dir.",
    )
    parser.add_argument("-o", "--output-dir", default=Path("."), type=Path)
    return parser


def load_imu_sensor_data(openpack_rootdir: Path) -> pd.DataFrame:
    """Load sensor data (atr/atr01; IMU on the right wrist) for Subject `U0101` and Sesion `S0100`."""
    path_imu = Path(openpack_rootdir, "U0101/atr/atr01/S0100.csv")
    df_imu = pd.read_csv(path_imu)

    print("Sensor Data (IMU; atr/atr01) from", path_imu)
    print(df_imu.head())

    return df_imu


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


def main(args: argparse.Namespace):
    df_imu = load_imu_sensor_data(args.openpack_rootdir)
    df_op = load_work_operation_labels(args.openpack_rootdir)

    # Add operation labels to IMU data.
    df_imu = combine_imu_data_and_operation_label(df_imu, df_op)
    print("Combined DataFrame:")
    print(df_imu.head())

    path = Path(args.output_dir, "atr01_with_operation_label.csv")
    df_imu.to_csv(path, index=False)


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
