# Smart Data Processing System

## 🚀 Overview
A backend RESTful API system built using Flask to process, store, and manage data with full CRUD functionality.

## 🔧 Features
- Create data (POST)
- Fetch data (GET)
- Update data (PUT)
- Delete data (DELETE)
- Input validation and error handling
- Logging for debugging and monitoring

## 🛠 Tech Stack
- Python
- Flask
- SQLite

## 📌 API Endpoints

### 1. Create Data
POST /process

### 2. Get Data
GET /data

### 3. Update Data
PUT /update/<id>

### 4. Delete Data
DELETE /delete/<id>

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py

## 📊 Sample Response

```json
[
  {
    "id": 1,
    "name": "yaswanth",
    "value": 20
  }
]
