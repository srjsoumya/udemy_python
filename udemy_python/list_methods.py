# Add a single item to list
names=["aray","jon","sercie","sansa"]
names.append("dragon")
print(names)

# Add multiple item to list
fruits=["apple","orange"]
fruits.extend(["banana","mango","melon"])
print(fruits)

# Add item to a perticular index
fruits=["apple","orange"]
fruits.insert(1,"banana")
print(fruits)
fruits.insert(-1,"melon")
print(fruits)

# clear the list
numbers=[1,2,3,4]
numbers.clear()
print(numbers)

# remove a item on specific index
numbers=[1,2,3,4,5]
last_element=numbers.pop() # Remove the last element
print(numbers)
print(last_element)

pop_item=numbers.pop(3)
print(numbers)
print(pop_item)

# Removes a specific item
colors=["orange","blue","red","black"]
colors.remove("red")
print(colors)

# Get the index of a element
items=["cup","mug","glass","pen","mug","paper","pencil","pen","pen"]
print(items.index("pen")) #index start from 0 to end
print(items.index("pen",4)) #index start from 4 to end

#Sort a list
items=["cup","mug","glass","pen","mug","paper","pencil","pen","pen"]
items.sort()
print(items)


