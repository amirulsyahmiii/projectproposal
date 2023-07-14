#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Wan Galaxy S23+";
const char* password = "Serirahmat2233";
const char* mqtt_server = "91.121.93.94";

const int triggerPin = 18; // Pin connected to the trigger pin of the ultrasonic sensor
const int echoPin = 19;    // Pin connected to the echo pin of the ultrasonic sensor
const int moisturePin = A0; // Pin connected to the moisture sensor

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  delay(100);
  Serial.begin(115200);
  while (!Serial);

  // Set up the ultrasonic sensor pins
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Set up the moisture sensor pin
  pinMode(moisturePin, INPUT); // Set moisture pin as INPUT

  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  char ultrasonicOutput[8]; // Assuming the value will be within a single digit
  char moistureOutput[8]; // Assuming the value will be within a single digit

  long duration, distance;

  // Trigger the ultrasonic sensor to measure distance
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2; // Calculate distance in centimeters

  snprintf(ultrasonicOutput, sizeof(ultrasonicOutput), "%d", distance); // Convert distance to string

  Serial.print("Ultrasonic Distance: ");
  Serial.println(ultrasonicOutput);
  client.publish("sensor/ultrasonic", ultrasonicOutput);

  int sensor_analog = analogRead(moisturePin);
  float _moisture = (100 - ((sensor_analog / 4095.00) * 100));

  snprintf(moistureOutput, sizeof(moistureOutput), "%.2f", _moisture); // Convert moisture reading to string with 2 decimal places

  Serial.print("Moisture Reading: ");
  Serial.print(_moisture);
  Serial.println("%");
  client.publish("sensor/moisture", moistureOutput);

  delay(1000);
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}
