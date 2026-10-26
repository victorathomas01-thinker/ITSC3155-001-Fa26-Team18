# ITSC 3155 — Team 18 Final Project

**Project:** Online Restaurant Ordering System (OROS)  
**Course:** ITSC 3155-001, Fall 2026  
**Scope:** REST API only (no frontend needed). FastAPI provides an interactive Swagger UI.

This repository started from the professor's [official FinalProject code skeleton](https://github.com/samfallahian/ITSC3155-Assignments/tree/main/FinalProject), with all source files imported into the repository root.

## Clone the project

```bash
git clone https://github.com/victorathomas01-thinker/ITSC3155-001-Fa26-Team18.git
cd ITSC3155-001-Fa26-Team18
```

## Create a virtual environment

On Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Configure MySQL

The professor's starter uses a **local MySQL database**, so the server does not work until MySQL is running and the database exists.

Run in MySQL:

```sql
CREATE DATABASE IF NOT EXISTS sandwich_maker_api;
```

The *unmodified instructor skeleton* expects the development connection in `api/dependencies/config.py`: `localhost:3306`, user `root`, password `rootroot`, schema `sandwich_maker_api`. These are sample local settings, **not production credentials**. If your local MySQL details differ, configure them privately; do not commit your own passwords to Git.

## Run the API and test

```bash
uvicorn api.main:app --reload
```

Then open http://127.0.0.1:8000/docs to try the API. The sample includes `/orders/` and `/orderdetails/` routes.

In another terminal with the virtual environment activated:

```bash
python -m pytest -q
```

A [GitHub Actions smoke test](.github/workflows/ci.yml) also starts a disposable MySQL service, installs dependencies, runs pytest, and checks FastAPI/Swagger routes on pushes and pull requests. Green checks on GitHub are the best way to confirm that automation actually ran.

## Project planning

See [requirements traceability](docs/REQUIREMENTS_TRACEABILITY.md) for a quick map to all eight staff and seven customer functionality questions. The separately prepared submission workbooks are `Team18_Product_Backlog.xlsx` and `Team18_User_Stories.xlsx`.

**Important:** The starter skeleton is not the completed restaurant API. The backlog and user stories describe work the group still needs to implement.

## Group setup

The repository owner should invite group members, the professor and TAs at **Settings → Collaborators and teams → Add people**, using the GitHub usernames supplied by the course. Invited members must accept their invitations. Each member should clone the repository and make their own commits.

Use conventional commit messages, such as `feat: add menu CRUD`, `test: cover guest orders`, and `docs: clarify API examples`.
