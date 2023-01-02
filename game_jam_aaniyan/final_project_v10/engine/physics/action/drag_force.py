###
import pygame
class drag_force_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='drag_force'
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
					
				if self.entity_state.particle_position[i][0] >= 600:
					

					if self.entity_state.particle_velocity[i][0] >0:
						self.entity_state.particle_velocity[i][0] = self.entity_state.particle_velocity[i][0]*0.96# -0.05
					else:
						self.entity_state.particle_velocity[i][0] = self.entity_state.particle_velocity[i][0]*0.96#+ 0.05

					if self.entity_state.particle_velocity[i][1] >0:
						self.entity_state.particle_velocity[i][1] = self.entity_state.particle_velocity[i][1]*0.96# -0.05
					else:
						self.entity_state.particle_velocity[i][1] = self.entity_state.particle_velocity[i][1]*0.96#+0.05
						


					#self.entity_state.particle_velocity[i][0] = self.entity_state.particle_velocity[i][0]*0.96
					#self.entity_state.particle_velocity[i][1] = self.entity_state.drag_constant*self.entity_state.particle_velocity[i][1]

					#self.entity_state.particle_drag_force[i][0] = self.entity_state.mass*self.entity_state.drag_constant
					#self.entity_state.particle_drag_force[i][1] = self.entity_state.mass*self.entity_state.drag_constant

			#print("drag velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

		return