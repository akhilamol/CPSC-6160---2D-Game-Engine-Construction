###
import pygame
import math
class collide_action():
	def __init__(self,walls):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='collide'
		self.walls = walls
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return Falses
		if self.entity_state.active == False:
			return False

		return True


	def act(self,data):
		if self.condition_to_act(data):
			#print("collide before velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])


			for i in range(self.entity_state.particle_number):
				is_collide = False
				point = (self.entity_state.particle_position[i][0], self.entity_state.particle_position[i][1])
				#print("walls = ", self.walls, len(self.walls))
				for j in range(0,len(self.walls)):

					is_collide = is_collide or self.walls[j].collidepoint(point)

					#if (i==0):
						#print("i, j = ", i, j, self.walls[j], is_collide)
						#print("collide 2 velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

				self.entity_state.particle_is_collide[i] = is_collide
				
				if is_collide:
						#print("collide 3 velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])
					
					#print("\n\n collide happens i, j ======= ", i, j )
					self.entity_state.particle_velocity[i][0] = -1.0 * self.entity_state.particle_velocity[i][0]
					#self.entity_state.particle_spring_force[i][0] = 0
					#self.entity_state.particle_gravity_force[i][0] = 0
					#self.entity_state.particle_drag_force[i][0] = 0
					#print("collide 3.1 velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

					self.entity_state.particle_velocity[i][1] = -1.0 * self.entity_state.particle_velocity[i][1]

					#print("collide 4 velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

				
			#print("collide after velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])

				
		return




		return