from rest_framework import generics, permissions
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer

# --- Custom Permissions ---
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or view it.
    """
    def has_object_permission(self, request, view, obj):
        # The object's 'created_by' field must match the request's user
        return obj.created_by == request.user

# --- Authentication Views ---
class UserCreateView(generics.CreateAPIView):
    """
    View for user registration.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # Anyone can register

# --- Doctor Views (CRUD) ---
class DoctorListCreateView(generics.ListCreateAPIView):
    """
    View to list all doctors or create a new one.
    Authentication is required.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific doctor.
    Authentication is required.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# --- Patient Views (CRUD with Custom Permissions) ---
class PatientListCreateView(generics.ListCreateAPIView):
    """
    View to list patients created by the current user or create a new one.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the patients
        for the currently authenticated user.
        """
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """
        Assign the current user as the creator of the patient.
        """
        serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a patient instance.
    Only the user who created the patient can perform these actions.
    """
    serializer_class = PatientSerializer
    # Use both IsAuthenticated and our custom IsOwner permission
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        """
        Ensure users can only access their own patient objects.
        """
        return Patient.objects.filter(created_by=self.request.user)

# --- Patient-Doctor Mapping Views ---
class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    """
    View to list patient-doctor mappings or create a new one.
    """
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        Optionally, you could filter this to only show mappings related
        to the current user's patients, but for simplicity, we show all.
        """
        return PatientDoctorMapping.objects.all()


class PatientDoctorMappingDetailView(generics.RetrieveDestroyAPIView):
    """
    View to retrieve or delete a patient-doctor mapping.
    (Update is not typically needed for a simple mapping).
    """
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]