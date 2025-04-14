# Create an empty list called my_list
my_list = []

# Append following elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position (index 1) in the list
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 30 in the list
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")

# Output the final list
print("Final list:", my_list)
