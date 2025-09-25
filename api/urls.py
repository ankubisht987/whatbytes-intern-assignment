from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # --- Authentication Endpoints ---
    path('register/', views.UserCreateView.as_view(), name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # --- Doctor Endpoints ---
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),

    # --- Patient Endpoints ---
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),

    # --- Mapping Endpoints ---
    path('mappings/', views.PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', views.PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]