from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("searchRank", views.searchRank, name="searchRank"),
]