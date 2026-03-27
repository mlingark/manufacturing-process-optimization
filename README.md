# Manufacturing Process Optimization

A Python project that simulates realistic manufacturing job data and analyzes production performance across machines, materials, operators, and process conditions.

This project was built to model how real shop-floor variables can influence product quality, defect rates, cycle time, and production cost. It combines simulated manufacturing data generation with exploratory data analysis and machine-level performance scoring to identify which setups offer the best balance of quality and efficiency.

## Project Overview

Manufacturing environments are affected by more than just machine choice. Production outcomes also depend on factors such as:

- material type
- process complexity
- operator experience
- tool condition
- rush orders
- downtime events
- inspection level
- deburring and secondary operations

This project simulates those relationships and analyzes how they impact defect rates and cost. It demonstrates how data analysis can be applied to manufacturing operations. Instead of only reporting basic averages, it explores how production variables interact and how those interactions affect business outcomes. The following processes are used:

- building realistic datasets
- cleaning and transforming data
- performing exploratory analysis
- visualizing patterns
- comparing tradeoffs across multiple business metrics

## Project Goals

- Generate realistic manufacturing job records
- Simulate defect patterns using production-related variables
- Compare machine performance across quality and cost metrics
- Analyze which operational factors are associated with higher defect risk
- Build a portfolio-ready project that demonstrates Python, pandas, and data analysis skills

### Example Business Questions Answered

This project helps answer questions such as:

- Which machine has the lowest average defect rate?
- Which materials are associated with the most defects?
- Do rush orders increase production risk?
- Does tool wear affect quality outcomes?
- How does complexity impact cost and defect rate?
- Which machine offers the best balance between quality, cost, and speed?

## Project Files

- `data_generator.py`  
  Generates simulated manufacturing job data and exports it to a CSV file

- `analysis.py`  
  Loads the dataset, performs analysis, creates visualizations, and compares machine performance

- `manufacturing_defect_data.csv`  
  Simulated dataset containing manufacturing job records

- `readme.md`  
  Project documentation

## Simulated Data Features

The generated dataset includes variables such as:

- Job ID
- Customer
- Industry
- Shift
- Material
- Machine
- Department
- Process Type
- Complexity Score
- Operator ID
- Operator Level
- Tool Condition
- Rush Order
- Machine Downtime
- Inspection Type
- Outside Process
- Hardware Requirement
- Deburr Method
- Setup Minutes
- Cycle Time Seconds
- Total Parts
- Defect Count
- Defect Rate
- Defect Type
- Possible Cause
- Scrap Cost Per Part
- Production Cost

These features were designed to make the dataset more realistic and more useful for analysis.

## How the Project Works

### 1. Data Generation

The `data_generator.py` script creates simulated manufacturing records by assigning job-level production variables and applying defect logic based on realistic shop conditions.

Examples of modeled relationships include:

- more complex jobs tend to have longer setup times and cycle times
- junior operators may contribute to slightly higher defect rates
- worn tools increase the likelihood of dimensional issues
- rush orders and downtime can increase production risk
- inspection type affects how defects are caught or reduced
- smaller high-complexity jobs are generated differently from larger standard jobs

### 2. Data Analysis

The `analysis.py` script evaluates the generated data using summary statistics and visualizations.

Example analyses include:

- average defect rate by machine
- average defect rate by shift
- total defects by material
- most common defect types
- average production cost by machine
- defect rate by operator level
- defect rate by tool condition
- defect rate by rush order
- defect rate by inspection type
- defect trends by complexity score

### 3. Machine Performance Comparison

The project also compares machines using a weighted performance score based on multiple factors such as:

- defect rate
- production cost
- cycle time

This helps identify which machine provides the best overall operational balance rather than focusing on only one metric.

## Tools Used

- Python
- pandas
- matplotlib
- CSV file handling

## Future Improvements

- build an interactive dashboard in Power BI or Tableau
- add predictive modeling for defect risk
- test classification or regression models on simulated outcomes
- add time-based trends by day, week, or month
- include machine-specific maintenance schedules
- simulate operator learning curves over time
- recommend the best machine setup for a new incoming job
