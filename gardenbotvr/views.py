from django.shortcuts import render
from datetime import datetime
import random
from .models import ThreeD
# Create your views here.
def home(request):
    alligator = [33343329399393, 'sonsonson']
    tiger = 'defefef'
    dog = 5
    now = datetime.now()
    choice = random.choice(alligator)
    colladas = ThreeD.objects.all()
    context = {'todd': alligator, 'jerry': tiger, 20: dog, 'today': now, 'plants': choice, 'colladas': colladas}
    return render(request, 'index.html', context)