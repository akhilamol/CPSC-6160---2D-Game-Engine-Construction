###
import pygame
class update_time_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='update_time'
		self.hud = None
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		if self.condition_to_act(data):
			self.hud.message = int(self.entity_state.elapsed_time/1000)

		return
