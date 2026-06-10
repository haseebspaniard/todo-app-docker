# Containerized Full-Stack Todo Application

A production-ready Todo Management Application built with Python Flask, MySQL, and Nginx, fully containerized with Docker and automated with a CI/CD pipeline using GitHub Actions.

## Architecture

Browser -> Nginx (Port 80) -> Flask App (Port 5000) -> MySQL (Port 3306)

- Nginx: Reverse proxy, handles all incoming HTTP traffic
- Flask: Python web application with full CRUD operations  
- MySQL 8.0: Persistent database with initialization scripts
- Docker Compose: Orchestrates all 3 containers on a custom network

## Features

- Add, complete, and delete tasks
- Live task stats (Total / Completed / Pending)
- Data persists across container restarts via Docker volumes
- Health checks on all containers
- Non-root user execution inside containers
- Secrets managed via .env file, never hardcoded
- Multi-stage Dockerfile for optimized image size
- CI/CD pipeline: auto build and push to Docker Hub on every push

## Tech Stack

- Application: Python 3.11, Flask 3.0, Gunicorn
- Database: MySQL 8.0
- Web Server: Nginx Alpine
- Containerization: Docker, Docker Compose
- CI/CD: GitHub Actions
- Registry: Docker Hub

## Quick Start

Prerequisites: Docker and Docker Compose

git clone https://github.com/haseebspaniard/todo-app-docker.git
cd todo-app-docker
cp .env.example .env
docker compose up --build

Open http://localhost in your browser.

## Docker Hub

docker pull haseebspaniard/todo-app:latest

## CI/CD Pipeline

Every push to main branch automatically:
1. Runs code quality checks with flake8
2. Runs syntax validation
3. Builds the Docker image
4. Pushes to Docker Hub with version tag and latest

## Author

Abdul Haseeb
- GitHub: https://github.com/haseebspaniard
- LinkedIn: https://www.linkedin.com/in/abdulhaseebas
- Medium: https://medium.com/@haseebabdul480
