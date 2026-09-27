<div align="center">

# Blog API — FastAPI Backend

**Production-ready REST API** for a blog platform — built with FastAPI, PostgreSQL, and async Python.

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

</div>

## Features

- **Auth** — JWT-based registration & login
- **Posts** — Full CRUD with pagination & search
- **Comments** — Nested comments on posts
- **Users** — Profile management, role-based access
- **Tests** — pytest with 90%+ coverage

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 + Alembic |
| Database | PostgreSQL |
| Auth | JWT (python-jose + passlib) |
| Testing | pytest + httpx |
| Deploy | Docker + docker-compose |

## Quick Start

```bash
git clone https://github.com/FlourishP/fastapi-blog-api.git
cd fastapi-blog-api
docker-compose up -d
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

## API Endpoints

```
POST   /api/auth/register
POST   /api/auth/login
GET    /api/posts          (paginated, searchable)
POST   /api/posts          (auth required)
GET    /api/posts/:id
PUT    /api/posts/:id      (owner only)
DELETE /api/posts/:id      (owner/admin)
POST   /api/posts/:id/comments
GET    /api/users/:id
```

## License

MIT
