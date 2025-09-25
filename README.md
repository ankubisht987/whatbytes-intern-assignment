Healthcare Backend API
A robust backend service for a healthcare application built with Django and Django REST Framework. This API provides functionalities for user management, patient and doctor records, and the mapping between them, all secured with JWT authentication.

Features 🚀
JWT Authentication: Secure user authentication using JSON Web Tokens.

User Registration & Login: Endpoints for creating new user accounts and logging in.

Patient Management: Full CRUD (Create, Read, Update, Delete) operations for patient records.

Doctor Management: Full CRUD operations for doctor records.

Patient-Doctor Mapping: Functionality to link patients with doctors.

Permission Control: Users can only view and manage the patient records they have created.

Technologies Used 🛠️
Backend: Django, Django REST Framework

Database: PostgreSQL

Authentication: djangorestframework-simplejwt

Environment Variables: python-decouple

Setup and Installation
Follow these steps to get the project running locally.

1. Prerequisites
Python 3.8+

PostgreSQL

2. Clone the Repository
Bash

git clone <your-repository-url>
cd healthcare_project
3. Set Up Virtual Environment
Bash

# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
4. Install Dependencies
Bash

pip install -r requirements.txt
5. Configure Environment Variables
Create a .env file in the project root directory. You can copy the example below.

Code snippet

# .env file
SECRET_KEY='your-strong-and-unique-secret-key'
DB_NAME='healthcare_db'
DB_USER='your_db_user'
DB_PASSWORD='your_db_password'
DB_HOST='localhost'
DB_PORT='5432'
6. Set Up the Database
Connect to PostgreSQL and create the database and user role.

SQL

-- Run these commands in psql
CREATE ROLE your_db_user WITH LOGIN PASSWORD 'your_db_password';
CREATE DATABASE healthcare_db OWNER your_db_user;
7. Run Migrations
Apply the database migrations to create the necessary tables.

Bash

python manage.py migrate
8. Run the Server
Start the Django development server.

Bash

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

API Endpoints
All endpoints are prefixed with /api/.

Endpoint	Method	Description	Auth Required
/register/	POST	Register a new user.	No
/token/	POST	Log in to obtain JWT access and refresh tokens.	No
/token/refresh/	POST	Get a new access token using a refresh token.	No
/doctors/	GET, POST	List all doctors or create a new one.	Yes
/doctors/<id>/	GET, PUT, DELETE	Retrieve, update, or delete a specific doctor.	Yes
/patients/	GET, POST	List your patients or create a new one.	Yes
/patients/<id>/	GET, PUT, DELETE	Retrieve, update, or delete one of your patients.	Yes
/mappings/	GET, POST	List all mappings or link a patient to a doctor.	Yes
/mappings/<id>/	GET, DELETE	Retrieve or delete a specific mapping.	Yes

Export to Sheets
Example Usage
Register a user by sending a POST request to /api/register/.

Log in by sending a POST request to /api/token/ with the user's credentials to get an access token.

Access a protected endpoint (e.g., GET /api/patients/) by including the token in the Authorization header:
Authorization: Bearer <your_access_token>
