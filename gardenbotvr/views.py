from django.shortcuts import render, redirect
from .models import Entity, Asset, Scene
from .forms import AssetForm, SceneForm, EntityForm
from django.contrib import messages
from django.views.generic import CreateView




def home(request):
    scenes = Scene.objects.all()
    entities = Entity.objects.all()
    context = {'scenes': scenes, 'entities': entities}
    return render(request, 'index.html', context)


class SceneFormView(CreateView):
    model = Scene
    fields = ['name', 'groundcolor', 'skycolor', 'template', 'assets']
    success_url = '/'


#     def create_collada(request):
#     form = EntityForm(data=request.POST or None)
#     if form.is_valid():
#         threed = form.save(commit=False)
#         threed.save()
#         return redirect('/thanks')
#
#     context = {'form': form}
#     return render(request, 'threedform.html', context)



def scene(request):
    selected = request.POST['plants']
    selected = [int(select) for select in selected.split(',')]

    colladas = Entity.objects.filter(pk__in=selected)
    sceneobjects = Asset.objects.filter()
    selectedmodels = [c.file.url for c in colladas ]

    context = {'colladas': colladas, 'selectedmodels': selectedmodels, 'sceneobjects': sceneobjects}
    return render(request, 'whatever.html', context)