
# 🖥️ System Check – System Utility Web App

A full-stack system utility web application built with **React** and **FastAPI**, designed to monitor and display system metrics in real-time. This project provides a sleek, responsive dashboard for visualizing key system health parameters such as machine information, antivirus logs, and overall resource usage.

---

## 🚀 Features

- ✅ Real-time system metrics monitoring (CPU, memory, disk, etc.)
- 🧠 Antivirus and machine logs display
- 📊 Interactive dashboard built with React and Tailwind CSS
- ⚡ RESTful API backend using FastAPI
- 🗃️ Lightweight data storage with SQLite3
- 📈 Data visualization through responsive tables and graphs

---

## 🛠️ Tech Stack

| Frontend        | Backend       | Styling        | Database   |
|-----------------|---------------|----------------|------------|
| React.js        | FastAPI       | Tailwind CSS   | SQLite3    |

---

## 📸 Screenshots

> _Add your screenshots here for visual preview (dashboard view, table, graphs, etc.)_

---

## 📂 Project Structure (Suggested)

```
System_check/
├── backend/
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── database.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── ...
│   └── public/
├── reports.db
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/krishnaistherealtruth/System_check.git
cd System_check
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

### 4. Access the App

- Backend API: `http://localhost:8000`
- Frontend Dashboard: `http://localhost:5173` (or as displayed by Vite)

---

## 📬 API Endpoints

| Method | Endpoint           | Description                           |
|--------|--------------------|---------------------------------------|
| POST   | `/report`          | Submit new system report              |
| GET    | `/report`          | Get all reports                       |
| GET    | `/filter/{os}`     | Filter reports by operating system    |
| GET    | `/machines`        | List all machines                     |
| GET    | `/export/csv`      | Export all data to CSV                |
| GET    | `/`                | Root endpoint                         |

---

## 📦 Requirements

- Python 3.8+
- Node.js 16+
- pip, npm
- OS: Windows/Linux

---

## 👨‍💻 Author

**Krishna Singh**  
[GitHub](https://github.com/krishnaistherealtruth)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---
