###
import pygame
class update_particle_position_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='update_particle_position'
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
			for i in range(self.entity_state.particle_number):
				# 1/2 a t^2
				delta_y = 0.5*self.entity_state.force[i][1]/self.entity_state.mass\
				*self.entity_state.time_step*self.entity_state.time_step
				self.entity_state.position[i][1] = self.entity_state.position[i][1] + delta_y

		return 