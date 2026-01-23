# YouTube Video Manager (Python CLI Application)

## About the Project
YouTube Video Manager is a command-line application built using Python that allows users to manage a collection of YouTube videos. The application supports adding, viewing, searching, updating, and deleting video records, with all data stored persistently in a relational database using SQLite.

This project focuses on applying core Python concepts along with database integration.

---

## Features
- Add YouTube videos with title and duration. 
- View all stored videos in a clean, numbered list.  
- Search videos using partial, case-insensitive matching.  
- Update existing video details.  
- Delete videos with confirmation to prevent accidental removal.  
- Persistent storage using an SQLite database.  
- Graceful handling of invalid user inputs.  

---

## Tech Stack
- Python 3  
- SQL (Database)  
- Python DB API (`sqlite3`)  
- Command Line Interface (CLI)  

---

## Project Structure

- **Youtube_Manager.py** – Core application logic and database operations  
- **database.db** – SQL database storing video records  
- **README.md** – Project documentation  

---

## How to Run
1. Make sure Python 3 is installed  
2. Clone or download this repository  
3. Open a terminal in the project directory  
4. Run the application:
   ```bash
   python Youtube_Manager.py

---


## Database Schema

The application uses a simple table structure:

```python
def add_video(name, duration):
    cursor.execute(
        "INSERT INTO videos (name, duration) VALUES (?, ?)",
        (name, duration)
    )
    conn.commit()

___


## What I Learned

- Building CRUD operations using SQLite and Python’s DB API.
- Designing and interacting with a relational database.
- Handling user input safely to prevent invalid data and crashes.
- Structuring a clean and functional CLI workflow.
- Organizing a small project with separate logic and database layers.