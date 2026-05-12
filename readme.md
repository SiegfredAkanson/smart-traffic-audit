# Smart Traffic Sensor Network Audit

## Executive Summary
This project was completed as part of an emergency audit for the city's Smart Traffic Sensor Network.
The city developed about 5000 Iot Sensors for monitoring traffic flow, air quality and emergency response routes. 
The system began producing unreliable data due to some missing values and duplicated records and invalid sensor readings.

The purpose of this project was to investigate the quality of the dataset, identify the major issues affecting the network, 
clean the dta and generate strategic insights that can help the city continue the smart traffic initiative.

The cleaned dataset was then transformed into a reliable analytical asset ready for future ML predictive modeling.


# Business Understanding

## Problem Staement
The city is currently losing productivity due to traffic congestion and unreliable traffic monitoring systems.
poor quality sensor dsta can lead to:
1. Incorrect traffic predictions
2. Delays in emergency response routing
3. Wrong navigation decisions
4. Unreliable AI model performance

The aim of the project was to determine whether the dataset could be recovered and used safely for future intelligent traffic systems.


# Dataset Information
https://raw.githubusercontent.com/eyowhite/Messy-dataset/main/warehouse_messy_data.csv

For this simulation:
product_id represents Sensor_ID
warehouse represents Sensor_Hub
Price represents Sensor Sensitivity/Cost

## Tools used
* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook


# Main Data Issues
1. Missing Values
Several records contained missing information in important columns.

2. Duplicate Records
Some sensor logs appeared multiple times, creating false activity levels.

3. Inconsistent Formatting
Text values had different capitalization styles, hidden spaces, and inconsistent naming conventions.

4. Numeric Columns Stored as Text
Some numerical fields contained symbols and text, making calculations difficult.

5. Impossible or Invalid Values
Some records contained unrealistic or invalid values that could affect analysis and AI systems.

These issues showed that the dataset could not be used directly without cleaning and validation.


## Data Preparation

A complete cleaning pipeline was created to transform the messy dataset into a structured and reliable dataset.



## Cleaning Steps Performed

1. Loaded and inspected the raw dataset
2. Standardized column names
3. Cleaned text columns
4. Removed hidden spaces and special characters
5. Converted numerical columns into proper numeric types
6. Handled missing values
7. Removed duplicate records
8. Removed invalid and impossible values
9. Exported the cleaned dataset

The final cleaned dataset was saved as:
**"cleaned smart traffic data.csv"**


# Strategic Intelligence Findings

1. System Reliability:
The analysis showed that some sensor hubs produced more inconsistent and problematic records than others.
This may indicate:
* Hardware failures
* Poor sensor synchronization
* Weak network communication
* Aging equipment

These hubs should be prioritized for physical inspection or replacement.

2. Resource Allocation:
The activity analysis showed that some sensor hubs handled significantly more traffic activity than others.
The visualizations revealed:
* Warehouse/Sensor Hub 2 recorded the highest overall activity
* Warehouse/Sensor Hub 1 showed moderate activity
* Warehouse/Sensor Hub 3 recorded slightly lower activity

This suggests that the city should prioritize infrastructure improvements and monitoring resources in high-activity zones.

3. Hidden Relationship Between Errors and Equipment Type:
The project also investigated whether some equipment categories generated more errors than others.
The analysis suggested that certain categories may have:
* Higher missing value rates
* More inconsistent readings
* Increased duplicate transmissions

This could indicate differences in sensor quality between manufacturers or equipment types.


The project included several visualizations to support decision-making:
* Sensor hub activity chart
* Missing value analysis
* Duplicate record analysis
* Equipment category distribution
* Data quality validation charts

These visualizations helped identify which parts of the network were most active and which areas experienced the highest data reliability problems.


How to run the project
* git clone https://github.com/SiegfredAkanson/smart-traffic-audit
* pip install pandas numpy matplotlib
* python pipeline.py

Or you can navigate to /Smart traffic assignment/scrpts/pipeline.py and run the python script.

# Final Conclusion
This project showed that the Smart-Traffic dataset was not unusable, but rather poorly managed and inconsistent.
After cleaning and validation, the dataset became more reliable and suitable for future traffic analysis and predictive AI systems.
The audit also demonstrated the importance of strong data quality management in smart city infrastructure.