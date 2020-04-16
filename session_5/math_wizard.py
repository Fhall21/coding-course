def sum_of_two(num1, num2=2):
	# any logic
	return num1 + num2

def multiplyer(number_one, number_two):
	number_three = sum_of_two(number_one, number_two)
	return number_one * number_three

# *
print (sum_of_two(3))
# 6
print (sum_of_two(4,3))
# 12

print (sum_of_two(multiplyer(2,3), 4))

print (multiplyer(2,3))