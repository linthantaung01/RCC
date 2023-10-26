from django.urls import path
from .views import home,everything_item,item_detail,addToCart,cart_info,deleteOrder,create_order

urlpatterns = [
    path("",home,name="home"),
    path("everything/",everything_item,name="everything_item"),
    path("item-detail/<slug:slug>",item_detail,name="item_detail"),
    path("addToCart", addToCart, name= "addToCart"),
    path("cartInfo",cart_info,name="cartInfo"),
    path("deleteOrder",deleteOrder,name="deleteOrder" ),
    path("create_order",create_order,name="create_order"),
]
