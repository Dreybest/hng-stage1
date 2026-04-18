# HNG Stage 1 DevOps Task – Personal API

This project is a simple **Personal API** built using Flask as part of the HNG DevOps Stage 1 task.

---

## Base URL

- **Local:**  
  `http://127.0.0.1:5000`

- **Live:**  
  `http://44.209.128.127`

---

## Endpoints

### `GET /`
**Description:** Check if the API is running.

**Response:**
```json
{
  "message": "API is running"
}
```

---

### `GET /health`
**Description:** Health check endpoint.

**Response:**
```json
{
  "message": "healthy"
}
```

---

### `GET /me`
**Description:** Returns personal information.

**Response:**
```json
{
  "name": "Damilare Idowu",
  "email": "aideedrey@gmail.com",
  "github": "https://github.com/Dreybest"
}
```

---

## Run Locally

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate the virtual environment

- **Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

- **Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

---

## Version Control (Git)

If you haven't initialized a repository yet:

```bash
git init
git add .
git commit -m "Initial commit for HNG Stage 1 Personal API"
```

---