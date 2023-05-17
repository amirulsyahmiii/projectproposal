# projectproposal
# Problem Statement: 
Our goal is to create an IoT system that monitors and controls the temperature and humidity levels in a greenhouse. The system will collect real-time data from sensors placed inside the greenhouse and use it to make informed decisions about when to activate a water sprinkler or turn on a fan to adjust the temperature and humidity levels. The main objective is to create a sustainable and efficient environment for plant growth, resulting in increased yield and reduced energy consumption.
# System Architecture:
Our IoT system will consist of three main components: the sensors, the cloud platform, and the dashboard. The sensors will be connected to a Raspberry Pi which will collect the data and send it to the cloud platform using MQTT protocol. The cloud platform will use Django/Flask and InfluxDB database to store the data and provide real-time analysis and decision-making capabilities. The dashboard will use Grafana to visualize the data and provide a user-friendly interface for users to monitor the system.
![Alt text](https://github.com/amirulsyahmiii/projectproposal/blob/main/Github%20repo/1.png)

# Sensor Used:
We will be using a Raspberry Pi as our IoT sensor. It will be connected to a DHT22 sensor for temperature and humidity measurements. We will be using the MQTT protocol for data transmission to the cloud platform.
# Cloud Platform:
We will be using PythonAnywhere as our web hosting service for the Django/Flask app. The app will use InfluxDB to store the data. The app will analyze the data to make decisions on when to turn on/off the water sprinkler or fan.
# Dashboard:
We will be using Grafana to create our dashboard. The dashboard will display real-time temperature and humidity readings from the sensors, along with graphs showing historical trends. It will also provide controls for users to turn on/off the water sprinkler or fan. We plan to use Figma to design the dashboard interface.
# Video Demo:
We will record a video demo of our Django/Flask app running on PythonAnywhere and provide a link to it on our Github page.
