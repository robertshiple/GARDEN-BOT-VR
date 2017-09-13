from django.shortcuts import render, redirect
from .models import ThreeD
from .forms import ThreeDForm
from django.contrib import messages
# Create your views here.

def home(request):
    colladas = ThreeD.objects.all()
    context = {'colladas': colladas}
    messages.add_message(request, messages.INFO, 'Hello world.')
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
    selected = request.POST['plants']
    selected = [int(select) for select in selected.split(',')]

    colladas = ThreeD.objects.filter(pk__in=selected)

    selectedmodels = [c.file.url for c in colladas ]

    context = {'colladas': colladas, 'selectedmodels': selectedmodels}
    return render(request, 'whatever.html', context)