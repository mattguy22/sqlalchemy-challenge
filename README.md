# Climate Analysis: Honolulu Vacation

Created by Matthew Guy, 2025

An in-depth research project analyzing climate data for Honolulu, Hawaii using SQLAlchemy, Pandas, and Flask. This project involves connecting to a SQLite database, performing precipitation and station analysis, and designing an API with Flask to expose climate data. The objective is to help with vacation planning by analyzing climate data from the past year.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Database Schema](#database-schema)
- [Running SQL Queries](#running-sql-queries)
- [Data Analysis Queries](#data-analysis-queries)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [About](#about)
- [Resources](#resources)

## Features
- **Database Connection:** Used SQLAlchemy to connect to the SQLite database and reflect the tables into classes.
- **Precipitation Analysis:** Performed a precipitation analysis to gather the last 12 months of data and visualized it.
- **Station Analysis:** Analyzed station data to find the most active station and summarized temperature data.
- **Flask API:** Designed a Flask API that exposes climate data and performs dynamic queries on temperature data.
- **Routes for Climate Data:** Includes routes for precipitation, stations, and temperature observations for a specific year.
- **Start/End Date Range:** Includes routes for querying temperature statistics based on start and end date ranges.

## Installation

### Requirements
- Python 3.x
- Flask
- SQLAlchemy
- SQLite

### Pre-Built Setup
1. Clone or download the repository.
2. Ensure Python 3.x is installed.
3. Install the required libraries using the command: `pip install -r requirements.txt`
4. Download and set up the SQLite database file (`hawaii.sqlite`).

## Usage Instructions
1. **Run the Flask App**  
   Execute the following command to start the Flask server:  
   `python app.py`
2. **Access the API**  
   Open a browser or use a tool like Postman to test the API endpoints.

## Database Schema
The database consists of two tables:

- **Measurement**: Contains daily weather data, including precipitation and temperature observations.
- **Station**: Contains station information, including station IDs and names.

The database schema is reflected through SQLAlchemy classes.

## Running SQL Queries
### Precipitation Analysis
1. Query the most recent date.
2. Retrieve the last 12 months of precipitation data.
3. Use Pandas to load and plot the data.

### Station Analysis
1. Query the number of stations.
2. Identify the most active station (USC00519281).
3. Retrieve the temperature observations (TOBS) for the most active station for the previous year.

## Data Analysis Queries
During the analysis phase, we executed **six SQL queries** to extract key insights from the climate database:

1. **Retrieve Precipitation Data** – List date and precipitation for the last year.
2. **Retrieve Temperature Observations** – List TOBS for the most active station (USC00519281) for the past year.
3. **Station Count** – Count the number of stations in the dataset.
4. **Most Active Station** – Find the station with the most observations.
5. **Temperature Statistics** – Get min, max, and average temperatures for the most active station.
6. **Temperature Histogram** – Plot a histogram of temperature observations for the past year.

## API Endpoints

### `/api/v1.0/precipitation`
- Returns the precipitation data for the last year, with date as the key and precipitation as the value.

### `/api/v1.0/stations`
- Returns a list of all stations in the database.

### `/api/v1.0/tobs`
- Returns temperature observations for the most active station (USC00519281) for the last year.

### `/api/v1.0/<start>`
- Accepts a start date in `YYYY-MM-DD` format and returns min, max, and average temperatures for the specified start date and onwards.

### `/api/v1.0/<start>/<end>`
- Accepts both start and end dates in `YYYY-MM-DD` format and returns min, max, and average temperatures for the specified date range.

## Future Enhancements
- **Implement Caching**: Optimize API calls for frequently requested data.
- **Expand with Additional Data**: Integrate with other weather APIs to enrich the dataset.
- **Create Visual Dashboards**: Use tools like Plotly or Dash to visualize data interactively.

## About
This project aims to provide detailed climate data analysis for Honolulu, Hawaii, to assist with vacation planning. By querying historical precipitation and temperature data, the API helps users assess the area's weather trends over the past year.

## Resources
- **DU Bootcamp Module 10**: Used to help with the climate analysis and the `app.py` script.
- **ChatGPT**: Assisted with syntax and debugging for the route coding in the script.

