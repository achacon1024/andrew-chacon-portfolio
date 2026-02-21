# Artifact 3 – Databases Enhancement

## Overview
This artifact represents the database enhancement of the Grazioso Salvare Animal Shelter Dashboard originally developed in CS 340. The application connects a MongoDB database to a Python Dash interface using a custom CRUD module.

## Enhancement Focus
The primary focus of this enhancement was strengthening the database layer to improve reliability, security, and structured data handling.

Enhancements include:

- Refining the custom CRUD module for clearer query structure
- Validating database connections and handling exceptions more effectively
- Implementing authenticated MongoDB access instead of unsecured default connections
- Managing database users and permissions
- Removing ObjectId fields before passing records to the user interface
- Improving handling of edge cases such as missing fields or invalid data types

## Database Improvements
This enhancement demonstrates practical database implementation within a full-stack application. Rather than executing isolated queries, the project manages structured interactions between MongoDB and the application layer.

Security and authentication were emphasized by configuring database users and requiring credential-based access. Query logic was refined to improve clarity and ensure only necessary data is retrieved.

## Technologies Used
- MongoDB
- PyMongo
- Python
- Dash (Plotly)

## How to Run
1. Ensure MongoDB is installed and running locally.
2. Create the appropriate database user and collection.
3. Import the dataset into MongoDB.
4. Run the dashboard notebook or application file.
5. Access the local server URL displayed in the terminal.
