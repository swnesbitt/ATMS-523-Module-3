# ATMS 523 Module-3

📘 README: Climate Temperature Analysis — Module 3 Assignment

🌍 Project Overview
This notebook analyzes historical temperature data for a selected city using NOAA’s GHCN Daily dataset hosted on AWS. The goal is to:
Calculate record and average high/low temperatures for the 1991–2020 climate normal period.
Visualize how a specific year (2020) compares to those long-term trends using Matplotlib.
This project is part of the ATMS 523 course and emphasizes reproducible, beginner-friendly workflows using open climate data.

🧰 Tools & Libraries
Python
Pandas for data manipulation
Matplotlib for visualization
NOAA GHCN Daily data via AWS S3

📈 What This Notebook Does
Loads daily temperature data for a selected station (e.g., San Diego, CA: USW00093134)
Filters and processes data for:
Record high/low temperatures (1991–2020)
Average high/low temperatures (1991–2020)
Actual high/low temperatures for 2020
Creates a clear, annotated plot comparing all three datasets

🧪 How to Run It
Open the notebook in Jupyter or VS Code (cloud or local).
Make sure you have internet access to read from AWS S3.
Run each cell in order. The plot will appear at the end.

📍 Station Selection
To analyze a different city:
Replace the station_id (e.g., 'USW00093134') with your desired GHCN station code.
You can find station IDs in the GHCN station inventory.

📚 Learning Goals
Practice working with large climate datasets in the cloud
Understand climate normals and variability
Build reproducible, beginner-friendly code and documentation

🤝 Acknowledgments
NOAA for providing open access to GHCN Daily data
ATMS 523 instructors and classmates for support and inspiration
Bokeh’s weather dashboard example for visualization inspiration
