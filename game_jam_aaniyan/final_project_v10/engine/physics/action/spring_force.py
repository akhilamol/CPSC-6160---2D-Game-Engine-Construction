###
import pygame
import numpy 
import math
class spring_force_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='spring_force'
		return

	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False
		if data == False:
			return False
		return True

	def update_particle_center(self):
		local_x = numpy.array(self.entity_state.particle_position)[:,0]
		local_y = numpy.array(self.entity_state.particle_position)[:,1]
		#print("local_x = ", local_x, local_y)

		left_x = local_x[local_x<800]
		left_y = local_y[local_x<800]
		#print("left_x", left_x,left_y)

		# don't contribute to center of mass
		self.entity_state.center_point = [numpy.average(left_x), numpy.average(left_y)]
		return self.entity_state.center_point 

	def distance(self,pos,center):
		a = math.sqrt((pos[0] - center[0])*(pos[0] - center[0]) + (pos[1] - center[1])*(pos[1] - center[1]))
		return a 


	def act(self,data):
		if self.condition_to_act(data):

			if self.entity_state.spring_force_verbose == True:
				center = self.update_particle_center()
				#print("center  = ", center)

				for i in range(self.entity_state.particle_number):

					if self.entity_state.particle_position[i][0] <= 580:
						#if (i==0):
							#print("\ndistance = ", my_distance)
						self.entity_state.particle_spring_force[i][0] = self.entity_state.spring_constant*\
					                         (center[0]- self.entity_state.particle_position[i][0])
						self.entity_state.particle_spring_force[i][1] = self.entity_state.spring_constant*\
					                         (center[1]-self.entity_state.particle_position[i][1])
					#print("force = ", self.entity_state.particle_force)
					else:
						
						# no spring force on right side
						self.entity_state.particle_spring_force[i][0] = 0
						self.entity_state.particle_spring_force[i][1] = 0

				#print("spring velocity =", self.entity_state.particle_velocity[0][0], self.entity_state.particle_velocity[0][1])


		return