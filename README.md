[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
# Overview
This repository includes the materials using during the Business Intelligence (BI) course, Spring 2018.
The course is taught by Hrant Davtyan as an elective course available to MBA students at the American University of Armenia (AUA). 

## Toolbox
During the course students will learn and use several tools necessary for completing a BI project as listed below:

- [Sublime Text Editor](https://www.sublimetext.com/3) - A simple yet powerful (user friendly interface + amazing performance) text editor. During the course Sublime will be used for creating and editing HTML, CSS, XML and JSON documents.
- [JSON formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en) - A google chrome extension which makes the JSON representation indented and highlighted (when viewed directly inside the browser).
- [Anaconda Python 3.6](https://www.continuum.io/downloads) - Python powered open data science platform, which comes toegther with Jupyter notebooks, Spider IDE and some of the most popular Python libraries preinstalled. During the course several python packages will be used. The list of packages (including thsoe preinstalled by Anaconda) is available below.
- [Falcon SQL client](https://plot.ly/free-sql-client-download/) - free and open-source SQL client with inline data visualization based on plotly.

## Required packages
- numpy
- pandas
- sklearn
- pandas_datareader
- googlemaps
- quandl
- matplotlib
- seaborn
- plotly
- dash
- dash-renderer
- dash-html-components
- dash-core-components
 
*The packages **json**, **csv** are also required, yet they come preinstalled with Python 3.6.*

## Installation 
To install the above provided packages please download requirements.txt to your local directory and run the following command in the command prompt:

```
pip install -r requirements.txt
```

## Dashboards in R
R users may complete the course in R. Given that Plotly is available as an R library as well, it will still be the required API for visualization. Shiny, shinydashboard or flexdashboard might be used to develop the applications in R. Shinyapps.io can be served as a platform for deployment.
