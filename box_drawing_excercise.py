design= "+ - - - - + - - - - +"
spaces= "/         /         /"

def print_four(f):
	f()
	f()
	f()
	f()

def print_spaces():
	print(spaces)

def print_design():
	print(design)


print_design()
print_four(print_spaces)
print_design()
print_four(print_spaces)
print_design()