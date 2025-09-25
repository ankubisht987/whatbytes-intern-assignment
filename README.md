# Healthcare Management System

A Django REST API-based healthcare management system that allows users to manage patients, doctors, and their relationships. The system includes authentication, patient-doctor mappings, and secure data access controls.

## 🚀 Features

- **User Authentication**: JWT-based authentication system with user registration and login
- **Patient Management**: Create, read, update, and delete patient records
- **Doctor Management**: Manage doctor profiles with specializations
- **Patient-Doctor Mapping**: Establish relationships between patients and doctors
- **Security**: Custom permissions ensuring users can only access their own patient data
- **RESTful API**: Clean, well-documented API endpoints

## 🛠️ Technology Stack

- **Backend**: Django 5.2.6 + Django REST Framework 3.16.1
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens) with SimpleJWT
- **Environment Management**: python-decouple
- **Additional Libraries**: 
  - TensorFlow/OpenCV for AI/ML capabilities
  - Streamlit for potential web interface
  - Various data science and image processing libraries

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd healthcare_project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your-secret-key-here
   DB_NAME=your-database-name
   DB_USER=your-database-user
   DB_PASSWORD=your-database-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Database Setup**
   ```bash
   # Create database migrations
   python manage.py makemigrations
   
   # Apply migrations
   python manage.py migrate
   
   # Create superuser (optional)
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

## 📚 API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/token/` - Login (obtain JWT tokens)
- `POST /api/token/refresh/` - Refresh JWT tokens

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor
- `GET /api/doctors/{id}/` - Get doctor details
- `PUT /api/doctors/{id}/` - Update doctor
- `DELETE /api/doctors/{id}/` - Delete doctor

### Patients
- `GET /api/patients/` - List user's patients
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient

### Patient-Doctor Mappings
- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Create new mapping
- `GET /api/mappings/{id}/` - Get mapping details
- `DELETE /api/mappings/{id}/` - Delete mapping

## 🔐 Authentication

The API uses JWT authentication. Include the access token in your requests:

```bash
curl -H "Authorization: Bearer your-access-token" http://localhost:8000/api/patients/
```

## 📊 Data Models

### User
- Custom user model extending Django's AbstractUser
- Supports future extensions for healthcare-specific user fields

### Doctor
- `name`: Doctor's name
- `specialization`: Medical specialization

### Patient
- `name`: Patient's name
- `date_of_birth`: Patient's date of birth
- `address`: Patient's address
- `created_by`: User who created the patient record
- `doctors`: Many-to-many relationship with doctors

### PatientDoctorMapping
- Links patients to doctors
- Ensures unique patient-doctor relationships

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Custom Permissions**: Users can only access their own patient records
- **Password Hashing**: Automatic password hashing for user accounts
- **CSRF Protection**: Built-in Django CSRF protection
- **Environment Variables**: Sensitive data stored in environment variables

## 🧪 Testing the API

### Register a new user
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Login
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Create a doctor (with authentication)
```bash
curl -X POST http://localhost:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-access-token" \
  -d '{"name": "Dr. Smith", "specialization": "Cardiology"}'
```

### Create a patient (with authentication)
```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-access-token" \
  -d '{"name": "John Doe", "date_of_birth": "1990-01-01", "address": "123 Main St"}'
```

## 🗂️ Project Structure

```
healthcare_project/
├── api/                          # Main application
│   ├── models.py                 # Database models
│   ├── views.py                  # API views
│   ├── serializers.py            # Data serializers
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Django admin configuration
│   └── migrations/               # Database migrations
├── healthcare_project/           # Django project settings
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Main URL routing
│   └── wsgi.py                   # WSGI configuration
├── venv/                         # Virtual environment
├── requirements.txt              # Python dependencies
├── manage.py                     # Django management script
└── README.md                     # This file
```

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database
4. Configure static file serving
5. Use a production WSGI server like Gunicorn
6. Set up environment variables securely

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions, please open an issue in the repository or contact the development team.

## 🔮 Future Enhancements

- Appointment scheduling system
- Medical record management
- Prescription tracking
- Telemedicine features
- Mobile app integration
- Advanced analytics and reporting
- Integration with external healthcare systems
