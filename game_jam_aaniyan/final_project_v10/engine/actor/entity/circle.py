class circle:
	def __init__(self,center_point,radius,color,name='circle'):
	self.actions = []
	self.name = name
	self.verbose = False
	self.active = True
	self.radius = radius
	self.color = color
	self.center_point = center_point
	return

	def insert_action(self,action):
		action.entity_state = self
		self.actions.append(action)
		return 

