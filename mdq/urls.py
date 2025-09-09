from django.urls import path, include
from django.contrib import admin

from mdq.views import auth, pages, shop

urlpatterns = [
    # auth
    path('', auth.index, name='index'),
    path('pet/customization', pages.customize, name='customize'),
    path('pet/customization/equip/<int:clo_item_id>', pages.customize_equip, name='customize-equip'),
    path('pet/select', pages.petselect, name='petselect'),
    path('pet/select/<int:species_id>/', pages.petselectform, name='petselectform'),
    path('pet/shop', shop.shop, name='shop'),
    path('pet/shop/buy/<int:item_id>', shop.purchase_item, name="purchase-item"),
    path('pet/settings', pages.settings, name='settings'),
    path('pet/tasks', pages.task_list, name='tasklist'),
    path('pet/tasks/<int:task_id>/', pages.complete_task, name='task-complete'),
    path('pet/task_select', pages.task_select, name='task_select'),
    path('pet/create_task', pages.task_create, name='create-task'),
    path('pet/adventure', pages.adventure, name='adventure'),
    path('pet/adventure/complete/<int:current_id>', pages.complete_adventure, name='complete_adventure'),
    path('accounts/registration/', auth.register, name='register'),
    path('accounts/registration/termsandconditions', auth.termsandconditions, name='tos'),
]
