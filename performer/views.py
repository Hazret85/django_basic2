from django.shortcuts import render
from .models import PerformerProfile

def profile(request):
    profiles = PerformerProfile.objects.all()
    return render(request, 'performer/profile.html', {'profiles': profiles})
