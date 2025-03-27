# Mental Health in Tech Dashboard

![view HOSTED Streamlit HERE](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)


An interactive dashboard analyzing mental health trends in the tech industry, deployed using Streamlit.

## Project Overview

This project involved multiple steps to clean, process, and analyze mental health survey data before deploying it as an interactive dashboard.

## Project Steps

### 1. Data Inspection
- Viewed shape of the dataset
- Examined all columns across data frames

### 2. Data Cleaning
- Processed each column:
  - Stripped HTML tags and unnecessary characters
  - Checked for null values
  - Identified columns with >45 missing values

### 3. Feature Engineering
- Categorized columns
- Kept only columns appearing in ≤3 data frames
- Joined all data frames by columns
- Renamed columns for clarity
- Performed final dataset refinement

### 4. Data Encoding
- Mapped company size categories to numerical values
- Label encoded categorical columns
- Converted binary columns to integer format

### 5. Exploratory Data Analysis (EDA)
- Conducted comprehensive analysis
- Generated visualizations
- Identified key trends and patterns

### 6. Dashboard Development
- Built interactive visualizations
- Implemented filtering functionality
- Designed user interface

## Deployment

The project was successfully deployed using Streamlit and made accessible on the Streamlit Community platform.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](your-streamlit-app-link-here)

## Features
- Interactive filters for demographic slicing
- Trend analysis by country and year
- Mental health prevalence visualization
- Industry support metrics

## Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Plotly
