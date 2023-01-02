###
import pygame
class timer_elapsed_time_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
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
			self.entity_state.elapsed_time = self.entity_state.current_time-self.entity_state.start_time
			# print("elapsed time for level = ",self.entity_state.elapsed_time)

		return 