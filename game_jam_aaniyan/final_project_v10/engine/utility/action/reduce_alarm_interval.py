###
import pygame

class reduce_alarm_interval_action():
	def __init__(self,reduce_ratio):
		self.types = ['']
		self.entity_state = None 
		self.verbose = False
		self.name ='reduce_alarm_interval'
		self.children = []
		self.reduce_ratio = reduce_ratio
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def insert_child(self,child):
		self.children.append(child)

	def act(self,data):
		if self.condition_to_act(data):
			# change button location
			self.entity_state.alarm_interval = self.entity_state.alarm_interval*self.reduce_ratio

		return 