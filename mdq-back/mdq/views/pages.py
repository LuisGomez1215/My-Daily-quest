from datetime import timedelta
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from mdq.forms import PetSelectForm, TaskCreateForm
from mdq.models import (AdventureLocation, Closet, ClosetItem,
                        CurrentAdventure, InventoryItem, Pet,
                        PetType, Inventory, Task, TasksList)


@login_required
def adventure(request):
    user = request.user
    remaining = None
    end_time = None
    progress = 0
    current = getattr(user, "currentadventure", None)

    if request.method == "POST" and not current:
        destination = get_object_or_404(AdventureLocation, id=request.POST.get("destination"))
        CurrentAdventure.objects.create(user=user, destination=destination)
        return redirect("adventure")

    if current:
        duration = timedelta(hours=current.destination.time)
        end_time = current.created_at + duration
        remaining = end_time - now()
        elapsed = (now() - current.created_at).total_seconds()
        total = duration.total_seconds()
        progress = min(100, max(0, (elapsed / total) * 100))

    return render(request, "adventure/adventure.html", {
        "current": current,
        "locations": AdventureLocation.objects.all(),
        "remaining": remaining,
        "end_time": end_time,
        "progress": progress,
    })


@login_required
def complete_adventure(request, current_id):
    """
    testing dev button,
    to instantly finish the adventure and reward the user
    """

    user = request.user
    currentadv = get_object_or_404(CurrentAdventure, id=current_id, user=user)
    destination = currentadv.destination
    pet = user.pet
    wallet = user.wallet

    pet.exp += destination.exp_reward
    pet.save()

    wallet.credits += destination.credit_reward
    wallet.save()

    currentadv.delete()
    return redirect("adventure")


@login_required
def customize(request):
    pet = None
    items = (
        Inventory.objects
        .filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "inventoryitem_set",
                queryset=InventoryItem.objects.select_related("consumable"),
            )
        )
    )
    cosmetics = (
        Closet.objects
        .filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "closetitem_set",
                queryset=ClosetItem.objects.select_related("cosmetic"),
            )
        )
    )

    try:
        pet = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    return render(request,
                'pages/customize.html',
                {'pet': pet,
                'items': items,
                'cosmetics': cosmetics})


@login_required
def customize_equip(request, clo_item_id):
    clo_item = get_object_or_404(ClosetItem, id=clo_item_id, closet__user=request.user)
    cosmetic = clo_item.cosmetic
    closet = clo_item.closet

    if clo_item.equipped:
        clo_item.equipped = False
        clo_item.save()
    else:
        ClosetItem.objects.filter(
            closet=closet,
            cosmetic__slot=cosmetic.slot,
            equipped=True
        ).update(equipped=False)
        clo_item.equipped = True
        clo_item.save()

    return redirect("customize")


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


def settings(request):
    return render(request, 'settings/user_settings.html')


@login_required
def task_select(request):
    tasklist = TasksList.objects.get(user=request.user)
    existing_tasks = Task.objects.filter(custom=False).exclude(
        id__in=tasklist.tasks.all()
    )

    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id, custom=False)
        tasklist.tasks.add(task)
        return redirect("tasklist")

    return render(request, "tasks/task_select.html", {
        "existing_tasks": existing_tasks,
        })


@login_required
def task_create(request):
    tasklist = TasksList.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskCreateForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.custom = True
            task.save()
            tasklist.tasks.add(task)
            return redirect("tasklist")
    else:
        form = TaskCreateForm()

    return render(request, "tasks/new_task.html", {"form": form})


@login_required
def task_list(request):
    tasklist = TasksList.objects.get(user=request.user)

    return render(request, "tasks/tasks.html", {
        "tasks": tasklist.tasks.all(),
    })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, task_lists__user=request.user)
    pet = request.user.pet
    wallet = request.user.wallet

    pet.exp += 5
    pet.save()

    wallet.credits += 100
    wallet.save()

    task.task_lists.remove(request.user.taskslist)
    if task.custom and task.user == request.user:
        task.delete()

    return redirect("tasklist")

def stats(request):
    pet = None

    try:
        pet = Pet.objects.get(user=request.user)
    except Pet.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response
    return render(request, 'pages/stats.html', {'pet': pet})
