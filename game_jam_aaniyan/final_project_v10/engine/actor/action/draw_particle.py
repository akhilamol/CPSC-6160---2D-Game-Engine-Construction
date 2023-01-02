###
import pygame
class draw_particle_action():
	def __init__(self):
		self.types = ['display']
		self.entity_state = None 
		self.verbose = False
		self.name ='draw_particle'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		
		return True

	def draw(self,data):
		for i in range(self.entity_state.particle_number):
			if self.entity_state.particle_position[i][0]>600:
				pygame.draw.circle(data,self.entity_state.particle_color[i],self.entity_state.particle_position[i],10)

			else:

				pygame.draw.circle(data,self.entity_state.particle_color[i],self.entity_state.particle_position[i],self.entity_state.radius)

		return

	def act(self,data):
		if self.condition_to_act(data):
			self.draw(data)
		return