# YouTube Video Manager (Python CLI Application)

## About the Project

This project is a simple command-line application built using Python that helps manage a list of YouTube videos.
It allows users to add, view, search, update, and delete video entries, with all data saved permanently using a JSON file.

The goal of this project was to practice core Python concepts by building something practical instead of just writing isolated examples.

---

## What This App Can Do

* Add YouTube videos with a name and duration
* Display all saved videos in a clean, numbered list
* Search videos using partial names (case-insensitive)
* Update video details such as name or length
* Delete videos with confirmation to avoid mistakes
* Store data persistently using a JSON file
* Handle invalid inputs without crashing

---

## Tech Stack

* Python 3
* JSON for data storage
* Command Line Interface (CLI)

---

## File Structure

```
Youtube_Manager.py
youtube.txt
README.md
```

* `Youtube_Manager.py` contains the full application logic
* `youtube.txt` stores video data in JSON format
* `README.md` explains the project

---

## How to Run

1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open a terminal in the project directory
4. Run the program using:

   ```
   python Youtube_Manager.py
   ```

---

## Data Storage Format

Videos are stored as a list of dictionaries in a JSON file:

```json
[
    {
        "Name": "Python Tutorial",
        "Length": "10:30"
    },
    {
        "Name": "Data Structures Basics",
        "Length": "15:45"
    }
]
```

---

## What I Learned

While building this project, I improved my understanding of:

* Python functions and modular code structure
* Lists and dictionaries for managing structured data
* File handling and JSON serialization
* User input validation and error handling
* Designing a menu-driven CLI application

---

## Possible Improvements

* Sort videos by name or duration
* Show basic statistics like total videos and average length
* Mark videos as favorites
* Export video data to CSV
* Use unique IDs instead of list index

---

## Author

Kishan
* This project was created for learning and personal practice.
