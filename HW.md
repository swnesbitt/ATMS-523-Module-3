# ATMS 523

## Module 3 Project

Submit this code as a pull request back to GitHub Classroom by the date and time listed in Canvas.

1. Adapt the code from class that reads GHCN Daily Data from Amazon Web Services and write a function that will download the station you want (called with a GHCN station ID), and calculate (1) the all time record high and low and (2) the normal (mean) high and low temperature *FOR EACH CALENDAR DAY* for the 1991-2020 period for the desired station.  The function should return a pandas data frame with the columns ['record_min_temp', average_min_temp', 'average_max_temp', record_max_temp'] FOR EACH DAY.  Write a code that can call this function and successfully demonstrate that it works.

2. Develop a plot (using matplotlib) that displays for the city of choice a plot showing the record, average, and actual high and low temperatures for that year and city for each day over the calendar year.  Note: You do not need to make the chart interactive, you can just plot the data from a your city and for the year of your choice.
     
     You are permitted to use the "weather" example from the `bokeh` gallery as inspiration.  An example for what the plot could look like is here: [Weather](https://demo.bokeh.org/weather), and the GitHub repository for the dashboard is [here](https://github.com/bokeh/bokeh/tree/branch-3.9/examples/server/app/weather). Note that you do not have to use bokeh for this assignment, you can use matplotlib!
