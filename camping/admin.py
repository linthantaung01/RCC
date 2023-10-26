from django.contrib import admin
from .models import Item,ItemCategory,OrderDetail,Order
# Register your models here.

class ItemAdmin(admin.ModelAdmin):

    list_display=(
        "id",
        "itemName",
        "slug",
        "description",
        "itemCategory",
        "image",
        "price",
    )  
    
    list_filter = (
        "itemCategory",
    )
       
    prepopulated_fields = (
        {"slug" : ("itemName",)}
    )

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "slug", 
    )
  
    prepopulated_fields = (
        {"slug" : ("name",)}
    )

class OrderDetailAdmin(admin.ModelAdmin):
    list_display=(
        "item",
        "quantity",
        "total", 
    )
  
   
class OrderAdmin(admin.ModelAdmin):
    list_display=(
        "username",
        "region",
        "city", 
        "address",
        "phone",
        "email",
        "grand_total",
        "get_order_detail"
    )

    def get_order_detail(self,obj):
        return [  detail.item for detail in  obj.order_detail.all() ]

admin.site.register(Order,OrderAdmin),
admin.site.register(OrderDetail,OrderDetailAdmin),
admin.site.register(Item,ItemAdmin),
admin.site.register(ItemCategory,ItemCategoryAdmin),