Healthcare Backend API
A robust and secure backend API for a healthcare management application, built with Django and Django REST Framework. This service provides a complete solution for user authentication, managing patient and doctor records, and establishing relationships between them.

Table of Contents
Key Features

Technology Stack

Getting Started

Prerequisites

Installation and Setup

API Endpoint Guide

Authentication

Doctors

Patients

Mappings

Usage Workflow

Admin Interface

Key Features ✨
Secure JWT Authentication: State-of-the-art user authentication using djangorestframework-simplejwt.

Complete Patient Management: Full CRUD (Create, Read, Update, Delete) capabilities for patient data.

Complete Doctor Management: Full CRUD capabilities for doctor profiles.

Role-Based Permissions: Users can only access and manage the patient records that they have personally created, ensuring data privacy.

Relational Mapping: A dedicated endpoint to create and manage the many-to-many relationships between patients and doctors.

Scalable Architecture: Built with a clean and organized structure that is easy to extend.

Technology Stack 🛠️
Backend Framework: Django

API Framework: Django REST Framework (DRF)

Database: PostgreSQL

Authentication: JSON Web Tokens (JWT)

Configuration: python-decouple for managing environment variables.

Getting Started 🚀
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python (version 3.8 or higher)

PostgreSQL

A code editor like VS Code

Installation and Setup
Clone the Repository

git clone <your-repository-url>
cd healthcare_project

Create and Activate a Virtual Environment

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install Project Dependencies

pip install -r requirements.txt

Configure Environment Variables
Create a .env file in the project's root directory and populate it with your credentials.

.env example:

SECRET_KEY='your-super-secret-key-goes-here'
DB_NAME='healthcare_db'
DB_USER='your_postgres_username'
DB_PASSWORD='your_postgres_password'
DB_HOST='localhost'
DB_PORT='5432'

Set Up the PostgreSQL Database
You must create the database and user role in PostgreSQL before running the application.

-- Connect to psql as a superuser
CREATE ROLE your_postgres_username WITH LOGIN PASSWORD 'your_postgres_password';
CREATE DATABASE healthcare_db OWNER your_postgres_username;

Apply Database Migrations
This will create the necessary tables in your database.

python manage.py makemigrations api
python manage.py migrate

Launch the Server!

python manage.py runserver

The API is now live and accessible at http://127.0.0.1:8000/.

API Endpoint Guide 📖
All endpoints are prefixed with /api. Authentication is required for all endpoints except for registration and login.

Authentication
Method

Endpoint

Description

POST

/register/

Creates a new user account.

POST

/token/

Logs a user in and returns access/refresh JWT tokens.

POST

/token/refresh/

Provides a new access token using a valid refresh token.

Doctors
Method

Endpoint

Description

GET

/doctors/

Retrieves a list of all doctors.

POST

/doctors/

Creates a new doctor record.

GET

/doctors/<id>/

Retrieves details of a specific doctor.

PUT

/doctors/<id>/

Updates the details of a specific doctor.

DELETE

/doctors/<id>/

Deletes a specific doctor.

Patients
Method

Endpoint

Description

GET

/patients/

Retrieves a list of patients created by the logged-in user.

POST

/patients/

Creates a new patient record, assigned to the logged-in user.

GET

/patients/<id>/

Retrieves a specific patient owned by the user.

PUT

/patients/<id>/

Updates a specific patient owned by the user.

DELETE

/patients/<id>/

Deletes a specific patient owned by the user.

Mappings
Method

Endpoint

Description

POST

/mappings/

Creates a link between a patient and a doctor.

GET

/mappings/<id>/

Retrieves details of a specific mapping.

DELETE

/mappings/<id>/

Deletes a specific patient-doctor mapping.

Usage Workflow 📈
Register: Create an account via the /api/register/ endpoint.

Login: Send your credentials to /api/token/ to receive your JWT access token.

Authorize: For all protected requests, include the token in the Authorization header.

Header Key: Authorization

Header Value: Bearer <your_access_token>

Interact: Make requests to the API endpoints to manage your data.

Admin Interface 🧑‍💻
This project includes a fully functional Django Admin interface for easy data management.

Create a Superuser

python manage.py createsuperuser

Follow the prompts to create your admin account.

Access the Admin Panel
Navigate to http://127.0.0.1:8000/admin/ in your browser and log in with your superuser credentials.
