# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Import the datetime module
from datetime import datetime, timedelta

# Import json 
import json

# Define one_year_ago at the top of the script, so it is accessible throughout
one_year_ago = datetime.now() - timedelta(days=365)

#################################################
# Database Setup
#################################################

# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the database
session = Session(engine)

# Check the number of records in the station and measurement tables
station_count = session.query(Station).count()
measurement_count = session.query(Measurement).count()

print(f"Number of stations: {station_count}")
print(f"Number of measurements: {measurement_count}")

#################################################
# Flask Setup
#################################################

# Initialize Flask app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Homepage route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (Replace 'start' with a date in YYYY-MM-DD format)<br/>"
        f"/api/v1.0/start/end (Replace 'start' and 'end' with dates in YYYY-MM-DD format)"
    )


# Precipitation Route:
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the most recent date in the dataset (2017-08-23)
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = most_recent_date[0]  # Extract the date from the tuple

    # Query precipitation data from January 1st, 2017, to the most recent available date
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2017-01-01').filter(Measurement.date <= most_recent_date).all()

    # Check if we have data
    if not results:
        return jsonify({"error": "No precipitation data found for the last year."})

    # Create a dictionary with date as key and prcp as value
    precipitation_data = {date: prcp for date, prcp in results}

    # Return the precipitation data as a JSON response
    return jsonify(precipitation_data)


# Stations Route:
@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station).all()

    # Convert the results into a list of stations
    stations_list = list(np.ravel(results))

    # Return the JSON response
    return jsonify(stations_list)


# Temperature Observations (TOBS) Route:
@app.route("/api/v1.0/tobs")
def tobs():
    # Specify the most active station ID (USC00519281)
    most_active_station_id = 'USC00519281'

    # Query the temperature observations (TOBS) for the entire year of 2017
    results = session.query(Measurement.tobs).filter(Measurement.station == most_active_station_id) \
                                              .filter(Measurement.date >= '2017-01-01') \
                                              .filter(Measurement.date <= '2017-12-31').all()

    # Check if we have data
    if not results:
        return jsonify({"error": "No temperature observations data found for the specified station."})

    # Convert the results to a list of temperature observations
    temperature_observations = list(np.ravel(results))

    # Return the JSON response
    return jsonify(temperature_observations)


# Route for /api/v1.0/start (Start date range)
@app.route("/api/v1.0/<start>")
def start(start):
    # Get the most recent date in the dataset
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = most_recent_date[0]  # Extract the date from the tuple

    # Query the database for the temperature statistics (min, avg, max) from the start date to the most recent date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
                     .filter(Measurement.date >= start) \
                     .filter(Measurement.date <= most_recent_date).all()

    # Convert the results into a list
    temp_stats = list(np.ravel(results))

    # Return the JSON response with the temperature statistics
    return jsonify(temp_stats)


# Route for /api/v1.0/start/end (Start to End date range)
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query the database for the temperature statistics (min, avg, max) between the start and end dates
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
                     .filter(Measurement.date >= start) \
                     .filter(Measurement.date <= end).all()

    # Convert the results into a list
    temp_stats = list(np.ravel(results))

    # Return the JSON response with the temperature statistics
    return jsonify(temp_stats)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)