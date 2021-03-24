from django.contrib import admin
from .models import House,Land,WareHouse

@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display=['name','price','created','status']
    list_filter=['created']


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display=['name','price','created']
    list_filter=['created']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display=['name','price','created']
    list_filter=['created']
