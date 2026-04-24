
# Defining Functions 

def sum (a,b):
	return (a+b)


def subtract (a,b):
	return (a-b)

def divide (a,b):
	return (a/b)

def int_divide (a,b):
	return (a//b)

def multiply (a,b):
	return (a*b)

def power (a, b):
	return (a**b)

def modulus (a, b):
	return (a%b)

# Defining Histroy Variable
history = []

# Defining Main Code
while True:
	c = input("Enter operation (+, -, *, /, %, ^, //) or 'exit': ")
	
	if c == "exit":
		print("Calculator quitting")
		break

	elif c == "history":
		#print(history)
		print(history[-5:][::-1])
		continue

	elif c == "^":
		try:
			a = float(input("Enter number: "))
			b = int(input("Enter power: "))
		except ValueError:
			print("Invalid input")
			continue
		result = power(a,b)
		print("Result:", result)
		history.append(result)
		continue

	elif c in ["+", "-", "*", "/", "%", "//"]:
		try:
			a = float(input("Enter first number: "))
			b = float(input("Enter second number: "))
		except ValueError:
			print("Invalid values entered")
			continue

	if c == "+":
		result = sum(a,b)
		print("Result:", result)
		history.append(result)

	elif c == "-":
		result = subtract(a,b)
		print("Result:", result)
		history.append(result)

	elif c == "*":
		result = multiply(a,b)
		print("Result:", result)
		history.append(result)

	elif c == "/":
		if b == 0:
                	print("Cannot divide by zero")
		else:
			result = divide (a,b)
			print("Result:", result)
			history.append(result)

	elif c == "//":
		if b == 0:
			print("Cannot divide by zero")
		else:
			result = int_divide(a,b)
			print("Result:", result)
			history.append(result)

	elif c == "%":
		if b == 0:
                	print("Cannot divide by zero")
		else:
			result = modulus(a,b)
			print("Result:", result)
			history.append(result)


	else:
        	print("Invalid operation")


