from django.contrib import admin
from .models import Item,ItemCategory
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


admin.site.register(Item,ItemAdmin),
admin.site.register(ItemCategory,ItemCategoryAdmin),