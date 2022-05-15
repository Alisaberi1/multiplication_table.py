n=int(input())
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	
	# Only want to loop through n
	while multiplier <= 9:
		result = number * multiplier  
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(n) 