# This is a global attribute of the python animal class.
session = "Python Classes"

# Python allows us to create classes with the introcution of 
# a minimal amount of syntax
class Animal:

	# An Attribute of the class 
	class_name = "Animal Class"

	def __init__(self, species = "Not Set", colour = "Not Set", noise = "Not Set"):
		self.species = species
		self.colour = colour
		self.noise = noise

	# This is a class method, but also a python function
	def return_species(self):
		return self.species

	# The use of the key word self tells us that this is a method of the class
	def return_colour(self):
		return self.colour

	# We can point to the noise value for this class instance using self
	def return_noise(self):
		return self.noise

	def set_species(self, species):
		self.species = species

	def set_colour(self, colour):
		self.colour = colour

	def set_noise(self, noise):
		self.noise = noise

	# In this method we point to other methods defined in this classes instance 
	def print_info(self):
		print("I'm a " + self.return_species() + " and I go " + self.return_noise())

# Create a cow and duck Animal Instance with different variables
cow = Animal("Cow", "Brown", "Moo")
duck = Animal("Duck", "Green", "Quack")

cow.print_info()
duck.print_info()

 # View an attribute of the class
#print(cow.class_name)
#print(duck.class_name)

# # Update an attribute of the class
duck.class_name = "Duck Class"
print(cow.class_name)
print(duck.class_name)
print(duck.species)

# # Just another class with a method 
class SuperPower:

	def return_power(self):
		return "Squeal!"

# The Pig Class inherits Animal and Super Power
class Pig(Animal, SuperPower): 

	# The __ notation tells us this variable is private to the class 
	__private_pig_variable = "I'm actually a duck"

	# Here we overwrite the print_info method found in animal 
	def print_info(self):
		print("I'm a " + self.return_species() + " and I go " + self.return_noise() + ". My Super power is " + self.return_power())

	# Here we overwrite the base class set noise method but invoke it with Super 
	def set_noise(self, noise):
		print("Setting the Pig Noise!")
		super().set_noise(noise)

# Create a Pig Class instance, inherits both animal and super power ...
pig = Pig("Pig", "Pink", "Oink")
pig.print_info()

# Try to pritn the private variable
#print(pig.__private_pig_variable)

# # We can set attributes for a class instance .. 
pig.private_pig_variable = "I'm actually a duck"
print(pig.private_pig_variable)

# Over write the noise of the pig
pig.set_noise("Oink Oink!")
pig.print_info()