from django.shortcuts import render, redirect
from .models import ThreeD
from .forms import ThreeDForm
# Create your views here.

def home(request):
    colladas = ThreeD.objects.all()
    context = {'colladas': colladas}
    return render(request, 'index.html', context)

def create_collada(request):

    form = ThreeDForm(data=request.POST or None)
    if form.is_valid():
        threed = form.save(commit=False)
        threed.save()
        return redirect('/thanks')

    context = {'form': form}
    return render(request, 'threedform.html', context)

def scene(request):
    colladas = ThreeD.objects.all()

    selectedmodels = [c.name for c in colladas ]

    context = {'colladas': colladas, 'selectedmodels': selectedmodels}
    return render(request, 'whatever.html', context)