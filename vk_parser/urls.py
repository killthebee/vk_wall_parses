from django.urls import path, include

from vk_parser import views


app_name = 'vk_parses'

urlpatterns = [
    path('', views.MainView.as_view()),
    path('api/', include('vk_parser.api.urls'))
]

