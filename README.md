# 🏋️ FitBuddy — AI Fitness Plan Generator

A FastAPI + Gemini + SQLite project that generates a 7-day fitness plan,
nutrition/recovery tips, and an updated plan based on user feedback.

## 1. Create and activate a virtual environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Configure Gemini

Copy `.env.example` to `.env` and put your Gemini API key in:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

## 4. Run

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000

Admin dashboard:

http://127.0.0.1:8000/view-all-users

API documentation:

http://127.0.0.1:8000/docs

## Project structure

```text
FitBuddy/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
├── templates/
│   ├── index.html
│   ├── result.html
│   └── all_users.html
├── static/
│   └── style.css
├── .env.example
├── requirements.txt
└── README.md
```

## Important

This project provides general fitness information and is not a substitute
for advice from a qualified healthcare professional.
