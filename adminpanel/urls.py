from django.urls import path
from . import views

urlpatterns = [
     path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
     path("create-client/", views.CreateClientView.as_view(), name="create_client")
]