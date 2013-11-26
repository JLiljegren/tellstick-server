# -*- coding: utf-8 -*-

import os
import json
from configobj import ConfigObj
import ConfigParser


class Settings(object):
	def __init__(self, section):
		super(Settings,self).__init__()
		self.section = section

		self.configPath = os.environ['HOME'] + '/.config/Telldus'
		self.configFilename = 'Telldus.conf'
		self.config = ConfigObj(self.configPath + '/' + self.configFilename)
		if section not in self.config:
			self.config[section] = {}

	def get(self, name, default):
		v = self[name]
		if v is None:
			return default
		if type(default) is dict or type(default) is list:
			v = json.loads(v)
		if type(default) == int:
			v = int(v)
		return v

	def __getitem__(self, name):
		try:
			value = self.config[self.section][name]
		except:
			return None
		return value

	def __setitem__(self, name, value):
		if type(value) is dict or type(value) is list:
			value = json.dumps(value)
		self.config[self.section][name] = value
		self.config.write()