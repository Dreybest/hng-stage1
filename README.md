# HNG Stage 1 DevOps Task - Personal API

This project is a simple Personal API built with Flask for the HNG DevOps Stage 1 task. It provides three JSON endpoints and is deployed on an AWS EC2 Ubuntu server using Gunicorn, Nginx reverse proxy, and systemd.

## Base URLs

Local:
`http://127.0.0.1:5000`

Live:
`http://44.209.128.127`

## Endpoints

### `GET /`

Returns:

```json
{
  "message": "API is running"
}
```

Live endpoint:
`http://44.209.128.127/`

### `GET /health`

Returns:

```json
{
  "message": "healthy"
}
```

Live endpoint:
`http://44.209.128.127/health`

### `GET /me`

Returns:

```json
{
  "name": "Damilare Idowu",
  "email": "aideedrey@gmail.com",
  "github": "https://github.com/Dreybest/hng-stage1"
}
```

Live endpoint:
`http://44.209.128.127/me`

## Run Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows Git Bash:

```bash
source venv/Scripts/activate
```

Activate the virtual environment on Linux or macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## Deployment Summary

The application is deployed on an AWS EC2 Ubuntu server.

- The Flask app runs with Gunicorn on `127.0.0.1:5000`
- Nginx serves as a reverse proxy on port `80`
- systemd keeps the service running persistently

## Repository

GitHub repository:
`https://github.com/Dreybest/hng-stage1`
