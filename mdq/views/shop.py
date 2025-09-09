from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from mdq.models import ShopItem, CreditPurchase, Inventory, InventoryItem, Closet, ClosetItem, Wallet, Cosmetic

@login_required
def shop(request):
    items = ShopItem.objects.all()
    closet = Closet.objects.get(user=request.user)
    owned = ClosetItem.objects.filter(closet=closet).values_list("cosmetic_id", flat=True)
    return render(request, "pages/shop.html", {"items": items, 'owned': set(owned) })

@login_required
def purchase_item(request, item_id):
    balance = Wallet.objects.get(user=request.user)
    item = None

    try:
        item = ShopItem.objects.get(pk=item_id)
    except ShopItem.DoesNotExist:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    if balance.credits < item.price:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    balance.credits -= item.price
    balance.save()
    model = item.content_type.model_class()
    if model == Cosmetic:
        closet = Closet.objects.get(user=request.user)
        owned = ClosetItem.objects.filter(closet=closet, cosmetic=item.item_object).exists()

        if owned:
            messages.error(request, f"You already own this {item.item_object.name}!")
            return redirect("shop")
        ClosetItem.objects.create(closet=closet, cosmetic=item.item_object)
    else:
        inventory = Inventory.objects.get(user=request.user)

        try:
            inv_item = InventoryItem.objects.get(
                inventory=inventory,
                consumable=item.item_object
            )
            inv_item.quantity += 1
            inv_item.save()

        except InventoryItem.DoesNotExist:
            InventoryItem.objects.create(
                inventory=inventory,
                consumable=item.item_object,
                quantity=1
            )

    order = CreditPurchase.objects.create(
        user=request.user,
        item=item,
        price=item.price,
    )
    return redirect("shop")
