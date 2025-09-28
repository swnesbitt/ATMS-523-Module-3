import pandas as pd


def station_summary(station_id):
    path_to_data = "s3://noaa-ghcn-pds/csv/by_station/" + station_id + ".csv"
    station_data = (
        pd.read_csv(
            path_to_data,
            storage_options={"anon": True},  # passed to `s3fs.S3FileSystem`
            dtype={"Q_FLAG": "object", "M_FLAG": "object"},
            parse_dates=["DATE"],
        )
        .set_index("DATE")
        .sort_index()
        .loc["1991-01-01":"2019-12-31"]
    )
    min_temp = station_data[station_data["ELEMENT"] == "TMIN"][["DATA_VALUE"]]
    max_temp = station_data[station_data["ELEMENT"] == "TMAX"][["DATA_VALUE"]]
    min_temp = min_temp / 10
    max_temp = max_temp / 10
    output = pd.DataFrame(
        [[min_temp.min(), min_temp.mean(), max_temp.mean(), max_temp.max()]]
    )
    output.columns = [
        "record_min_temp",
        "average_min_temp",
        "average_max_temp",
        "record_max_temp",
    ]
    return output


# station_summary("PO000008535")
