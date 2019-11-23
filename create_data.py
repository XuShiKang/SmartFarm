# Project name: SmartFarm
# File name: create_data
# Create time: 2019-11-22
from collect_data.models import *
import random
from datetime import datetime, timedelta

temperature = 17.2
soil_humidity = 15.6
air_humidity = 53.3
oxygen = 20.9
carbon_dioxide = 0.24

nodes = Sensor_node.objects.all()


def run():
	time = datetime(2019, 11, 21)
	battery = 98.4

	while time < datetime(2019, 11, 24):
		for node in nodes:
			t = Node_data(
				node=node,
				collect_date=time.date(),
				collect_time=time.time(),
				collect_datetime=time,
				temperature=round(temperature + random.randint(-200, 200) / 100,3),
				soil_humidity=round(soil_humidity + random.randint(-500, 500) / 100,3),
				air_humidity=round(air_humidity + random.randint(-1000, 1000) / 100,3),
				oxygen=round(oxygen + random.randint(-200, 200) / 100,3),
				carbon_dioxide=round(carbon_dioxide + random.randint(-100, 100) / 1000,3),
				battery=round(battery,3)
			)
			t.save()
		print(f"time: {time}\tbattery: {battery}")
		time += timedelta(minutes=5)
		battery -= 0.01
