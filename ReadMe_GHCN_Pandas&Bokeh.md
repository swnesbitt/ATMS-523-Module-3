# ATMS 523 Weather and Climate Data Analytics
## Project 3: Introduction to Cloud Pandas

Author: deffip2@illinois.edu

### Task:
Create code to access AWS cloud data and using `pandas` to process the data.

### Goals:
1. Access data from AWS cloud.
2. Process station data for a certain period using `pandas`
3. Visualize the data interactively using `bokeh`.

### Data Source:
the NOAA Global Historical Climatology Network Daily (GHCN-D) database (https://doi.org/10.7289/V5D21VHZ)
Retreived from Amazon Web Services (https://registry.opendata.aws/noaa-ghcn/)

### Steps:
1. Access the station data from AWS cloud data and open it using `pandas parquet`. This format is more efficient to process compare to the common tabular data format (e.g. csv)
2. Data processing using pandas, such as: creating a new index (with pd.to_datetime), creating a new dataframe, selecting the highest and the lowest value (.max and .min), calculate normal value (.mean) and selecting a certain period of time (pd.Timestamp)
3. Visualize the data using `bokeh` by creating overlay plots of all recorded data, normal values and actual values for a selected year. The interactive plot has hover to show the temperature values for the pointed date. The plotting is exported into .html to provide web based visual output.

### Required libraries:
1. pandas
2. numpy
3. bokeh