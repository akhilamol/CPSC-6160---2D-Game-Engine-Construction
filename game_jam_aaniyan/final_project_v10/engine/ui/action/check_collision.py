###
class check_collision_action():
	def __init__(self):
		self.types = ['loop']
		self.entity_state = None 
		self.verbose = False
		self.name ='check_collision'
		self.children=[]
		self.color= None
		return

	def insert_child(self,child):
		self.children.append(child)


	def condition_to_act(self,data):
		if self.entity_state == None:
			return False
		if self.entity_state.active == False:
			return False

		upper_bound = self.entity_state.bounds[1]
		lower_bound = self.entity_state.bounds[1]+self.entity_state.bounds[3]

		for child_button in self.entity_state.children_button:
			if child_button.active == True:

				child_button_upper_bound = child_button.bounds[1]
				child_button_lower_bound = child_button.bounds[1]+child_button.bounds[3]
				if child_button_lower_bound < lower_bound and child_button_upper_bound > upper_bound and child_button.bounds[0]<0:
					self.color =child_button.color
					return True
		return False

	def act(self,data):
		if self.condition_to_act(data):	
			print("Collision")
			for child in self.children:
				child.act(self.color)	
		return
