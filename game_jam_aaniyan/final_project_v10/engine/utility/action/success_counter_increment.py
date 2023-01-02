###
import pygame

class success_counter_increment_action():
	def __init__(self):
		self.types = []
		self.entity_state = None 
		self.name ='success_counter_increment'
		self.children =[]
		self.verbose = False
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False

		return True

	def act(self,data):
		if self.condition_to_act(data):
			self.entity_state.counter +=1	
			#print("~~~~~~~~~~~~~\n\n\n\n\nsuccess counter new = ", self.entity_state.counter)

		return