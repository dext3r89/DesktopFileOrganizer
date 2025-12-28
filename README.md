# DesktopFileOrganizer
Python file organizers that are used to decrease file clutter and make file organization easier for everyday life

📁 Python File Organizer

A simple and practical Python-based file organizer designed to help keep directories clean and structured.
This project provides multiple scripts that organize files based on file type or name substrings, making it ideal for downloads folders, project directories, or general file housekeeping.

Built with core Python libraries — lightweight, beginner-friendly, and effective.

🚀 Features

- Organize files by file extension (e.g. .pdf, .jpg, .py)
- Group files by a specific word or substring in the filename
- Interactive command-line input
- Automatically creates folders when needed
- Uses only standard Python libraries (os, shutil)

🛠️ Technologies Used

- Python 3
- os module
- shutil module

No external dependencies required.

📂 Project Structure
File-Organizer/
│
├── FileOrganizer.py        # Automatically sorts files into folders by extension
├── FileGroupByName.py      # Groups files based on a user-defined substring
├── FileGroupByType.py      # Allows user to select a file type to organize
└── README.md

📌 Script Breakdown
1️⃣ FileOrganizer.py — Organize by Extension

Automatically scans a directory and moves files into folders named after their file extensions.

Example:
report.pdf  →  /pdf/report.pdf
image.jpg   →  /jpg/image.jpg

How to run:
python FileOrganizer.py
You’ll be prompted to enter the path of the directory you want to organize.


2️⃣ FileGroupByName.py — Organize by Substring

Groups files based on a keyword or substring found in the filename.

Example:
If you enter assignment, all files containing that word will be moved into an assignment folder.

How to run:
python FileGroupByName.py


3️⃣ FileGroupByType.py — Organize by Selected File Type

Displays all file types in a directory and allows you to choose one specific type to organize.

Example:
1. PDF
2. JPG
3. DOCX

Only the selected type will be moved into its own folder.

How to run:
python FileGroupByType.py


⚠️ Notes & Best Practices

Make sure the directory path you enter exists
Avoid running the scripts in system-critical folders
Files are moved, not copied — double-check before running
The scripts skip folders automatically to prevent recursion issues

🎓 Why This Project?

This project was built to:
- Practice Python file handling
- Understand real-world automation tasks
- Create a practical utility useful for everyday student life
- Demonstrate clean, readable scripting for portfolio use

📈 Future Improvements

- Add a GUI (Tkinter)
- Add logging and undo functionality
- Support organizing into custom categories
- Cross-platform path handling improvements

👤 Author
Kabelo Monnakgotla
