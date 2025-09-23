from rest_framework import serializers, status
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType

from mdq.models import (
    Profile,
    Pet,
    PetType,
    Wallet,
    CreditPurchase,
    CurrentAdventure,
    AdventureLocation,
    ShopItem,
    Consumable,
    Cosmetic,
    Closet,
    ClosetItem,
    Inventory,
    InventoryItem,
    TasksList,
    Task,
    MdqUser,
)


class MdqUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MdqUser
        fields = ["username", "email", "id"]


class MdqUserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = MdqUser
        fields = ["username", "email", "password", "password2"]

    def validate_username(self, value):
        try:
            MdqUser.objects.get(username=value)
            raise serializers.ValidationError({"detail": "existing_user"})
        except MdqUser.DoesNotExist:
            return value

    def validate_email(self, value):
        try:
            MdqUser.objects.get(email=value)
            raise serializers.ValidationError({"detail": "existing_email"})
        except MdqUser.DoesNotExist:
            return value

    def validate(self, attrs):
        password = attrs["password"]
        pswd2 = attrs["password2"]

        if password and pswd2 and password != pswd2:
            raise serializers.ValidationError({"detail": "invalid_password"})
        return attrs

    def create(self, validated_data):
        new_user = MdqUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        Profile.objects.create(user=new_user)
        Inventory.objects.create(user=new_user)
        Closet.objects.create(user=new_user)
        Wallet.objects.create(user=new_user)
        TasksList.objects.create(user=new_user)
        return new_user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "user", "birthday"

        class PetSerializer(serializers.ModelSerializer):
            class Meta:
                model = Pet
                fields = "__all__"


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = ["id", "species", "desc", "pet_avatar"]


class PetSerializer(serializers.ModelSerializer):
    species = PetTypeSerializer(read_only=True)
    level = serializers.ReadOnlyField()
    max_exp = serializers.ReadOnlyField()
    mood_status = serializers.ReadOnlyField()
    bond_meter = serializers.ReadOnlyField()
    avatar = serializers.ReadOnlyField()
    current_exp = serializers.SerializerMethodField()
    percentage = serializers.SerializerMethodField()
    petcheck = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = [
            "id",
            "species",
            "background",
            "name",
            "exp",
            "hp",
            "stamina",
            "bond",
            "mood",
            "birthday",
            "last_fed",
            "level",
            "max_exp",
            "mood_status",
            "bond_meter",
            "avatar",
            "current_exp",
            "percentage",
            "petcheck",
        ]
        read_only_fields = fields

    def get_current_exp(self, obj):
        return obj.exp

    def get_percentage(self, obj):
        if obj.max_exp > 0:
            return min(100, (obj.exp / obj.max_exp) * 100)
        return 0

    def get_petcheck(self, obj):
        return True


class PetSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["name"]

    def validate(self, attrs):
        user = self.context["request"].user
        if Pet.objects.filter(user=user).exists():
            raise serializers.ValidationError({"detail": 'existing_pet'})
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        species = self.context["species"]
        return Pet.objects.create(user=user, species=species, **validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "icon", "custom"]


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "icon"]

    def validate(self, attrs):
        request = self.context["request"]
        user = request.user
        name = attrs.get("name")

        if Task.objects.filter(user=user, name=name, custom=True).exists():
            raise serializers.ValidationError({"name": "duplicate_task"})

        if Task.objects.filter(name=name, custom=False).exists():
            raise serializers.ValidationError({"name": "duplicate_task"})

        return attrs

    def create(self, validated_data):
        request = self.context["request"]
        tasklist = TasksList.objects.get(user=request.user)

        task = Task.objects.create(user=request.user, custom=True, **validated_data)
        tasklist.tasks.add(task)
        return task


class TasksListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TasksList
        fields = ["id", "user", "tasks"]
        read_only_fields = ["id", "user", "tasks"]


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["user", "credits", "pcredits"]


class AdventureLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdventureLocation
        fields = [
            "id",
            "location_name",
            "description",
            "difficulty",
            "time",
            "exp_reward",
            "credit_reward",
        ]


class CurrentAdventureSerializer(serializers.ModelSerializer):
    destination = AdventureLocationSerializer(read_only=True)
    remaining = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()

    class Meta:
        model = CurrentAdventure
        fields = [
            "id",
            "destination",
            "created_at",
            "remaining",
            "end_time",
            "progress",
        ]

    def get_remaining(self, obj):
        duration = timedelta(hours=obj.destination.time)
        end_time = obj.created_at + duration
        return max((end_time - now()).total_seconds(), 0)

    def get_end_time(self, obj):
        duration = timedelta(hours=obj.destination.time)
        return (obj.created_at + duration).isoformat()

    def get_progress(self, obj):
        duration = timedelta(hours=obj.destination.time)
        elapsed = (now() - obj.created_at).total_seconds()
        total = duration.total_seconds()
        return min(100, max(0, (elapsed / total) * 100))


class CosmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmetic
        fields = ["id", "name", "rarity", "slot", "icon"]


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = ["id", "name", "effect", "uses", "icon"]


class InventoryItemSerializer(serializers.ModelSerializer):
    consumable = serializers.StringRelatedField()

    class Meta:
        model = InventoryItem
        fields = ["id", "consumable", "quantity"]


class ClosetItemSerializer(serializers.ModelSerializer):
    cosmetic = serializers.StringRelatedField()

    class Meta:
        model = ClosetItem
        fields = ["id", "cosmetic", "equipped"]


class CustomizeSerializer(serializers.Serializer):
    pet = PetSerializer()
    inventory = InventoryItemSerializer(many=True)
    cosmetics = ClosetItemSerializer(many=True)


class ShopItemSerializer(serializers.ModelSerializer):
    item_object = serializers.SerializerMethodField()
    owned = serializers.SerializerMethodField()

    class Meta:
        model = ShopItem
        fields = ["id", "name", "price", "item_object", "owned"]

    def get_item_object(self, obj):
        if obj.content_type.model_class() == Cosmetic:
            return CosmeticSerializer(obj.item_object).data
        elif obj.content_type.model_class() == Consumable:
            return ConsumableSerializer(obj.item_object).data
        return None

    def get_owned(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        if obj.content_type.model_class() == Cosmetic:
            closet_items = ClosetItem.objects.filter(
                closet__user=request.user, cosmetic=obj.item_object
            )
            return closet_items.exists()
        return False


class CreditPurchaseSerializer(serializers.ModelSerializer):
    item = ShopItemSerializer(read_only=True)

    class Meta:
        model = CreditPurchase
        fields = ["id", "item", "price", "created_at"]
