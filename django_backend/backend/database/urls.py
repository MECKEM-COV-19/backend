from django.urls import path

from . import views


urlpatterns = [
    path('patient-data/',views.patient_data, name="patient_data" ),
    path('daily-data',views.daily_data, name="daily_data"),
    
]