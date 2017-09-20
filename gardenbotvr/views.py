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



def scene(request, slug):
    # retrieve scene by its name
    scene = Scene.objects.get(slug=slug)
    template_name = scene.template

    # parse the users selected entities
    selected = request.POST['plants']
    selected = [int(select) for select in selected.split(',')]

    # retrieve user selection from the database
    entities = Entity.objects.filter(pk__in=selected)
    entity_data = [{"model": c.file.url} for c in entities]


    # capture the assets on that scene
    sceneobjects = scene.assets.all()

    context = {'entities': entities, 'entity_data': entity_data,
               'sceneobjects': sceneobjects, 'scene': scene}
    return render(request, template_name, context)