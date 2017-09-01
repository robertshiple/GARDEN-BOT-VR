from django.shortcuts import render
from datetime import datetime
import random
from .models import ThreeD
# Create your views here.
def home(request):
    colladas = ThreeD.objects.all()
    context = {'colladas': colladas}
    return render(request, 'index.html', context)