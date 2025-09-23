from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from mdq.views import auth, pages, shop
from mdq.rest_views import viewsets, rest_views

router = DefaultRouter()
router.register(r"petselect", viewsets.PetTypeViewSet, basename="petselect")
router.register(r"pet", viewsets.PetViewSet, basename="pet")

urlpatterns = [
    # api
    path('api/v1/', include(router.urls)),
    path('api/v1/register', rest_views.user_registration, name='register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # api task
    path('api/v1/tasks/select/', viewsets.TaskSelectAPIView.as_view(), name="task-select"),
    path('api/v1/tasks/create/', viewsets.TaskCreateAPIView.as_view(), name="task-create"),
    path('api/v1/tasks/list/', viewsets.TaskListAPIView.as_view(), name="task-list"),
    path('api/v1/tasks/<int:task_id>/complete/', viewsets.TaskCompleteAPIView.as_view(), name="task-complete"),
    # api adventure
    path('api/v1/adventure/locations/', viewsets.AdventureLocationAPIListView.as_view(), name="adv-location"),
    path('api/v1/adventure/current/', viewsets.CurrentAdventureAPIView.as_view(), name="current-adv"),
    path('api/v1/adventure/start/', viewsets.AdventureStartAPIView.as_view(), name="adv-start"),
    path('api/v1/adventure/complete/<int:pk>/', viewsets.CompleteAdventureAPIView.as_view(), name="adv-complete"),
    # api shop
    path('api/v1/shop/', viewsets.ShopItemListView.as_view(), name="shop-display"),
    path('api/v1/shop/purchase/<int:item_id>/', viewsets.PurchaseItemAPIView.as_view(), name="shop-purchase"),
    path('api/v1/shop/history/', viewsets.PurchaseHistoryAPIView.as_view(), name="shop-history"),
    # api customize
    path('api/v1/customize/', viewsets.CustomizeAPIView.as_view(), name="customize-display"),
    path('api/v1/customize/equip/<int:clo_item_id>/', viewsets.EquipCosmeticAPIView.as_view(), name="customize-equip"),
    # non drf paths
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
