# Project name: SmartFarm
# File name: xadmin
# Create time: 2019-11-22
import xadmin
from .models import *
from xadmin import views


# 是否使用主题选择功能
class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True


class GlobalSetting(object):
	site_title = u'智慧农场'  # 设置头标题
	site_footer = u'2019 智慧农场'  # 设置脚标题


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


class Sensor_nodeAdmin(object):
	list_display = ['identify', 'position', 'create_time', 'description']
	search_fields = ['identify', 'position']
	list_editable = ['identify', 'position', 'create_time', 'description']
	list_filter = ['identify', 'position', 'create_time', 'description']


class Node_dataAdmin(object):
	list_per_page = 120
	list_display = [
		'node', 'collect_time', 'temperature',
		'soil_humidity', 'air_humidity', 'oxygen',
		'carbon_dioxide', 'battery','collect_date',
		'collect_datetime'
	]
	search_fields = [
		'node',
		'collect_datetime'
	]
	list_editable = [
		'node', 'collect_time', 'temperature',
		'soil_humidity', 'air_humidity', 'oxygen',
		'carbon_dioxide', 'battery','collect_date',
		'collect_datetime'
	]
	list_filter = [
		'node', 'collect_time', 'temperature',
		'soil_humidity', 'air_humidity', 'oxygen',
		'carbon_dioxide', 'battery','collect_date',
		'collect_datetime'
	]
	data_charts = {
		u"温度变化": {
			'title': u"温度变化",
			"x-label": u"时间",
			"y-label": u"温度/℃",
			"x-field": "collect_datetime",
			"y-field": "temperature",
			"order": ('-collect_datetime',)
		},
		u"土壤湿度变化": {
			'title': u"土壤湿度变化",
			"x-field": "collect_datetime",
			"y-field": "soil_humidity",
			"order": ('-collect_datetime',)
		},
		u"空气湿度变化": {
			'title': u"空气湿度变化",
			"x-field": "collect_datetime",
			"y-field": "air_humidity",
			"order": ('-collect_datetime',)
		},
		u"氧气浓度变化": {
			'title': u"氧气浓度变化",
			"x-field": "collect_datetime",
			"y-field": "oxygen",
			"order": ('-collect_datetime',)
		},
		u"二氧化碳浓度变化": {
			'title': u"二氧化碳浓度变化",
			"x-field": "collect_datetime",
			"y-field": "carbon_dioxide",
			"order": ('-collect_datetime',)
		},
		u"电池电量变化": {
			'title': u"电池电量变化",
			"x-field": "collect_datetime",
			"y-field": "battery",
			"order": ('-collect_datetime',)
		},
	}


xadmin.site.register(Sensor_node, Sensor_nodeAdmin)
xadmin.site.register(Node_data, Node_dataAdmin)
