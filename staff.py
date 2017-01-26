class Employee(object):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "My name is {}".format(self.name)


