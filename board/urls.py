from django.urls import path
from . import views

app_name ="board"
urlpatterns = [
        path("",views.List.as_view(), name="list"),
        path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
        path("create/", views.Create.as_view(), name="create"),
        path("edit/<int:pk>/", views.Edit.as_view(), name ="edit"),
        path("delete/<int:pk>/", views.Delete.as_view(), name="delete")
]
