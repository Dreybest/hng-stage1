# HNG Stage 1 DevOps Task - Personal API

This is a simple Personal API built with Flask for the HNG DevOps Stage 1 task.

## Base URL

Local:
`http://127.0.0.1:5000`

Live:
`Add your live deployment URL here after deployment`

## Endpoints

### GET /

Response:
```json
{
  "message": "API is running"
}

#### GET /health

Response:
```json

{
  "message": "healthy"
}

### GET /me
Response:
```json

{
  "name": "Damilare Idowu",
  "email": "aideedrey@gmail.com",
  "github": "https://github.com/Dreybest"
}

### Run Locally
1. Create a virtual environment:

```bash
python -m venv venv

2. Activate it:

```bash
source venv/Scripts/activate
Install dependencies:
pip install -r requirements.txt
Run the app:
python app.py

**After that, push to GitHub**

If you haven’t created the repo yet, the normal commands will be:

```bash
git init
git add .
git commit -m "Initial commit for HNG Stage 1 personal API"