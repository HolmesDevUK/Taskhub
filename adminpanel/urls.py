from django.urls import path
from . import views

app_name = "adminpanel"

urlpatterns = [
     path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
     path("create-client/", views.CreateClientView.as_view(), name="create_client"),
     path("create-task/", views.CreateTaskView.as_view(), name="create_task"),
]