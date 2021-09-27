from django.urls import path

from vk_parser.api import views


app_name = "api"

urlpatterns = [
    path('<str:wall_url>/', views.ParseView.as_view(), name='parser')
]