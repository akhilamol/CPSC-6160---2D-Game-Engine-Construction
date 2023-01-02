###
import pygame
class timer_alarm_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='timer_alarm'
		self.children = []
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
			#print("Alarm~~~~~~~\n", self.entity_state.alarm_interval, self.entity_state.elapsed_time)
			alarm_is_off = self.entity_state.elapsed_time > self.entity_state.alarm_interval
			if alarm_is_off:
				for child in self.children:
					child.act(alarm_is_off)

		return 