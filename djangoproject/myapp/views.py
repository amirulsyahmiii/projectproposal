from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import SensorData
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import paho.mqtt.client as mqtt
import mysql.connector
import threading
import time
def home(request):
    return HttpResponse("Hello! This is a Django project from SMIRKING MERLIONS ROAR ROAR ROAR using Ubuntu!")

def welcome(request):
    mqtt_handler_url = reverse('mqtt_handler')  # Get the URL for the mqtt_handler view
    return render(request, 'welcome.html', {'mqtt_handler_url': mqtt_handler_url})

# Create your views here
ultrasonic_data = 0.0
moisture_data = 0.0

def mqtt_handler():
    # MQTT Broker Settings
    mqtt_broker = "91.121.93.94"
    mqtt_topics = [("sensor/ultrasonic"), ("sensor/moisture_data")]

    # MySQL Database Settings
    mysql_host = 'localhost:'
    mysql_user = 'jaguar'
    mysql_password = '2233'
    mysql_database = 'sensor_data'
    
    def on_connect(client, userdata,flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to the MQTT topics
            for topic in mqtt_topics:
                client.subscribe(topic)
        else:
            print("Failed to connect to MQTT broker")

    # MQTT Callback function to handle received messages
    def on_message(client, userdata, message):
        global ultrasonic_data, moisture_data  # Access the outer variable
        topic = message.topic
        payload = message.payload.decode()
        if topic == "sensor/ultrasonic":
            ultrasonic_data = int(payload)
            
        elif topic == "sensor/moisture_data":
            moisture_data = float(payload)

        # Save data to MySQL
        sensor_data = SensorData(ultrasonic_data=ultrasonic_data, moisture_data=moisture_data)
        sensor_data.save()
        print("save data")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(mqtt_broker, 1883)

    client.loop_start()
    while True:
        time.sleep(1)  



         
        
        
def subscribe_to_mqtt_broker(request):
    mqtt_thread = threading.Thread(target=mqtt_handler)
    mqtt_thread.start()
	
	
    return render(request, 'sensor_data.html', {'ultrasonic_data': ultrasonic_data, 'moisture_data': moisture_data})
  
    


"""
def mqtt_handler(request):
    # MQTT Broker Settings
    mqtt_broker = "91.121.93.94"
    mqtt_topics = [("sensor/ultrasonic"), ("sensor/moisture")]

    # MySQL Database Settings
    mysql_host = 'localhost'
    mysql_user = 'jaguar'
    mysql_password = '2233'
    mysql_database = 'sensor_data'

    # MQTT Callback function to handle received messages
    def on_message(client, userdata, message):
        global ultrasonic_data, moisture_data  # Access the outer variable
        topic = message.topic
        payload = message.payload.decode()
        if topic == "sensor/ultrasonic":
            ultrasonic_data = int(payload)
        elif topic == "sensor/moisture":
            moisture_data = float(payload)

    # Save data to the database


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
"""


