from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class MdqUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='avatar')
    birth = models.DateField(null=True, blank=True, default=None)
    birthday = models.DateTimeField(auto_now_add=True)

    def get_avatar_url(self, request=None):
        url = static('img/placeholder/300x150.png')
        avatar_url = self.avatar.url if self.avatar else url
        return request.build_absolute_uri(avatar_url) if request else avatar_url

    def __str__(self) -> str:
        return f"{self.user}"


class PetType(models.Model):
    species = models.CharField(max_length=50)
    desc = models.TextField(max_length=300, blank=True)
    pet_avatar = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.species


class PetBackground(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="pet_backgrounds/")
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    species = models.ForeignKey(PetType, on_delete=models.CASCADE)
    background = models.ForeignKey(PetBackground, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Pet")
    exp = models.FloatField(default=0.0)
    hp = models.PositiveIntegerField(default=20)
    stamina = models.PositiveIntegerField(default=40)
    bond = models.FloatField(default=0.0)
    mood = models.IntegerField(default=50)
    birthday = models.DateTimeField(auto_now_add=True)
    last_fed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ({self.species.species})"

    def get_level(self):
        level = 1
        while self.exp >= self.exp_required(level + 1):
            level += 1
        return level

    def exp_required(self, x):
        b, t = 1, 0
        return (1 + b) ** (x + t)

    @property
    def mood_status(self):
        if self.mood >= 100:
            return "Perfect"
        if self.mood >= 80:
            return "Good"
        if self.mood >= 50:
            return "Normal"
        if self.mood >= 20:
            return "Bad"
        return "Awful"

    @property
    def bond_meter(self):
        if self.bond > 5:
            return round(self.bond / 20)
        return round(self.bond)

    @property
    def max_exp(self):
        return self.exp_required(self.get_level() + 1)

    @property
    def level(self):
        return self.get_level()

    @property
    def avatar(self):
        return self.species.pet_avatar.url


class Wallet(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField(default=1000)
    pcredits = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.user} - {self.credits} credits"


class Task(models.Model):
    user = models.ForeignKey(MdqUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    custom = models.BooleanField(default=False)

    def __str__(self):
        if self.custom:
            return f"[Custom] {self.name} - ({self.user})"
        return f"[Default] {self.name}"


class TasksList(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name="task_lists", blank=True)

    def __str__(self):
        return f"{self.user}'s Task List"


class AdventureLocation(models.Model):
    location_name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    difficulty = models.PositiveIntegerField(default=1)
    time = models.IntegerField(default=10)
    exp_reward = models.IntegerField(default=10)
    credit_reward = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.location_name}"


class CurrentAdventure(models.Model):
    destination = models.ForeignKey(AdventureLocation, on_delete=models.CASCADE)
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} is adventuring in {self.destination.location_name}"


class Inventory(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s Inventory"

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"

class Consumable(models.Model):
    name = models.CharField(max_length=100)
    effect = models.TextField(max_length=50)
    uses = models.IntegerField(default=1)
    icon = models.ImageField(upload_to="consumable/")

    def __str__(self):
        return f"{self.name} (x{self.uses})"


class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consumable.name} (x{self.quantity})"


class Cosmetic(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    slot = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="cosmetic/")

    def __str__(self):
        return f"{self.name} ({self.rarity})"


class Closet(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s Closet"


class ClosetItem(models.Model):
    closet = models.ForeignKey(Closet, on_delete=models.CASCADE)
    cosmetic = models.ForeignKey(Cosmetic, on_delete=models.CASCADE)
    equipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cosmetic} in {self.closet}"


class ShopItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"{self.name} - {self.price} credits"


class CreditPurchase(models.Model):
    user = models.ForeignKey(MdqUser, on_delete=models.CASCADE)
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} bought {self.item.name}"


class PaymentTransaction(models.Model):
    user = models.ForeignKey(MdqUser, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_url = models.URLField(default='', blank=True)
    token = models.CharField(default='', blank=True, max_length=64)
    token_gp = models.DateTimeField(default=None, blank=True, null=True)
    paid = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.paid}"
