# YouTube Video Manager (Python CLI Application)

YouTube Video Manager (Python CLI Application)
About the Project

YouTube Video Manager is a command-line application built using Python that allows users to manage a collection of YouTube videos. The application supports adding, viewing, searching, updating, and deleting video records, with all data stored persistently in a relational database using SQL.

The project focuses on applying core Python concepts alongside database integration to build a practical, real-world CLI tool rather than isolated code examples.

Features

Add YouTube videos with a title and duration

Display all stored videos in a clean, numbered list

Search videos using partial, case-insensitive matching

Update existing video details such as name or duration

Delete videos with confirmation to prevent accidental removal

Persistent data storage using an SQL database

Input validation to handle invalid or unexpected user input gracefully

Tech Stack

Python 3

SQL (SQLite / MySQL, depending on configuration)

Python DB API (sqlite3 or equivalent)

Command Line Interface (CLI)

File Structure
Youtube_Manager.py
database.db
README.md


Youtube_Manager.py – Contains the full application logic and database operations

database.db – SQL database file storing video records

README.md – Project documentation

How to Run

Ensure Python 3 is installed on your system

Clone or download this repository

Open a terminal in the project directory

Run the application:

python Youtube_Manager.py


The database will be created automatically if it does not already exist.

Database Schema

The application uses a simple table to store video records:

CREATE TABLE videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration TEXT NOT NULL
);


Each video is stored as a row in the database, ensuring structured and reliable data management.

What I Learned

Through this project, I strengthened my understanding of:

Python functions and modular program design

SQL fundamentals and database schema design

Performing CRUD operations using SQL from Python

Input validation and error handling in CLI applications

Designing a menu-driven program with persistent storage

Possible Improvements

Add sorting by video name or duration

Display statistics such as total video count and average duration

Introduce a favorites flag for videos

Export video data to CSV

Extend support to multiple users

Author

Kishan

This project was built for learning and hands-on practice with Python and SQL integration.

## Author

Kishan
* This project was created for learning and personal practice.
