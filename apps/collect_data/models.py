from django.db import models


# 传感器节点信息
class Sensor_node(models.Model):
	identify = models.CharField(max_length=30, verbose_name="编号")
	# 坐标采用高精度gps定位坐标 exp: (22.4222, 119.2411)
	position = models.CharField(max_length=30, verbose_name="坐标")
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	description = models.CharField(max_length=200, verbose_name="附加描述")

	def __str__(self):
		return self.identify

	class Meta:
		verbose_name = '节点'
		verbose_name_plural = verbose_name


# 节点收集的数据
class Node_data(models.Model):
	node = models.ForeignKey('Sensor_node', on_delete=models.CASCADE, verbose_name="节点")
	collect_time = models.TimeField(default=None, verbose_name="采集时间")
	collect_date = models.DateField(default=None, verbose_name="采集日期")
	collect_datetime = models.DateTimeField(default=None, verbose_name="采集日期时间")
	# 具体数据
	temperature = models.FloatField(verbose_name="温度/℃")
	soil_humidity = models.FloatField(verbose_name="土壤湿度/%")
	air_humidity = models.FloatField(verbose_name="空气湿度/%")
	oxygen = models.FloatField(verbose_name="氧气浓度/%")
	carbon_dioxide = models.FloatField(verbose_name="二氧化碳浓度/%")
	# 设备自身信息
	battery = models.FloatField(verbose_name="电池电量/%")

	def __str__(self):
		return str(self.collect_time)

	class Meta:
		verbose_name = '节点收集的数据'
		verbose_name_plural = verbose_name
