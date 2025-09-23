# views.py
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from collections import defaultdict
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from mdq.models import (
    AdventureLocation,
    Closet,
    ClosetItem,
    Consumable,
    Cosmetic,
    CreditPurchase,
    CurrentAdventure,
    Inventory,
    InventoryItem,
    PetType,
    Pet,
    ShopItem,
    Task,
    TasksList,
)
from mdq.serializers import (
    AdventureLocationSerializer,
    ClosetItemSerializer,
    CreditPurchaseSerializer,
    CurrentAdventureSerializer,
    InventoryItemSerializer,
    PetTypeSerializer,
    PetSerializer,
    PetSelectionSerializer,
    ShopItemSerializer,
    TaskCreateSerializer,
    TaskSerializer,
    TasksListSerializer,
)


class PetTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer

    @action(detail=True, methods=["post"])
    def select(self, request, pk=None):
        species = self.get_object()

        if Pet.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "PET_EXISTS"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = PetSelectionSerializer(
            data=request.data, context={"request": request, "species": species}
        )
        serializer.is_valid(raise_exception=True)
        pet = serializer.save()
        return Response(PetSerializer(pet).data, status=status.HTTP_201_CREATED)


class PetViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            pet = Pet.objects.get(user=request.user)
            return Response(PetSerializer(pet).data)
        except Pet.DoesNotExist:
            return Response(
                {"petcheck": False, "detail": "NO_PET"},
                status=status.HTTP_404_NOT_FOUND,
            )


class TaskSelectAPIView(generics.GenericAPIView):
    serializer_class = TaskSerializer

    def get(self, request):
        tasklist = TasksList.objects.get(user=request.user)
        existing_tasks = Task.objects.filter(custom=False).exclude(
            id__in=tasklist.tasks.values_list("id", flat=True)
        )
        return Response(TaskSerializer(existing_tasks, many=True).data)

    def post(self, request):
        tasklist = TasksList.objects.get(user=request.user)
        task_id = request.data.get("task_id")
        task = get_object_or_404(Task, id=task_id, custom=False)

        if tasklist.tasks.filter(id=task_id).exists():
            return Response(
                {"detail": "task_exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tasklist.tasks.add(task)
        return Response({"detail": "task_added"}, status=status.HTTP_201_CREATED)


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, custom=True)


class TaskCompleteAPIView(generics.GenericAPIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, task_lists__user=request.user)
        pet = request.user.pet
        wallet = request.user.wallet
        pet.exp += 5
        pet.save()

        wallet.credits += 100
        wallet.save()

        tasklist = request.user.taskslist
        tasklist.tasks.remove(task)

        if task.custom and task.user == request.user:
            task.delete()

        return Response({"detail": "task_reward_ok"}, status=status.HTTP_200_OK)


class TaskListAPIView(generics.RetrieveAPIView):
    serializer_class = TasksListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return TasksList.objects.get(user=self.request.user)


class AdventureLocationAPIListView(generics.ListAPIView):
    queryset = AdventureLocation.objects.all()
    serializer_class = AdventureLocationSerializer


class CurrentAdventureAPIView(generics.RetrieveAPIView):
    serializer_class = CurrentAdventureSerializer

    def get_object(self):
        return getattr(self.request.user, "currentadventure", None)


class AdventureStartAPIView(generics.GenericAPIView):
    def post(self, request):
        if hasattr(request.user, "currentadventure"):
            return Response(
                {"detail": "adventure_ongoing"}, status=status.HTTP_400_BAD_REQUEST
            )

        destination_id = request.data.get("destination_id")
        destination = get_object_or_404(AdventureLocation, id=destination_id)

        current = CurrentAdventure.objects.create(
            user=request.user, destination=destination
        )
        return Response(
            CurrentAdventureSerializer(current).data, status=status.HTTP_201_CREATED
        )


class CompleteAdventureAPIView(generics.GenericAPIView):
    def post(self, request, pk):
        try:
            current = CurrentAdventure.objects.get(id=pk, user=request.user)
        except CurrentAdventure.DoesNotExist:
            return Response(
                {"detail": "current_adventure_not_found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        destination = current.destination
        pet = request.user.pet
        wallet = request.user.wallet

        pet.exp += destination.exp_reward
        pet.save()

        wallet.credits += destination.credit_reward
        wallet.save()

        current.delete()
        return Response({"detail": "rewards_granted"}, status=status.HTTP_200_OK)


class ShopItemListView(generics.ListAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class CustomizeAPIView(generics.GenericAPIView):
    def get(self, request):
        try:
            pet = Pet.objects.get(user=request.user)
        except Pet.DoesNotExist:
            return Response({"detail": "pet_missing"}, status=status.HTTP_404_NOT_FOUND)
        inventory = (
            Inventory.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "inventoryitem_set",
                    queryset=InventoryItem.objects.select_related("consumable"),
                )
            )
            .first()
        )
        closet = (
            Closet.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "closetitem_set",
                    queryset=ClosetItem.objects.select_related("cosmetic"),
                )
            )
            .first()
        )
        cosmetics_grouped = defaultdict(list)
        if closet:
            for clo_item in closet.closetitem_set.all():
                cosmetics_grouped[clo_item.cosmetic.slot].append(
                    {
                        "id": clo_item.id,
                        "name": clo_item.cosmetic.name,
                        "rarity": clo_item.cosmetic.rarity,
                        "equipped": clo_item.equipped,
                        "icon": (
                            clo_item.cosmetic.icon.url
                            if clo_item.cosmetic.icon
                            else None
                        ),
                    }
                )
        data = {
            "pet": (
                {
                    "name": pet.name,
                    "avatar": pet.avatar if pet.avatar else None,
                }
                if pet
                else None
            ),
            "inventory": (
                InventoryItemSerializer(
                    inventory.inventoryitem_set.all(), many=True
                ).data
                if inventory
                else []
            ),
            "cosmetics": cosmetics_grouped,
        }

        return Response(data, status=status.HTTP_200_OK)


class EquipCosmeticAPIView(generics.GenericAPIView):
    def post(self, request, clo_item_id):
        clo_item = get_object_or_404(
            ClosetItem, id=clo_item_id, closet__user=request.user
        )
        cosmetic = clo_item.cosmetic
        closet = clo_item.closet

        if clo_item.equipped:
            clo_item.equipped = False
            clo_item.save()
            return Response({"detail": "item_unequipped"}, status=status.HTTP_200_OK)

        ClosetItem.objects.filter(
            closet=closet, cosmetic__slot=cosmetic.slot, equipped=True
        ).update(equipped=False)

        clo_item.equipped = True
        clo_item.save()
        return Response({"detail": "item_equipped"}, status=status.HTTP_200_OK)


class PurchaseItemAPIView(generics.GenericAPIView):
    def post(self, request, item_id):
        user = request.user
        balance = user.wallet
        item = get_object_or_404(ShopItem, pk=item_id)

        if balance.credits < item.price:
            return Response(
                {"detail": "insufficient_credits"}, status=status.HTTP_400_BAD_REQUEST
            )

        balance.credits -= item.price
        balance.save()

        model = item.content_type.model_class()
        if model == Cosmetic:
            closet = user.closet
            if ClosetItem.objects.filter(
                closet=closet, cosmetic=item.item_object
            ).exists():
                return Response(
                    {"detail": "owned_item"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            ClosetItem.objects.create(closet=closet, cosmetic=item.item_object)

        elif model == Consumable:
            inventory = user.inventory
            inv_item, created = InventoryItem.objects.get_or_create(
                inventory=inventory,
                consumable=item.item_object,
                defaults={"quantity": 1},
            )
            if not created:
                inv_item.quantity += 1
                inv_item.save()

        order = CreditPurchase.objects.create(
            user=user,
            item=item,
            price=item.price,
        )

        return Response(
            {"detail": "successful_purchase"}, status=status.HTTP_201_CREATED
        )


class PurchaseHistoryAPIView(generics.ListAPIView):
    serializer_class = CreditPurchaseSerializer

    def get_queryset(self):
        return CreditPurchase.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )
