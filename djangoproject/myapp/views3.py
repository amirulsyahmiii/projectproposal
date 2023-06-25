from django.shortcuts import render
from django.http import HttpResponse
import paho.mqtt.client as mqtt
#from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return HttpResponse("Hello! This is a Django project from Thundering Jaguars using Ubuntu!")

def welcome(request):
    return render(request, 'welcome.html')

# Create your views here
ultrasonic_data = 0
moisture_data = 0.0

#@csrf_exempt
def mqtt_handler(request):
    # MQTT Broker Settings
    mqtt_broker = "91.121.93.94"
    mqtt_topics = ("sensor/ultrasonic"), ("sensor/moisture")

    # MQTT Callback function to handle received messages
    def on_message(client, userdata, message):
        global ultrasonic_data, moisture_data  # Access the outer variable
        topic = message.topic
        payload = message.payload.decode()
        if topic == "sensor/ultrasonic":
            ultrasonic_data = int(payload)
        elif topic == "sensor/moisture":
            moisture_data = float(payload)

    # Create MQTT client and connect to the broker
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_broker, 1883)

    # Subscribe to the MQTT topics
    for topic in mqtt_topics:
        client.subscribe(topic)

    # Start the MQTT loop to handle incoming messages
    client.loop_start()

    return render(request, 'sensor_data.html', {'ultrasonic_data': ultrasonic_data, 'moisture_data': moisture_data})
