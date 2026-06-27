# Lesson 2 -- Project Structure, PostgreSQL & Django REST Framework

## Goal

By the end of this lesson you will:

-   Understand why PostgreSQL is preferred over SQLite
-   Install and configure PostgreSQL
-   Connect Django to PostgreSQL
-   Learn what a Django App is
-   Create a production-ready project structure
-   Configure Django REST Framework
-   Understand migrations
-   Create your first app (`accounts`)

------------------------------------------------------------------------

# 1. Why PostgreSQL?

SQLite is a file-based database:

``` text
db.sqlite3
```

Advantages:

-   Easy setup
-   No installation
-   Good for small projects

Disadvantages:

-   Limited concurrency
-   Less scalable
-   Fewer advanced database features

Production projects commonly use PostgreSQL.

------------------------------------------------------------------------

# 2. Install PostgreSQL

## macOS

``` bash
brew install postgresql@16
brew services start postgresql@16
psql --version
```

------------------------------------------------------------------------

# 3. Create a Database

``` bash
psql postgres
```

``` sql
CREATE DATABASE shopping_db;
```

List databases:

``` sql
\l
```

Exit:

``` sql
\q
```

------------------------------------------------------------------------

# 4. Configure Environment Variables

Create/update `.env`:

``` env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=shopping_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Never hardcode secrets in source code.

------------------------------------------------------------------------

# 5. Configure Django

Import:

``` python
from decouple import config
```

Update settings:

``` python
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
```

Database configuration:

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}
```

Run migrations:

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

# 6. What is a Django App?

A Django project is composed of multiple apps.

Example:

``` text
Shopping Project
│
├── Accounts
├── Products
├── Cart
├── Orders
└── Addresses
```

Each app should have one responsibility.

------------------------------------------------------------------------

# 7. Production Folder Structure

``` text
shopping-backend/
│
├── backend/
├── apps/
│   └── accounts/
├── manage.py
└── requirements.txt
```

Create:

``` bash
mkdir apps
mkdir -p apps/accounts
python manage.py startapp accounts apps/accounts
```

------------------------------------------------------------------------

# 8. Important Files

-   `models.py` → Database models
-   `views.py` → Business logic
-   `admin.py` → Django Admin registration
-   `migrations/` → Database schema history

------------------------------------------------------------------------

# 9. Register the App

Create:

``` text
apps/__init__.py
```

Update `INSTALLED_APPS`:

``` python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "apps.accounts",
]
```

------------------------------------------------------------------------

# 10. Configure Django REST Framework

``` python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}
```

------------------------------------------------------------------------

# 11. Understanding Migrations

Flow:

``` text
Python Model
      ↓
makemigrations
      ↓
Migration File
      ↓
migrate
      ↓
SQL
      ↓
PostgreSQL
```

Commands:

``` bash
python manage.py makemigrations
python manage.py migrate
```

------------------------------------------------------------------------

# Homework Checklist

-   [x] Explain why PostgreSQL is preferred.
-   [x] Explain the purpose of `.env`.
-   [x] Explain what a Django App is.
-   [x] Explain `makemigrations` vs `migrate`.
-   [x] Configure Django REST Framework.

------------------------------------------------------------------------

# Next Lesson

Lesson 3:

-   Custom User Model
-   Why Django recommends creating it before any other models
-   Authentication architecture
-   Preparing for Signup and Login APIs
