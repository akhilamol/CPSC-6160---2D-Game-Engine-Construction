###
import pygame
class update_message_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='update_message'
		self.hud = None
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		print("\n\n!!!!!!!!!!!!!",self.condition_to_act(data))
		if self.condition_to_act(data):
			print("current_time\n", self.entity_state)
			self.hud.message = self.entity_state.current_time
		return