###
import pygame
class gravity_force_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='gravity_force'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		return True

	def act(self,data):
		if self.condition_to_act(data):
			#print("gravity before velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

			for i in range(self.entity_state.particle_number):
				self.entity_state.particle_gravity_force[i][0] = 0
				self.entity_state.particle_gravity_force[i][1] = self.entity_state.mass*self.entity_state.gravity_constant

			#print("gravity after velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])


		return