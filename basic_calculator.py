import sys
 #Just a basic calculator program with user input.   
while True:
	first_value = "\nWhat is the first number? "
	second_value = "What is the second number? "
	
	
	
	def calc():
		message = "\nWhat kind of problem do you need solved?"
		message_1 = "\n Addition\n Subtraction\n Multiplication\n Exponent\n Division\nor type 'exit' when you are done."
		problem = input(message + message_1 + '\n<<<').lower()
		
		
		if problem == 'addition':
			addition()
		elif problem == 'subtraction':
			subtraction()
		elif problem == 'multiplication':
			multiplication()
		elif problem == 'division':
			division()
		elif problem == 'exponent':
			exponent()
		elif problem == 'exit':
			sys.exit()
		else:
			print("\nPlease use a defined message.")
		
				
	def addition():
		cont = "y"
		while cont != "n":
			maker = int(input(first_value))
			maker_1 = int(input(second_value))
			answer = maker + maker_1
			print("\nYour answer is : ", answer)
			cont = input("\nDo you want to add another set? \nEnter 'Y' to continue or 'n' to exit. \n>>>>  ").lower()
			if cont != "y" or "n":
				cont = input("Please enter either 'y' or 'n'.").lower
			
	def subtraction():
		cont = "y"
		while cont != "n":
			maker = int(input(first_value))
			maker_1 = int(input(second_value))
			answer = maker - maker_1
			print("\nYour answer is : ", answer)
			cont = input("\nDo you want to subtract another set? \nEnter 'y' to continue or 'n' to exit. \n>>>>  ").lower()
			if cont != "y" or "n":
				cont = input("Please enter either 'y' or 'n'.").lower
				
	def multiplication():
		cont = "y"
		while cont != "n":
			maker = float(input(first_value))
			maker_1 = float(input(second_value))
			answer = maker * maker_1
			print("\nYour answer is : ", answer)
			cont = input("\nDo you want to multiply another set? \nEnter 'y' to continue or 'n' to exit. \n>>>>  ").lower()
			if cont != "y" or "n":
					cont = input("Please enter either 'y' or 'n'.").lower()
					
	def division():
		cont = "y"
		while cont != "n":
			maker = float(input(first_value))
			maker_1 = float(input(second_value))
			answer = maker / maker_1
			print("\nYour answer is : ", answer)
			cont = input("\nDo you want to divide another set? \nEnter 'y' to continue or 'n' to exit. \n>>>>  ").lower()
			if cont != "y" or "n":
				cont = input("please enter either 'y' or 'n'.").lower()
				
	def exponent():
		cont = "y"
		while cont != "n":
			maker = int(input("What is the base number?"))
			maker_1 = int(input("To the power of what?"))
			answer = maker ** maker_1
			print("Your answer is: ", answer)
			cont = input("\nDo you want to exponent another set? \nEnter 'y' to continue or 'n' to exit. \n>>>>  ").lower()
			if cont != "y" or "n":
				cont = input("Please enter either 'y' or 'n'.").lower()
	
	
	calc()
	
