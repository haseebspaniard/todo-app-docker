# Containerized Full-Stack Todo Application

A production-ready Todo Management Application built with **Python Flask**, **MySQL**, and **Nginx**, fully containerized with **Docker** and automated with a **CI/CD pipeline** using GitHub Actions. Includes real-time monitoring with **Prometheus** and **Grafana**.

---

## Architecture

```
Browser → Nginx (Port 80) → Flask App (Port 5000) → MySQL (Port 3306)
                                    |
                             Prometheus (Port 9090)
                                    |
                             Grafana (Port 3000)
```

---

## Services

| Container | Image | Role |
|---|---|---|
| todo-nginx | nginx:alpine | Reverse proxy — handles all incoming traffic |
| todo-app | custom (Flask) | Web application — CRUD operations |
| todo-mysql | mysql:8.0 | Database — persistent task storage |
| todo-prometheus | prom/prometheus | Metrics collection — scrapes Flask every 15s |
| todo-grafana | grafana/grafana | Metrics visualization — dashboards |

---

## Features

- Add, complete, and delete tasks
- Live task stats (Total / Completed / Pending)
- Data persists across container restarts via Docker volumes
- Health checks on all 5 containers
- Non-root user execution inside app container
- Secrets managed via `.env` file — never hardcoded
- Multi-stage Dockerfile for optimized image size
- Custom Docker bridge network for container isolation
- CI/CD pipeline: auto build and push to Docker Hub on every push to main
- Real-time HTTP metrics with Prometheus and Grafana

---

## Tech Stack

| Layer | Technology |
|---|---|
| Application | Python 3.11, Flask 3.0, Gunicorn |
| Database | MySQL 8.0 |
| Web Server | Nginx Alpine |
| Monitoring | Prometheus, Grafana, prometheus-flask-exporter |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |

---

## Quick Start

### Prerequisites
- Docker
- Docker Compose

### Run locally

```bash
git clone https://github.com/haseebspaniard/todo-app-docker.git
cd todo-app-docker
cp .env.example .env
# Edit .env with your own values
docker compose up --build
```

### Access the Services

| Service | URL | Credentials |
|---|---|---|
| Todo App | http://localhost | — |
| Prometheus | http://localhost:9090 | — |
| Grafana | http://localhost:3000 | admin / admin123 |

---

## Docker Hub

Pull and run without cloning:

```bash
docker pull haseebspaniard/todo-app:latest
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:

1. Runs code quality checks with flake8
2. Runs Python syntax validation
3. Builds the Docker image
4. Pushes to Docker Hub with version tag and `latest`

---

## Security

- `.env` file excluded from Git via `.gitignore`
- App runs as non-root user (`appuser`) inside container
- Docker Hub credentials stored as GitHub Secrets
- `.env.example` provided as template — no real credentials in repo

---

## Monitoring

Prometheus scrapes metrics from `/metrics` endpoint on the Flask app every 15 seconds.

In Grafana, query `flask_http_request_total` to see all HTTP requests broken down by method, status code, and endpoint.

---

## Project Structure

```
todo-app-docker/
├── app/
│   ├── app.py                  # Flask application
│   ├── requirements.txt        # Python dependencies
│   └── templates/
│       └── index.html          # Frontend UI
├── nginx/
│   └── nginx.conf              # Reverse proxy config
├── mysql/
│   └── init.sql                # Database initialization
├── monitoring/
│   ├── prometheus.yml          # Prometheus scrape config
│   └── grafana/
│       └── provisioning/
│           └── datasources/
│               └── prometheus.yml  # Auto-provisioned data source
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions pipeline
├── Dockerfile                  # Multi-stage build
├── docker-compose.yml          # Full stack orchestration
├── .env.example                # Environment variable template
└── .gitignore
```

---

## Author

**Abdul Haseeb** — Former CS Teacher, now Cloud & DevOps Engineer

- GitHub: [@haseebspaniard](https://github.com/haseebspaniard)
- LinkedIn: [abdulhaseebas](https://www.linkedin.com/in/abdulhaseebas)
- Medium: [@haseebabdul480](https://medium.com/@haseebabdul480)
