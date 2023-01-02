###
import pygame
class update_particle_velocity_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='update_velocity_position'
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
		#print("condition," ,self.condition_to_act(data))
		if self.condition_to_act(data):
			for i in range(self.entity_state.particle_number):
				# v2 = v1 + a*t\

				self.entity_state.particle_velocity[i][0] = self.entity_state.particle_velocity[i][0] +\
						self.entity_state.particle_gravity_force[i][0]/self.entity_state.mass*data +\
						self.entity_state.particle_spring_force[i][0]/self.entity_state.mass*data +\
						self.entity_state.particle_drag_force[i][0]/self.entity_state.mass*data

				self.entity_state.particle_velocity[i][1] = self.entity_state.particle_velocity[i][1] \
				 + self.entity_state.particle_gravity_force[i][1]/self.entity_state.mass*data+\
						self.entity_state.particle_spring_force[i][1]/self.entity_state.mass*data+\
						self.entity_state.particle_drag_force[i][1]/self.entity_state.mass*data

				if (i==0):
					print("abs velocity =", self.entity_state.particle_velocity[0][1])
				if abs(self.entity_state.particle_velocity[i][0]) > 100:
					self.entity_state.particle_velocity[i][0] = 0.0
				if abs(self.entity_state.particle_velocity[i][1]) > 100:
					self.entity_state.particle_velocity[i][1] = 0.0

		return 