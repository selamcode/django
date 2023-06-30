from django.urls import path

from .import views

# this will avoid conflict if we have the same functions name in different apps.
app_name = "tasks" 

urlpatterns = [

    path("", views.index, name="index"),
    path("add", views.add, name="add")
]