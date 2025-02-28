from django.urls import path
from . import views

app_name ="board"
urlpatterns = [
        path("",views.List.as_view(), name="list")
]
