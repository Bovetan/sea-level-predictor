# Sea Level Predictor

This project is part of the FreeCodeCamp Data Analysis with Python certification.

## Description

This project analyzes historical global sea level data and uses linear regression to predict future sea level rise.

The dataset contains measurements of sea level changes from 1880 to recent years. Using this data, two regression models are created to estimate sea level rise up to the year 2050.

## Dataset

The dataset used is `epa-sea-level.csv`.

It contains:

- `Year` → year of measurement  
- `CSIRO Adjusted Sea Level` → adjusted sea level in inches  

## Tasks Completed

- Imported the dataset using Pandas  
- Created a scatter plot to visualize historical data  
- Applied linear regression using all available data (1880–present)  
- Extended the regression line to predict sea level in 2050  
- Applied a second regression using only data from 2000 onward  
- Compared long-term vs recent trends in sea level rise  

## Technologies Used

- Python  
- Pandas  
- Matplotlib  
- SciPy  

## Project Files

- `sea_level_predictor.py` → main implementation  
- `main.py` → execution script  
- `epa-sea-level.csv` → dataset  

## Output

The project generates a visualization with:

- Scatter plot of historical sea level data  
- Red regression line (based on all data)  
- Green regression line (based on data since 2000)  
- Projection of sea level rise up to 2050  

## Author

Bovetan