from django.contrib import admin
from django.urls import path,include
from Home import views
urlpatterns = [
    path('',views.Index,name="Index"),
    path('portfolio',views.portfolio,name="Portfolio"),
    path('cv',views.cv,name="CV"),
    path('hire',views.hire,name="Hire"),
]
