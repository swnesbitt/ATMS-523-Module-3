# ATMS 523

## Module 3 Project

Submit this code as a pull request back to GitHub Classroom by the date and time listed in Canvas.

1. Adapt the code from class that reads GHCN Daily Data from Amazon Web Services and write a function that will download the station you want (called with a GHCN station ID), and calculate the all time record high and low and the normal (mean) high and low temperature for the 1991-2020 period for the desired station and returns a pandas data frame with the columns ['record_min_temp', average_min_temp', 'average_max_temp', record_max_temp'].  Write a code that can call this function and successfully demonstrate that it works.

2. Develop a plot (using matplotlib) that displays for the city of choice a plot showing the record, average, and actual high and low temperatures for that year and city.  
     
     You are permitted to use the "weather" example from the `bokeh` gallery as inspiration.  A running example for what the plot could look like is here: [Weather](https://demo.bokeh.org/weather), and the GitHub repository for the dashboard is [here](https://github.com/bokeh/bokeh/tree/branch-3.9/examples/server/app/weather). Note that you do not have to use bokeh for this assignment, you can use matplotlib!
