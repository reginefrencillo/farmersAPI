from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Farmer
from farmers.serializers import FarmerSerializer
from .forms import FarmerForm

# API View to List and Create Farmers
class FarmerListCreateView(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

# API View for Fetching, Updating, and Deleting a Farmer
class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer



def add_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmer added successfully!')
            return redirect('farmers:add_farmer')  # Redirect to the same page to show the success message

    else:
        form = FarmerForm()
    return render(request, 'farmers/add_farmer.html', {'form': form})
