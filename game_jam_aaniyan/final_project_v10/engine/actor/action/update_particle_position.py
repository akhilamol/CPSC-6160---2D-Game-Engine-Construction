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
		#print("condition," ,self.condition_to_act(data))
		if self.condition_to_act(data):
			#print("position before velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

			for i in range(self.entity_state.particle_number):
				# x2 = x1 + 1/2 a t^2
				#gravity_delta_y = 0.5*self.entity_state.particle_gravity_force[i][1]/self.entity_state.mass\
				#*data*data
				# x2 = x1 + v*t
				delta_x = self.entity_state.particle_velocity[i][0]*data
				delta_y = self.entity_state.particle_velocity[i][1]*data

				if delta_x > 20:
					delta_x = 5
				if delta_x < -20:
					delta_x = -5

				if delta_y > 20:
					delta_y = 5
				if delta_y < -20:
					delta_y = -5

				self.entity_state.particle_position[i][0] = self.entity_state.particle_position[i][0] \
				                                            + delta_x
				self.entity_state.particle_position[i][1] = self.entity_state.particle_position[i][1] \
															+ delta_y

				if self.entity_state.particle_position[i][0] < 0:
					self.entity_state.particle_position[i][0] = 10
				elif self.entity_state.particle_position[i][0] > 990:
					self.entity_state.particle_position[i][0] = 990

				if self.entity_state.particle_position[i][1] <10:
					self.entity_state.particle_position[i][1] = 10
				elif self.entity_state.particle_position[i][1]>790:
					self.entity_state.particle_position[i][1] =790

				if self.entity_state.particle_position[i][0] > 580 and self.entity_state.particle_position[i][0] < 600:
					if (self.entity_state.particle_position[i][1] >0 and self.entity_state.particle_position[i][1] < 300)\
						or (self.entity_state.particle_position[i][1] <800 and self.entity_state.particle_position[i][1] >500):
						self.entity_state.particle_position[i][0] = 580

				if self.entity_state.particle_position[i][0] > 580 and self.entity_state.particle_position[i][0] < 600 \
				and self.entity_state.particle_is_collide[i] == True:
					self.entity_state.particle_position[i][0] = 580

			#print("position after velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])
			#print("position after [pos] =", self.entity_state.particle_position[0][0], self.entity_state.particle_position[0][1])

				#if (i==0):				
					#print("position abs velocity =", self.entity_state.particle_velocity[0][1])


		return 