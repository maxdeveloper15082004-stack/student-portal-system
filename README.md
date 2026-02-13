# Student Portal System

A Django-based Student Portal application.

## Project Structure

```
student-portal-system/
│
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
│
├── backend/                     🔥 Django Backend
│   ├── manage.py
│   │
│   ├── config/                  ⚙️ Main project config folder
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── apps/                    📦 All Django apps inside one folder
│   │   ├── accounts/
│   │   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │   │
│   │   └── students/            (future app example)
│   │
│   ├── templates/               🎨 All HTML files
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   │
│   ├── static/                  🎨 CSS / JS / Images
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── db.sqlite3
│
└── frontend/ (Optional - Only if React/Next/Vue in future)
```

## Setup

1. Create a virtual environment and activate it:

   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```
   cd backend
   python manage.py migrate
   ```

4. Run server:
   ```
   cd backend
   python manage.py runserver
   ```
