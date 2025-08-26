from django.urls import path, include
from django.contrib import admin

from mdq.views import auth, pages

urlpatterns = [
    # auth
    path('', auth.index, name='index'),
    path('pet/customization', pages.customize, name='customize'),
    path('pet/select', pages.petselect, name='petselect'),
    path('pet/select/<int:species_id>/', pages.petselectform, name='petselectform'),
    path('pet/shop', pages.shop, name='shop'),
    path('pet/settings', pages.settings, name='settings'),
    path('pet/tasks', pages.tasks, name='tasks'),
    path('pet/adventure', pages.adventure, name='adventure'),
    path('accounts/registration/', auth.register, name='register'),
    path('accounts/registration/termsandconditions', auth.termsandconditions, name='tos'),
]

