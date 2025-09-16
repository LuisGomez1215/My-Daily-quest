from typing import NewType
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mdq.models import (AdventureLocation, Closet, ClosetItem,
                        Consumable, Cosmetic, CreditPurchase,
                        CurrentAdventure, Inventory, InventoryItem,
                        MdqUser, PaymentTransaction, Pet,
                        PetBackground, PetType, Profile,
                        ShopItem, Task, TasksList, Wallet)


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


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user','credits','pcredits']
    list_filter = ['user']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user','name','icon','custom']
    list_filter = ['name','user']


@admin.register(TasksList)
class TasksListAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']

@admin.register(AdventureLocation)
class AdventureLocationAdmin(admin.ModelAdmin):
    list_display = ['location_name','description','difficulty','time','exp_reward','credit_reward']
    list_filter = ['difficulty','time']


@admin.register(CurrentAdventure)
class CurrentAdventureAdmin(admin.ModelAdmin):
    list_display = ['destination','user','created_at']
    list_filter = ['user']


class InventoryItemInline(admin.TabularInline):
    model = InventoryItem
    extra = 1


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']

    inlines=[InventoryItemInline]


class ClosetItemInline(admin.TabularInline):
    model = ClosetItem
    extra = 1


@admin.register(Closet)
class ClosetAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']

    inlines=[ClosetItemInline]


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','content_type','object_id','item_object']
    list_filter = ['content_type','name','price']


@admin.register(Cosmetic)
class CosmeticAdmin(admin.ModelAdmin):
    list_display = ['name','rarity','slot','icon']
    list_filter = ['slot','rarity']


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display = ['name','effect', 'uses', 'icon']
    list_filter = ['name', 'effect']


@admin.register(CreditPurchase)
class CreditPurchaseAdmin(admin.ModelAdmin):
    list_display = ['user','item','price','created_at']
    list_filter = ['user','item']


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','paid','created_at','confirmed_at','payment_url']
    list_filter = ['user','paid','created_at']
