from django.db import models

class SensorData(models.Model):
    ultrasonic_data = models.IntegerField()
    moisture_data = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ultrasonic: {self.ultrasonic_data}, Moisture: {self.moisture_data}"


