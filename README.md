# Containerized Full-Stack Todo Application

A production-ready Todo Management Application built with Python Flask, MySQL, and Nginx, fully containerized with Docker and automated with a CI/CD pipeline using GitHub Actions. Includes Prometheus and Grafana monitoring.

## Services
- Nginx: Reverse proxy on port 80
- Flask: Python web application with full CRUD operations
- MySQL 8.0: Persistent database
- Prometheus: Scrapes metrics from Flask every 15 seconds
- Grafana: Visualizes metrics with dashboards

## Features
- Add, complete, and delete tasks
- Health checks on all containers
- Non-root user execution inside containers
- Secrets managed via .env file
- Multi-stage Dockerfile
- CI/CD pipeline with GitHub Actions
- Real-time monitoring with Prometheus and Grafana

## Access the Services
- Todo App: http://localhost
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin / admin123)

## Quick Start
git clone https://github.com/haseebspaniard/todo-app-docker.git
cd todo-app-docker
cp .env.example .env
docker compose up --build

## Docker Hub
docker pull haseebspaniard/todo-app:latest

## Author
Abdul Haseeb
- GitHub: https://github.com/haseebspaniard
- LinkedIn: https://www.linkedin.com/in/abdulhaseebas
- Medium: https://medium.com/@haseebabdul480
