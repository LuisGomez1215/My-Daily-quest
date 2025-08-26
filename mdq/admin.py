from typing import NewType
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MdqUser, Pet, PetBackground, PetType, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"

@admin.register(MdqUser)
class MdqUserAdmin(UserAdmin):
    inlines = [ProfileInline]

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','user','species','background','exp','hp','stamina','bond','mood','birthday']
    list_filter = ['species', 'user']
    search_fields = ['name']
    date_hierarchy = 'birthday'

@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    list_display = ['species','desc','pet_avatar']
    list_filter = ['species']

@admin.register(PetBackground)
class PetBackgroundAdmin(admin.ModelAdmin):
    list_display = ['name','image','description']
    list_filter = ['name']
