from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,ItemCategory,Order,OrderDetail
from django.db.models import Sum
from .util import grand_total

def home(request):
    equipment = Item.objects.filter(itemCategory__name="Equipment").reverse()[:3]
    furniture = Item.objects.filter(itemCategory__name="Furniture").reverse()[:3]
    category = ItemCategory.objects.all()
    context = {
        "items" : equipment,
        "furniture" : furniture,
        "categories" : category,
    }
    return render(request,'camping/index.html',context)




def everything_item(request):
    items = Item.objects.all()
    category = ItemCategory.objects.all()
    query = request.GET.get("category")

    if query:
        items = items.filter(itemCategory__name=query)

    context={
        'items' : items,
        'categories': category,
    }
    return render(request,"camping/everything.html",context)


def item_detail(request,slug:str):
    item = get_object_or_404(Item, slug=slug)
    context = {
        "item": item,
    }
    return render(request,"camping/itemDetail.html",context)

def addToCart(request):
    itemID = request.POST.get("item_id")
    quantity = request.POST.get("quantity")
    item = Item.objects.get(id=itemID)
    total = item.price * int(quantity) 
    OrderDetail.objects.create(item = item, quantity=quantity,total=total)
    return redirect('home')

def cart_info(request):
    order = OrderDetail.objects.filter(status=0)
    total = grand_total()
    context={
        'orders': order,
        'total':total,
    }
    return render(request,"camping/cart.html",context)

def deleteOrder(request):
    orderId = request.POST.get("order_id")
    obj = OrderDetail.objects.get(id=orderId)
    obj.delete() 

    return redirect("cartInfo")

def create_order(request):
    username = request.POST.get("name")
    region = request.POST.get("region")
    city = request.POST.get("city")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    get_grand_total = grand_total()
    order_detail = OrderDetail.objects.all()
    for i in order_detail:
        i.status = 1
        i.save()

    order = Order.objects.create(username=username,region=region,city=city,address=address,phone=phone,email=email,grand_total=get_grand_total)
    order.order_detail.add(*order_detail)
    order.save()
    
    
    return redirect("home")
