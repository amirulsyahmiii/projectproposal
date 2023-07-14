from django.urls import path
from .views import mqtt_handler
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path ('mqtt-handler/', views.subscribe_to_mqtt_broker, name = 'mqtt_handler')

    #path('mqtt-handler/', views.mqtt_handler, name='mqtt_handler')
	
]
