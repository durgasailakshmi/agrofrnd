from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('farmers',views.farmers,name="farmers"),
    path('transportprovider/',views.transportprovider,name="transportprovider"),
    path('market',views.market,name="market"),
    path('wearhouses',views.wearhouses,name="wearhouses"),
    path('communityowner',views.communityowner,name="communityowner"),
    	]