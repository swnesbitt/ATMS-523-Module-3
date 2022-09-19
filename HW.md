# ATMS 523

## Module 3 Project

Submit this code as a pull request back to GitHub Classroom by the date and time listed in Canvas.

1. Adapt the code from class that reads GHCN Daily Data from Amazon Web Services and write a function that will download the station you want (called with a GHCN station ID), and calculate the all time record high and low and the normal (mean) high and low temperature for the 1981-2010 period for the desired station and returns a pandas data frame with the columns ['record_min_temp', average_min_temp', 'average_max_temp', record_max_temp'].  Write a code that can call this function and successfully demonstrate that it works.

2. Develop a bokeh GHCN annual weather data dashboard that displays in a web site where the user can select 
   
   - a city from a dropdown of 5 cities you pick that have data at least from 1981-present, 
   
   - a dropdown that selects a year from the data record of those cities.
     
     The dashboard will generate a plot showing the record, average, and actual high and low temperatures for that year and city.  
     
     You are permitted to use the "weather" example from the `bokeh` gallery as a basis.  A running example for the dashboard can be found here: [Weather](https://demo.bokeh.org/weather), and the GitHub repository for the dashboard is here: [bokeh/examples/app/weather at branch-3.0 · bokeh/bokeh · GitHub](https://github.com/bokeh/bokeh/tree/branch-3.0/examples/app/weather).
