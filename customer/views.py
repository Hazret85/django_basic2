from django.shortcuts import render
from .models import CustomerProfile

def profile(request):
    profiles = CustomerProfile.objects.all()
    return render(request, 'customer/profile.html', {'profiles': profiles})
