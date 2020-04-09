
# Def introduces the function definition key word
# Note that we have indentation, keeps things tidy, reduces brackets 
def my_func():
	"I'm some doc string, I can describe the function"
	pass # TODO Skeleton Function

my_func()

# More interesting feature, default vaules and local variable assignment, we use this alot in foragg testing
def create_name(passed_name="Bob"):
	"Function to create the name variable"
	name = passed_name
	#print("The passed in name: ", name)


# Call create_name twice then try to print the local name variable 
create_name("Ben")
create_name()
#print(name)

# Introducing return
def square(value):
	"Returns the squared value of the number passed in"
	return value ** 2

square_3 = square(3)
print(square_3)


""" There are 3 ways to call a function """

#Lots of Default Values
def amazing_function(age=26, name="Bob", company="ACompany"):
	print(age, name, company)

# Only give the mandatory argument
amazing_function("20")
# Giving one or two values, note the order!
amazing_function(name="Ben", age="25")
# Call all function variables
amazing_function(name="Ben", company="ACompany2", age="25")

""" Default values are evaluated at the point of function definition """

i = 5 

def f(arg=i):
	print(arg)

i = 6
# This will print 5, not 6
f()

""" Good Doc String """

def good_function(arg1, arg2):
	"""
	This line should be a short summary.
	
	Now here we can enter a much more detailed documentation
	of what the function actually does across multiple lines
	"""
	return arg1 + arg2

print(good_function.__doc__)