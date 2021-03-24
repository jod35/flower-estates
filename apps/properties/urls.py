from django.urls import path
from . import views

app_name = 'prop'

urlpatterns =[
    path('',views.HomeView.as_view(),name='home'),
    path('rentals/',views.HouseRentalListView.as_view(),name='rentals'),
    path('houses_for_sale/',views.HouseSaleListView.as_view(),name='sale_houses'),
    path('warehouses/',views.WareHouseListView.as_view(),name='warehouses'),
    path('agents/',views.AgentView.as_view(),name='agents'),
    path('lands',views.LandListView.as_view(),name='land'),
    path('articles/',views.BlogView.as_view(),name='articles'),
    path('contacts/',views.ContactView.as_view(),name='contacts')

]