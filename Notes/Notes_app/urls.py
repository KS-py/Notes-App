from django.urls import path
from . import views

urlpatterns = [
	path("home/", views.home, name="home"),
	path("create/", views.create, name="create"),
	path("home/edit/<int:id>", views.edit, name="edit"),
	path("home/delete/<int:id>", views.delete, name="delete"),
	path("home/create", views.create, name="create"),
]
