# Create list and get 10 values for list
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
for i in range(10):
	numbers1[i] = int(numbers1[i]) 

# Print original list
print("The original list:", numbers1)

# New list for even numbers
evenList = []

# Get even numbers from list
evenList.append(numbers1.pop(0))
evenList.append(numbers1.pop(1))
evenList.append(numbers1.pop(2))
evenList.append(numbers1.pop(3))
evenList.append(numbers1.pop(4))

# Print updated list and even list
print("The list numbers now: ", numbers1)
print("The list for even index elements:", evenList)