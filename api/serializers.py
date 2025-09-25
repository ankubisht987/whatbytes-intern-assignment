from rest_framework import serializers
from .models import User, Patient, Doctor, PatientDoctorMapping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password upon user creation
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'specialization')

class PatientSerializer(serializers.ModelSerializer):
    # Use a read-only field to show the username of the creator
    created_by_username = serializers.ReadOnlyField(source='created_by.username')
    
    class Meta:
        model = Patient
        fields = ('id', 'name', 'date_of_birth', 'address', 'created_by', 'created_by_username')
        # 'created_by' is hidden from the output and set automatically from the request user
        extra_kwargs = {'created_by': {'write_only': True}}

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    # Display names instead of just IDs for better readability
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'patient_name', 'doctor_name')