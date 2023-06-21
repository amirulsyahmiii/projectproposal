from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('mqtt-handler/', views.mqtt_handler, name='mqtt_handler')
	
]
