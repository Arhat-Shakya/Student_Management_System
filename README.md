# 🎓 Student Management System

A Python-based **Student Management System** designed to manage student records, academic subjects, examination marks, attendance, and academic performance reports.

This project uses **Object-Oriented Programming (OOP)** and **JSON file handling** to organize data and maintain records between program executions.

## 🚀 Features

### 1. Student Management
- Register new students.
- Update existing student information.
- Search and view student details using their ID.
- Remove student records.
- Generate unique student IDs.

### 2. Subject Management
- Add subjects to the academic curriculum.
- Update subject names, IDs, and full marks.
- View subject information.
- Remove subjects.

### 3. Examination & Marks Management
- Add examination marks for students across registered subjects.
- Automatically calculate total marks and percentages.
- Assign grades based on percentage.
- Update individual subject marks.
- View and remove examination records.
- Prevent duplicate examination records for the same student.

### 4. Attendance Management
- Record daily student attendance.
- Mark students as present or absent.
- Update attendance records.
- View attendance by date.
- Remove attendance records.
- Calculate individual student attendance percentages.

### 5. Academic Performance & Reports
- Generate class rankings based on examination percentages.
- Calculate individual attendance percentages.
- Display academic performance in descending order.

## 🛠️ Technologies Used

- **Python 3** – Core programming language.
- **JSON** – Data storage and persistence.
- **OOP** – Classes, objects, constructors, and methods.
- **File Handling** – Reading and writing persistent records.
- **Python Standard Library:**
  - `json`
  - `os`
  - `string`
  - `secrets`

## 📂 Project Structure

```text
Student_Management_System/
│
├── student_manage.py
│
├── student.json
├── subject.json
├── exam.json
└── attendence.json
│
└── README.md
```

## ⚙️ How to Run

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Student_Management_System
```

**3. Run the Python program**

```bash
python student_manage.py
```

**4. Select a management system**

The program provides five main sections:

- Student Management
- Subject Management
- Examination and Marks
- Attendance Management
- Academic Reports

Follow the terminal instructions to perform the desired operations.

## 💾 Data Storage

The project uses separate JSON files to store different categories of information.

| JSON File | Purpose |
|---|---|
| `student.json` | Student personal information |
| `subject.json` | Academic subject information |
| `exam.json` | Examination marks and results |
| `attendence.json` | Daily attendance records |

Data is loaded into Python lists and dictionaries when the program starts and written back into JSON files after operations are completed.

This allows records to persist even after the program is closed.

## 📚 Concepts Practiced

This project helped me practice and apply:

- Object-Oriented Programming
- Classes and constructors (`__init__`)
- Methods and object interaction
- Lists and dictionaries
- Loops and conditional statements
- List comprehensions
- Lambda functions and sorting
- File handling
- JSON serialization and deserialization
- Exception handling
- Randomized ID generation using `secrets`

## 🎯 Project Objective

The main objective of this project was to apply Python concepts to a practical, real-world management problem.

Rather than creating isolated programs for individual Python concepts, I wanted to combine them into one system with multiple interconnected functionalities.

This project represents my progress in Python programming, logical problem-solving, and building larger applications using OOP and file handling.

---

**Author:** Arhat

**Language:** Python

**Project Type:** Console-Based Application
