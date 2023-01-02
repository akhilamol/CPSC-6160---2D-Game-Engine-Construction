
import pygame
class draw_circle_action():
	def __init__(self):
		self.types = ['display']
		self.entity_state = None 
		self.verbose = False
		self.name ='draw_circle'
		return

	def condition_to_act(self,data):
		
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def draw(self,data):

		pygame.draw.circle(data,self.entity_state.color,self.entity_state.center)

		return

	def act(self,data):

		if self.condition_to_act(data):
			self.draw(data)
		return