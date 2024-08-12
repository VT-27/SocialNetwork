from django.urls import path
from . import views

app_name = "tasks" # There is a folder newyear and urlpatterns with name = "index". To avoid name collision, it is better to add this line. Now in index.html and add.html, add tasks prefix when specifying name of route i.e. index or add.
urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.add, name = "add")
]