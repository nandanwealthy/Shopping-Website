# Lesson 4 -- Email Authentication & Custom User Manager

## Goal

Learn how Django creates users and configure email-based authentication.

## Topics

-   Email login
-   Django Managers
-   Custom User Manager
-   USERNAME_FIELD
-   REQUIRED_FIELDS
-   create_user()
-   create_superuser()

## Why Email?

Modern applications use email because it is unique, memorable, and
useful for password recovery.

## Manager

Every model has a manager.

``` python
Product.objects.all()
```

`objects` communicates with the database.

## Custom User Manager

`apps/accounts/managers.py`

``` python
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)
```

## Update User Model

``` python
USERNAME_FIELD = "email"
REQUIRED_FIELDS = []
objects = UserManager()
```

## Passwords

Always use:

``` python
user.set_password(password)
```

## Test

``` python
User.objects.create_user(
    email="user@example.com",
    password="test1234",
)
```

## Homework

-   Explain USERNAME_FIELD
-   Explain REQUIRED_FIELDS
-   Explain Manager
-   Explain UserManager
-   Explain create_user vs create_superuser

## Next Lesson

Build the Signup API using Django REST Framework.
