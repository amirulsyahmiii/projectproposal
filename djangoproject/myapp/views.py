from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt
#from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
	return HttpResponse("Hello! This is a django project from Thundering Jaguars using Ubuntu!")

def welcome(request):

	return render(request, 'welcome.html')

# Create your views here

mqtt_data = 0  # MQTT data variable

@csrf_exempt


def mqtt_handler(request):
    # MQTT Broker Settings
    mqtt_broker = "91.121.93.94"
    mqtt_topic = "sensor/data"

    # MQTT Callback function to handle received messages
    def on_message(client, userdata, message):
        global mqtt_data  # Access the outer variable
        mqtt_data = int(message.payload.decode())  # Update the MQTT data

    # Create MQTT client and connect to the broker
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_broker, 1883)

    # Subscribe to the MQTT topic
    client.subscribe(mqtt_topic)

    # Start the MQTT loop to handle incoming messages
    client.loop_start()

    return render(request, 'mqtt_data.html', {'mqtt_data': mqtt_data})
