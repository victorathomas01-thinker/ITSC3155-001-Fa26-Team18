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

See [requirements traceability](docs/REQUIREMENTS_TRACEABILITY.md) for all eight staff and seven customer functionality questions. The filled professor-template spreadsheets are supplied separately for Canvas submission; GitHub-readable versions are in [Product Backlog](docs/PRODUCT_BACKLOG.md) and [User Stories with Acceptance Criteria](docs/USER_STORIES.md). Priorities, story points and sprint assignments are draft estimates until approved by the group.

**Important:** The starter skeleton is not the completed restaurant API. The backlog and user stories describe work the group still needs to implement.

## November 2026 TA submission corrections

Elijah Jones requested that the product backlog and user stories also be stored in the course team Google Drive folder and that the final-project attendance-log dates be corrected to actual class dates before the group replies to confirm completion. His Canvas comment names **Team17**, although this repository and his attendance email say **Team18**. See the [TA correction checklist](docs/TA_SUBMISSION_CORRECTIONS.md) for the exact requests, source-document links, and unresolved actions. **Neither a Drive upload nor an attendance-date correction has been confirmed just by adding this checklist.**

## Shared Google Drive deliverables

The group's shared folder is [ITSC3155-001-Fa26-Team18](https://drive.google.com/drive/folders/1i6folBxKi0tPjLkSZ_BWoZdFpbLO8ydv). Existing course-format planning spreadsheets are:

- [Product Backlog (Google Sheets)](https://docs.google.com/spreadsheets/d/1P_nlTGsS7w6WuGONDBe5mBSRUS8-29lz0Wt3BWqWbPI/edit)
- [User Stories (Google Sheets)](https://docs.google.com/spreadsheets/d/1uzWiHTu5QqZx0JWaxpNe2GN1yB5FGH4wp2QmPI5VWyQ/edit)
- [Sprint Backlog (Google Sheets)](https://docs.google.com/spreadsheets/d/1Xh8OHZX6PqycxhD6w2Z69WPOwJHFp4rtIOeOsTLl3J8/edit)
- [Attendance Log (Google Sheets)](https://docs.google.com/spreadsheets/d/1D5av7iikflAe_fO7YfqbMVjsMBTg8VYjPmoSQ_oEy9E/edit)

The Google Sheets are the group's shared submission-facing documents; the Markdown files in `docs/` are expanded draft planning references and may not have identical story counts, sprint assignments, or estimates. Coordinate any changes to shared backlog priorities with the team before treating a GitHub draft as final.

**Attendance:** Use the **Attendance Log (Fall Dates)** tab for the Fall 2026 project. Verify class dates and group-meeting dates against the course schedule and meeting records, then record actual attendance; do not infer attendance from the calendar. The Spring tab remains untouched as an archive/template.

## Group setup

The repository owner should invite group members, the professor and TAs at **Settings → Collaborators and teams → Add people**, using the GitHub usernames supplied by the course. Invited members must accept their invitations. Each member should clone the repository and make their own commits.

Use conventional commit messages, such as `feat: add menu CRUD`, `test: cover guest orders`, and `docs: clarify API examples`.

## Setup verified by Martha Corona-Carballo
