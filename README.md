# projectproposal
# Problem Statement: 
Our goal is to create an IoT system that monitors and controls the temperature and humidity levels in a greenhouse. The system will collect real-time data from sensors placed inside the greenhouse and use it to make informed decisions about when to activate a water sprinkler or turn on a fan to adjust the temperature and humidity levels. The main objective is to create a sustainable and efficient environment for plant growth, resulting in increased yield and reduced energy consumption.
# System Architecture:
Our IoT system will consist of three main components: the sensors, the cloud platform, and the dashboard. The sensors will be connected to a Raspberry Pi which will collect the data and send it to the cloud platform using MQTT protocol. The cloud platform will use Django/Flask and InfluxDB database to store the data and provide real-time analysis and decision-making capabilities. The dashboard will use Grafana to visualize the data and provide a user-friendly interface for users to monitor the system.
![Alt text](https://github.com/amirulsyahmiii/projectproposal/blob/main/Github%20repo/1.png)

# Sensor Used:
We will be using a ESP32 as our IoT sensor. It will be connected to a moisture sensor and ultrasonic sensors. We will be using the Mosquitto MQTT protocol for data transmission to the cloud platform.
# Cloud Platform:
The app will use MySQL to store the data. The app can analyze the data to make decisions to turn on/off components connected.
# Dashboard:
We will be using Grafana to create our dashboard. The dashboard will display real-time temperature and humidity readings from the sensors, along with graphs showing historical trends. It will also provide controls for users to turn on/off the water sprinkler or fan. We plan to use Figma to design the dashboard interface.
![Alt text](https://github.com/amirulsyahmiii/projectproposal/blob/main/software/soft%20dashboard.PNG)

# Video Demo:
We will record a video demo of our Django/Flask app running on PythonAnywhere and provide a link to it on our Github page.

# Installation:
## Step 1: Sensors from ESP32 and Arduino IDE
Moisture sensor and ultrasonic sensor data will be acquired by ESP32 and transmitted to Arduino IDE. Arduino IDE will be connected to a specific MQTT ip address (91.121.93.94). These data will be send to listening topics which are sensor/moisture and sensor/ultrasonic for moisture sensor and ultrasonic sensor respectively.

## Step 2: MQTT (Mosquitto)

## Step 3: Django
Open a terminal on your Ubuntu system.

1. Update the package lists by running the following command:

"sudo apt update"

2. Install Python 3 and pip (Python package installer) if they are not already installed:

"sudo apt install python3 python3-pip"

3. Once Python and pip are installed, you can install Django using pip. Run the following command:

"pip3 install Django"

4. Create a new Django project (myproject) by running the following command:

"django-admin startproject myproject"

(myproject) can be anything you like.

Django will have default directories and files that are essential for web building.

### manage.py:
This is a command-line utility that allows you to interact with your Django project. You can use it to run development servers, perform database migrations, create superusers, and more.

### settings.py:
This file contains the configuration settings for your Django project. It includes database settings, middleware settings, static file settings, template settings, and other project-specific configurations.

### apps directory:
This directory contains the applications within your Django project. Each application typically has its own set of models, views, templates, and URL configurations.

### migrations directory:
This directory is created for each application and contains database migration files. Migrations are used to manage changes to your database schema over time.

### templates directory:
This directory stores the HTML templates for your Django project. Templates define the structure and layout of the rendered web pages.

To start Django server, we must be at the root Django folder which has manage.py file.

1. Start the Django development server by running the following command:

"python3 manage.py runserver"

2. Open a web browser and enter the following URL:

"http://localhost:8000"


## Step 4: MySQL

## Step 5: Graffana
