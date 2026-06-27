# Lesson 1 -- Django Shopping Backend Setup

## Course Goal

Build a production-style Shopping Backend using **Django + Django REST
Framework + PostgreSQL**, with React as the frontend.

------------------------------------------------------------------------

## Learning Objectives

By the end of this lesson you should understand:

-   What Django is
-   How Django projects are organized
-   What `manage.py` does
-   What a Django app is
-   How virtual environments work
-   How to install Django and Django REST Framework
-   Why `requirements.txt`, `.gitignore`, and `.env` exist
-   How to start the Django development server

------------------------------------------------------------------------

# Step 1: Create the Project Folder

``` bash
mkdir shopping-backend
cd shopping-backend
```

Project structure:

``` text
shopping-backend/
```

------------------------------------------------------------------------

# Step 2: Create a Virtual Environment

### macOS/Linux

``` bash
python3 -m venv venv
```

### Windows

``` bash
python -m venv venv
```

A virtual environment isolates project dependencies so different
projects can use different package versions.

------------------------------------------------------------------------

# Step 3: Activate the Virtual Environment

### macOS/Linux

``` bash
source venv/bin/activate
```

### Windows

``` bash
venv\Scripts\activate
```

Your terminal should show `(venv)`.

------------------------------------------------------------------------

# Step 4: Install Required Packages

``` bash
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install python-decouple
pip install Pillow
pip install django-filter
pip install djangorestframework-simplejwt
```

## Why?

  Package               Purpose
  --------------------- ----------------------------
  Django                Web framework
  djangorestframework   REST APIs
  psycopg2-binary       PostgreSQL driver
  python-decouple       Read environment variables
  Pillow                Image uploads
  django-filter         Filtering
  simplejwt             JWT authentication

------------------------------------------------------------------------

# Step 5: Save Dependencies

``` bash
pip freeze > requirements.txt
```

Anyone can recreate the environment:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Step 6: Create the Django Project

``` bash
django-admin startproject backend .
```

Project structure:

``` text
shopping-backend/
│
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── venv/
```

------------------------------------------------------------------------

# Step 7: Understand the Files

## manage.py

Command-line entry point for Django.

Common commands:

``` bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```

## backend/settings.py

Contains project configuration:

-   Installed apps
-   Database
-   Middleware
-   Static & media files
-   Security
-   Time zone

## backend/urls.py

Main URL router.

Initially:

``` python
urlpatterns = [
    path("admin/", admin.site.urls),
]
```

Later it will include APIs like:

-   `/api/auth/`
-   `/api/products/`
-   `/api/cart/`
-   `/api/orders/`

## backend/wsgi.py

Used for traditional deployment servers.

## backend/asgi.py

Used for async servers and WebSockets.

------------------------------------------------------------------------

# Step 8: Run the Development Server

``` bash
python manage.py runserver
```

Open:

    http://127.0.0.1:8000/

You should see the Django welcome page.

------------------------------------------------------------------------

# Step 9: Create a .gitignore

``` gitignore
venv/
__pycache__/
*.pyc
db.sqlite3
.env
media/
```

------------------------------------------------------------------------

# Step 10: Create a .env File

``` env
SECRET_KEY=replace-with-a-random-secret-key
DEBUG=True
```

We'll add database credentials in Lesson 2.

------------------------------------------------------------------------

# Final Project Structure

``` text
shopping-backend/
│
├── backend/
├── venv/
├── manage.py
├── requirements.txt
├── .gitignore
└── .env
```

------------------------------------------------------------------------

# Homework Checklist

-   [x] Create a virtual environment
-   [x] Activate and deactivate it
-   [x] Install packages
-   [x] Understand `manage.py`
-   [x] Understand `settings.py`
-   [x] Understand `urls.py`
-   [x] Run the development server
-   [x] Understand `.env`, `.gitignore`, and `requirements.txt`

------------------------------------------------------------------------

# Next Lesson

Lesson 2 covers:

-   PostgreSQL configuration
-   Creating Django apps
-   Django REST Framework setup
-   JWT authentication setup
-   Understanding migrations
-   Production-ready project structure
