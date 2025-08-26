from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Prefetch, Count

from mdq.forms import MdqUserRegistrationForm
from mdq.models import MdqUser, Pet, Profile


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    pet = None
    petcheck = Pet.objects.filter(user=request.user)

    if petcheck:
        try:
            pet = Pet.objects.get(user=request.user)
        except Pet.DoesNotExist:
            response = render(request, '404.html')
            response.status_code = 404
            return response

    return render(request,  'index.html', {'petcheck': petcheck, 'pet': pet})


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = MdqUserRegistrationForm()
    if request.method == 'POST':
        form = MdqUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Correct login.')
            return redirect('login')

    return render(request, 'registration/register.html', {'form': form})


def termsandconditions(request):
    return render(request, 'registration/tos.html')