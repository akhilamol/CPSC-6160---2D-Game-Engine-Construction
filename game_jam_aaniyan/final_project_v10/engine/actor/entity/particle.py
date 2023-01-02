import random

class particles_entity:
	def __init__(self,initial_velocity,spring_constant, gravity_constant, drag_constant,bounds,number,radius = 5, mass = 1, name='particles'):
		self.actions = []
		self.spring_constant = spring_constant
		self.gravity_constant = gravity_constant
		self.drag_constant = drag_constant
		self.initial_velocity=initial_velocity
		self.name = name
		self.number = number
		self.bounds = bounds
		self.verbose = False
		self.active = True
		self.center_point = None
		self.particle_position = []
		self.particle_velocity = []
		self.particle_spring_force = []
		self.particle_gravity_force = []
		self.particle_drag_force = []
		self.particle_is_collide =[]
		self.particle_color = []
		self.particle_number = number
		self.radius = radius
		self.mass = mass
		self.gravity_force_verbose = True
		self.spring_force_verbose = True
		#self.particles_force = []
		self.add_particles(number)

		return

	def insert_action(self,action):
		action.entity_state = self
		#self.actions.append(action)

		return 


	def random_position(self):
		x_pos = self.bounds[0]+int(self.bounds[2]*random.random())
		y_pos = self.bounds[1]+int(self.bounds[3]*random.random())

		#return [x_pos,y_pos]
		return [x_pos+20,y_pos]

	def random_color(self):
		red = int(255.0*random.random())
		green = int(255.0*random.random())
		blue = int(255.0*random.random())

		return (red, green, blue)

	def add_particles(self,number):
		self.number = number
		for i in range(number):
			#self.particle_position.append([100,100])
			self.particle_position.append(self.random_position())
			self.particle_velocity.append([1.0,0.0])
			self.particle_gravity_force.append([0,0])
			self.particle_spring_force.append([0,0])
			self.particle_drag_force.append([0,0])
			self.particle_color.append(self.random_color())
			self.particle_is_collide.append(False)

		#print(self.particle_velocity)

		return



