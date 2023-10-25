from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,ItemCategory
from django.db.models import Q

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

def category_detail(request,slug:str):
    category =  get_object_or_404(ItemCategory,slug = slug)
    context = {
        "category": category,
        "items" : category.item.all(),
    }
    return render(request,"camping/category_detail.html",context)

# def equipment(request):
#     equipment = Item.objects.filter(itemCategory=1)
#     context ={
#         "equipment" : equipment,
#     }
#     return render(request,'camping/equipment.html',context)

# def category_detail(request, slug:str):
#     category = get_object_or_404(ItemCategory,slug=slug)
    
#     context = {
#         "category" : category,
#         "equipment" :  category.item.all(),
#     }
#     return render(request,"camping/equipment.html",context)
