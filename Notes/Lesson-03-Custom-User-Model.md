# Lesson 3 -- Custom User Model

## Goal

Build a production-ready custom User model before implementing
authentication APIs.

## Learning Objectives

-   Django built-in User model
-   Why create a custom User model
-   AbstractUser vs AbstractBaseUser
-   Authentication flow
-   Password hashing
-   Configure AUTH_USER_MODEL

## Why Custom User?

Create a custom user model at the start of the project so future
requirements (email login, phone number, profile image, social login)
are easy to support.

## AbstractUser vs AbstractBaseUser

### AbstractUser

``` python
class User(AbstractUser):
    pass
```

-   Extends Django's built-in user
-   Recommended for most projects

### AbstractBaseUser

``` python
class User(AbstractBaseUser):
    ...
```

-   Full customization
-   Requires implementing manager, authentication, permissions and admin
    support

We use **AbstractUser**.

## Authentication Flow

``` text
React
  ↓
Signup API
  ↓
User Model
  ↓
Database

Login
  ↓
Password Verification
  ↓
JWT Token
```

## Password Hashing

Never store plain passwords.

Django stores hashed passwords (e.g. `pbkdf2_sha256...`) and compares
hashes during login.

## User Model

`apps/accounts/models.py`

``` python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
```

## Django Settings

`backend/settings.py`

``` python
AUTH_USER_MODEL = "accounts.User"
```

## Admin Registration

`apps/accounts/admin.py`

``` python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

## Migrations

``` bash
python manage.py makemigrations accounts
python manage.py migrate
```

## Create Superuser

``` bash
python manage.py createsuperuser
python manage.py runserver
```

Open:

    http://127.0.0.1:8000/admin/

## Relationships

Always reference:

``` python
from django.conf import settings

user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
)
```

## Homework

-   Explain AbstractUser
-   Explain AbstractBaseUser
-   Explain password hashing
-   Explain AUTH_USER_MODEL
-   Explain why email is unique

## Next Lesson

-   Custom User Manager
-   Email login
-   USERNAME_FIELD
-   REQUIRED_FIELDS
-   Signup & Login preparation
