from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Prefetch, Count

from mdq.forms import PetSelectForm
from mdq.models import MdqUser, Pet, PetType, Profile


def adventure(request):
    return render(request, 'adventure/adventure.html')

def customize(request):
    pet = None

    try:
        pet = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response
    return render(request, 'pages/customize.html', {'pet':pet})

def petselect(request):
    pet = PetType.objects.get(id=1)
    pet2 = PetType.objects.get(id=2)
    pet3 = PetType.objects.get(id=3)

    return render(request, 'pages/pet_select.html',{'pet':pet, 'pet2':pet2, 'pet3':pet3})

def petselectform(request, species_id):
    species = get_object_or_404(PetType, id=species_id)

    if request.method == 'POST':
        form = PetSelectForm(request.POST, species_id=species.id)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.species = species
            pet.save()
            return redirect('index')
    else:
        form = PetSelectForm(species_id=species.id)

    return render(request, 'pages/pet_select_form.html', {'form': form, 'species': species})

def shop(request):
    return render(request, 'pages/shop.html')

def settings(request):
    return render(request, 'settings/user_settings.html')

def tasks(request):
    return render(request, 'tasks/tasks.html')

def stats(request):
    pet = None

    try:
        pet = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response
    return render(request, 'pages/stats.html', {'pet': pet})