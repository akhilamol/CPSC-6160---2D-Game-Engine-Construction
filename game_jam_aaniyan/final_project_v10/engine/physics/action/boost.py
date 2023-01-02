###
import pygame
import numpy 
import math
class boost_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='boost'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		if self.condition_to_act(data):

				for i in range(self.entity_state.particle_number):

					self.entity_state.particle_velocity[i][0] = 5 + self.entity_state.particle_velocity[i][0]
					self.entity_state.particle_velocity[i][1] = 5 + self.entity_state.particle_velocity[i][1]
					#self.entity_state.radius = self.entity_state.radius*1.1

		return