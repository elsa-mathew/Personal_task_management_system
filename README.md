Personal Task Management System

Project Overview

The Personal Task Management System is a web-based application developed using Python and Django to help users efficiently organize and manage their daily tasks. The application provides a secure authentication system, allowing users to create an account, log in, and manage their own tasks. Each user can only access the tasks they have created, ensuring data privacy and security.

The system offers features such as task creation, task editing, task deletion, task viewing, task searching, filtering, sorting, dashboard analytics, profile management, and file attachment support. It is designed with a clean and user-friendly interface to provide an intuitive task management experience.

Features

*User Registration
*User Login and Logout
*Secure Authentication
*Create New Tasks
*View Task Details
*Edit Existing Tasks
*Delete Tasks
*Upload File Attachments
*Search Tasks
*Filter Tasks by Status
*Filter Tasks by Priority
*Sort Tasks by Newest, Oldest, Due Date, andPriority
*Dashboard with Task Statistics
*Profile Management
*Change Password
*Pagination (10 tasks per page)
*User-specific Task Management

Technologies Used

Backend

*Python
*Django

Frontend

*HTML5
*CSS3
*JavaScript
*Font Awesome

Database

*PostgreSQL

Tools

*Git
*GitHub
*Visual Studio Code

Project Modules

Authentication Module

*User Registration
*User Login
*User Logout
*Change Password

Dashboard Module

*Displays total tasks
*Displays completed tasks
*Displays pending tasks
*Displays overdue tasks
*isplays upcoming tasks
*Search functionality
*Filter by status
*Filter by priority
*Sort tasks
*Quick task creation

Task Management Module

*Create Task
*View Task Details
*Edit Task
*Delete Task
*Upload Attachments
*Search Tasks
*Filter Tasks
*Pagination

Profile Module

*View Profile
*Edit Profile
*Change Password

Database Design

User

The application uses Django's built-in User model for authentication.

Task

Fields included in the Task model:

*User
*Title
*Description
*Priority
*Status
*Due Date
*File Attachment
*Created Date
*Updated Date

Security Features

*Django Authentication
*Login Required Access
*CSRF Protection
*User-specific Task Access
*Secure Password Storage

Installation

Clone the repository


    git clone https://github.com/yourusername/personal-task-management.git


Navigate to the project directory

    cd PersonalTask


Create a virtual environment

    python -m venv venv


Activate the virtual environment

    venv\Scripts\activate



Install the required packages

    pip install -r requirements.txt


Configure PostgreSQL in settings.py


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'personaltask_db',
            'USER': 'postgres',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


Apply migrations

    python manage.py makemigrations
    python manage.py migrate


Create a superuser

    python manage.py createsuperuser


Run the server

    python manage.py runserver


Open the application in your browser:

    http://127.0.0.1:8000/


Project Structure

PersonalTask/
│
├── authentication/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── task/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── media/
├── static/
├── PersonalTask/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt



PostgreSQL Configuration for Render Deployment

Why the Project Did Not Work on the Live Link ?

The project worked correctly on the local development environment because PostgreSQL was running on the local computer.

The local Django configuration was using:

python
    HOST = "localhost"
    PORT = "5432"


This works when PostgreSQL is installed and running on the same computer as Django.
However, after deploying the project to Render, the application produced the following error:

    OperationalError:
    connection to server at "localhost", port 5432 failed:
    Connection refused


The reason is that localhost on Render refers to the Render web service itself, not the PostgreSQL server running on the developer's local computer.

Therefore, the deployed application could not access the local PostgreSQL database.

Local Database Architecture

During local development, the application worked with the following setup:


Local Computer
    |
    | Django
    |
    | localhost:5432
    |
    v
Local PostgreSQL Database


The PostgreSQL server was running locally, so Django could connect to:

    localhost
    5432


Render Database Architecture

For production deployment, the PostgreSQL database must also be hosted on Render.

The correct architecture is:

Render Web Service
        |
        | DATABASE_URL
        |
        v
Render PostgreSQL Database

The Django application and PostgreSQL database are separate Render services.

Creating PostgreSQL on Render

To create a PostgreSQL database on Render:

    1. Log in to the Render dashboard.

    2. Select:
                New

    3. Select:
                PostgreSQL

    4. Enter a name for the database.

    5. Select the appropriate region.

    6. Create the PostgreSQL database.

It is recommended to use the same region for the PostgreSQL database and Django web service.

Getting the Database Connection URL

After creating the PostgreSQL database:

    1. Open the PostgreSQL service in Render.

    2. Go to the connection details.

    3. Locate the Internal Database URL.

    4. Copy the Internal Database URL.

The URL contains the information Django needs to connect to the PostgreSQL database.

It should have a structure similar to:

postgresql://username:password@hostname/database

The actual URL should not be committed to GitHub because it contains database credentials.

Adding DATABASE_URL to Render

Open the Django Web Service in Render.

Go to:
        Environment

Add a new environment variable:

        Key: DATABASE_URL


Set its value to the Internal Database URL obtained from the Render PostgreSQL service.

The configuration becomes:

DATABASE_URL = <Render PostgreSQL Internal Database URL>


The database URL should be stored as an environment variable rather than directly inside settings.py.

Installing dj-database-url

The Django project uses "dj-database-url" to read the database configuration from the "DATABASE_URL" environment variable.

Install it using:

    pip install dj-database-url

Then update the requirements file:

    pip freeze > requirements.txt


The "requirements.txt" file should contain:

    dj-database-url


along with the other project dependencies.

Django Database Configuration

In "settings.py", import:

python
    import os
    import dj_database_url


Then configure the database using:

python
        DATABASES = {
            "default": dj_database_url.config(
                default=os.environ.get("DATABASE_URL")
            )
        }


This allows Django to obtain the PostgreSQL connection details from the Render environment variable.

The application no longer depends on:

        localhost
        5432

for the production database connection.

Local and Production Configuration

The application uses different database environments.

For local development:

        Django
            |
            v
        Local PostgreSQL
        localhost:5432


For production:


        Django on Render
        |
        v
        DATABASE_URL
        |
        v
        PostgreSQL on Render


This allows the same Django project to work in both environments without hardcoding the production database credentials.

Running Migrations on Render

After connecting the Django application to the Render PostgreSQL database, Django's database tables need to be created.

Open the Render Web Service and use the Shell.

Run:

    python manage.py migrate


This applies all Django migrations to the Render PostgreSQL database.

For example:

        Applying auth migrations
        Applying contenttypes migrations
        Applying sessions migrations
        Applying task migrations


After the migrations complete successfully, the database is ready for the application.


Final Render Deployment Flow

The complete production deployment architecture is:


        User
        |
        v
        Render Live Website
        |
        v
        Django Web Service
        |
        | DATABASE_URL
        |
        v
        Render PostgreSQL
        |
        v
        Task Database


The main issue with the earlier deployment was that Django was attempting:


        Render Django
            |
            v
        localhost:5432
            |
            v
        Local PostgreSQL


The corrected configuration is:


        Render Django
            |
            v
        DATABASE_URL
            |
            v
        Render PostgreSQL


This PostgreSQL configuration was necessary to make the Django application work correctly on the Render live environment.


