from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class MdqUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(MdqUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='avatar')
    birth = models.DateField(null=True, blank=True, default=None)
    credits = models.IntegerField(default=1000, blank=True)
    birthday = models.DateTimeField(auto_now_add=True)

    def get_url(self, request=None):
        rev_url = reverse('profile', kwargs={'username': self.user.username})
        return request.build_absolute_uri(rev_url) if request else rev_url

    def get_avatar_url(self, request=None):
        url = static('img/placeholder/300x150.png')
        avatar_url = self.avatar.url if self.avatar else url
        return request.build_absolute_uri(avatar_url) if request else avatar_url

    def __str__(self) -> str:
        return f'{self.user}'


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
    last_adventure = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ({self.species.species})"

    def get_mood_display(self):
        return self.MOOD_CHOICES.get(self.mood, "Unknown")

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
        elif self.mood >= 80:
            return "Good"
        elif self.mood >= 50:
            return "Normal"
        elif self.mood >= 20:
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
