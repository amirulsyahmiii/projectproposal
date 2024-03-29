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
Open a terminal on your Ubuntu system.

1. To install Mosquitto MQTT, run the following command in the terminal.

```bash
sudo apt install mosquitto
```

2. Start Mosquitto Service. After the installation is complete, Mosquitto should start automatically and you can verify the service status by running.
```bash
sudo systeml status mosquitto
```
If the service not running, start it using this command.
```bash
sudo systeml start mosquitto
```
3. Test Mosquitto. Open 2 new terminal and subscribe to a topic.
```bash
mosquitto_sub -t sensor/moisture
mosquitto_sub -t sensor/ultrasonic
```
4. Try sending a message into your topic.
```bash
mosquitto_pub -t test/topic -m "Hello Thundering Jaguars"
```

## Note that when using mosquitto, you need to get the IP for MQTT broker. When you using your IPv4 and still cannot connect to the broker try use this command.
```bash
ping test.mosquitto.org
```
## After that you will get a new IP then put it in your esp to connect to the Mosquitto MQTT broker.

## Step 3: Django
Open a terminal on your Ubuntu system.

1. Update the package lists by running the following command:

```bash
sudo apt update
```
2. Install Python 3 and pip (Python package installer) if they are not already installed:

```bash
sudo apt install python3 python3-pip
```
3. Once Python and pip are installed, you can install Django using pip. Run the following command:

```bash
pip3 install Django
```
4. Create a new Django project (myproject) by running the following command:

```bash
django-admin startproject myproject
```
(myproject) can be anything you like.

Django will have default directories and files that are essential for web building.

**manage.py:**
>This is a command-line utility that allows you to interact with your Django project. You can use it to run development servers, perform database migrations, create superusers, and more.

**settings.py:**
> This file contains the configuration settings for your Django project. It includes database settings, middleware settings, static file settings, template settings, and other project-specific configurations.

**apps directory:**
> This directory contains the applications within your Django project. Each application typically has its own set of models, views, templates, and URL configurations.

**migrations directory:**
> This directory is created for each application and contains database migration files. Migrations are used to manage changes to your database schema over time.

**templates directory:**
> This directory stores the HTML templates for your Django project. Templates define the structure and layout of the rendered web pages.

To start Django server, we must be at the root Django folder which has manage.py file.

1. Start the Django development server by running the following command:

```bash
python3 manage.py runserver
```
2. Open a web browser and enter the following URL:
```bash
 http://localhost:8000
```
**Once you can start the server, the installation is complete. Next, we want to integrate MQTT and MySQL with Django. The necessary files for settings.py, urls.py, views.py, and html files are already provided within the repository.**

## Step 4: MySQL

pen the terminal

1. Install the MySQL server package:

```bash
sudo apt install mysql-server
```

2. During the installation process, you'll be prompted to set a password for th>

3. Start the MySQL service by running:

```bash
sudo systemctl start mysql
```
4. You can check whether the service is running by using command:

```bash
sudo systemctl status mysql
```

   If MySQL is running, you should see output indicating that it is active and >

5. Change the IP address at the 'bind-address' to allow it connected to any IP >

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf mysql
```

6. Restart MySQL to apply the configuration changes by running the following co>

```bash
sudo systemctl restart mysql
```

7. Verify that MySQL is listening on all IP addresses by running the following >

``bash
sudo netstat -tuln | grep 3306
```
or

```bash
sudo ss -tuln | grep 3306
```

8. Connect to the MySQL server using the root account and the password you set >

```bash
mysql -u root -p
```

9. After enter MySQL command-line interface, create a new database by running t>

```bash
CREATE DATABASE myapp_sensordata;
```

10. Create a new MySQL user and grant it privileges on the database by running >

```bash
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON myapp_sensordata.* TO 'username'@'%';
FLUSH PRIVILEGES;
```

11. Show the database available in mySQl and use the database that we want to u>

```bash
SHOW databases;
USE myapp_sensordata;
```

2. Create table for the database:
```bash
CREATE TABLE myapp_sensordata (
    id data_type1 [constraints],
    ultrasonic_data INT,
    moisture_data FLOAT,
    timestamp FLOAT
);
```

13. In Django project, open the 'settings.py' file located in the project's dir>

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myapp_sensordata',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
);
```

14. Create a Django app within project using the following command:

```bash
python manage.py startapp myapp
```

15. Update the 'models.py':

```bash
from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ultrasonic_data = models.IntegerField()
    moisture_data = models.FloatField()
```
16. Migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate

```

17. After that, go to MySQL interface and type the command for calling the tabl>

```bash
SELECT * FROM myapp_sensordata;

```

Data from Django is stored to MySQL


## Step 5: Grafana
Open browser and enter http://your_ip:3000 by using own IP address

1. Log in using the credentials "admin" and password "admin". This can be chan>

2. Add data source by selecting data source used. In this case we use MySQL.

3. All the details such as database, user, password and host information.

4. Then, the configuration is saved and tested to verify the connection.

5. Select create new dashboard then select add new panel.

6. In the measurements box, all the database and variables from MySQL are selected.

7. All the data extracted will be shown in the graph in the dashboard. After all this have been done click apply.

8. Two dashboards are created which is Ultrasonic sensor dashboard and Moisture sensor dashboard.  

9. Lastly, save the dashboard and now it will show all the data received from MySQL
