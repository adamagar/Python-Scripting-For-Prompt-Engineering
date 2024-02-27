def calculate_average(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum

numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))