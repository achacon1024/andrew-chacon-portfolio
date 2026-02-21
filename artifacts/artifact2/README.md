# Artifact 2 – Algorithms & Data Structures Enhancement

## Overview
This artifact represents the algorithms and data structures enhancement of the Grazioso Salvare Animal Shelter Dashboard originally developed in CS 340.

## Enhancement Focus
The primary focus of this enhancement was improving algorithmic efficiency and structured data handling within the application.

Enhancements include:

- Reducing repeated MongoDB queries by leveraging in-memory data structures
- Utilizing Pandas DataFrames for structured data manipulation
- Improving filtering logic to minimize unnecessary computation
- Implementing controlled Dash callbacks to streamline data flow between components
- Optimizing database queries to return only required records

## Algorithmic Improvements
Rather than querying the database for each user interaction, the application now uses structured in-memory data representations to handle filtering and transformations. This reduces execution time and improves responsiveness, particularly when working with larger datasets.

The use of dictionaries for MongoDB queries and DataFrames for data processing demonstrates intentional data structure selection based on performance and maintainability tradeoffs.

## Technologies Used
- Python
- Dash (Plotly)
- MongoDB
- PyMongo
- Pandas

## How to Run
1. Ensure MongoDB is running locally.
2. Confirm the dataset is imported into the database.
3. Run the dashboard notebook or application file.
4. Access the local server URL displayed in the terminal.
