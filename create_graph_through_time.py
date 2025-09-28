import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_graph_through_time(station_id):
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
    annual_min = min_temp.groupby(min_temp.index.year)["DATA_VALUE"].min()
    annual_max = max_temp.groupby(max_temp.index.year)["DATA_VALUE"].max()
    record_min = annual_min.min()
    average_min = annual_min.mean()
    average_max = annual_max.mean()
    record_max = annual_max.max()
    plt.figure(figsize=(12, 7))
    plt.scatter(
        annual_min.index,
        annual_min.values,
        color="blue",
        label="Annual Record Low",
        marker="o",
        s=50,
        zorder=3,  # Ensures points are drawn on top
    )
    plt.scatter(
        annual_max.index,
        annual_max.values,
        color="red",
        label="Annual Record High",
        marker="o",
        s=50,
        zorder=3,
    )
    plt.hlines(
        record_max,
        1991,
        2019,
        color="darkred",
        linestyle="-",
        linewidth=2,
        label=f"Lifetime Record Max: {record_max:.1f} °C",
        zorder=1,
    )
    plt.hlines(
        average_max,
        1991,
        2019,
        color="salmon",
        linestyle="--",
        linewidth=2,
        label=f"Lifetime Average Max: {average_max:.1f} °C",
        zorder=2,
    )
    plt.hlines(
        average_min,
        1991,
        2019,
        color="skyblue",
        linestyle="--",
        linewidth=2,
        label=f"Lifetime Average Min: {average_min:.1f} °C",
        zorder=2,
    )
    plt.hlines(
        record_min,
        1991,
        2019,
        color="darkblue",
        linestyle="-",
        linewidth=2,
        label=f"Lifetime Record Min: {record_min:.1f} °C",
        zorder=1,
    )

    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.title(
        f"Annual Extreme Temperatures vs. Lifetime Statistics (1991–2019)", fontsize=14
    )

    plt.xticks(np.arange(1991, 2019 + 1, 5))

    plt.legend(loc="upper right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


# create_graph_through_time('PO000008535')
