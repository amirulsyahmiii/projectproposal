from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import SensorData
import paho.mqtt.client as mqtt
import mysql.connector

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
    # Extract the received data
    topic = message.topic
    payload = message.payload.decode()
    if topic == "sensor/ultrasonic":
        ultrasonic_data = int(payload)
    elif topic == "sensor/moisture":
        moisture_data = float(payload)
    
    # Save the received data to the database
    save_data_to_mysql(ultrasonic_data, moisture_data)

# Create a MySQL connection and cursor
db_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
db_cursor = db_connection.cursor()

# Save data to the MySQL database
def save_data_to_mysql(ultrasonic_data, moisture_data):
    # Define the SQL query
    query = "INSERT INTO sensor_data (ultrasonic_data, moisture_data) VALUES (%s, %s)"

    # Execute the query with the data
    db_cursor.execute(query, (ultrasonic_data, moisture_data))

    # Commit the changes to the database
    db_connection.commit()

def mqtt_handler(request):
    # Create MQTT client and connect to the broker
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_broker, 1883)
    
    # Subscribe to the MQTT topics
    for topic in mqtt_topics:
        client.subscribe(topic)

    # Start the MQTT loop to handle incoming messages
    client.loop_start()

    return render(request, 'sensor_data.html')

def home(request):
    return HttpResponse("Hello! This is a Django project from Thundering Jaguars using Ubuntu!")

def welcome(request):
    return render(request, 'welcome.html')
