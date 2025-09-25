from django.db import models
from django.contrib.auth.models import AbstractUser

# Create a custom User model to allow for future extension
class User(AbstractUser):
    # We can add extra fields here in the future if needed
    pass

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class Patient(models.Model):
    # The user who registered this patient
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    # A patient can see multiple doctors, and a doctor can see multiple patients
    doctors = models.ManyToManyField(Doctor, through='PatientDoctorMapping')

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    """
    This is the "through" model for the many-to-many relationship
    between Patient and Doctor. It allows us to add extra information
    to the relationship in the future if needed.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    class Meta:
        # Ensures a patient cannot be mapped to the same doctor more than once
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"