from django.urls import path

from . import views


urlpatterns = [
    path('patient-data',views.patient_data, name="get_patient_data" ),
]