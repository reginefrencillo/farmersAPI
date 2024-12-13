from django.urls import path
from .views import FarmerListCreateView, FarmerDetailView
from . import views


app_name='farmers'
urlpatterns = [
     # API Endpoints for Farmer List & Create
    path('api/farmers/', views.FarmerListCreateView.as_view(), name='farmer_list_create'),

    # API Endpoint for Farmer Detail (Retrieve, Update, Delete)
    path('api/farmers/<int:pk>/', views.FarmerDetailView.as_view(), name='farmer_detail'),

    # Web Form to Add a Farmer
    path('farmers/add/', views.add_farmer, name='add_farmer'),
]
