fruits = {"cherry", "melone", "pineapple","banana", "peach","apple", "pineapple", "cherry"}
print(type(fruits))


# even_numbers = set({2,4,6,16,64})
# print(even_numbers)
# print(even_numbers)

# for element in fruits:
#   print(element)

# even_numbers.add(100)
# print(even_numbers)

# combined_fruits_number = even_numbers.update(fruits)
# print(even_numbers)
# print(combined_fruits_number)
# print(even_numbers.update(fruits))

# cars = ["BMW", "Benz", "Toyota"]
# even_numbers.update(cars)
# print(even_numbers)

fruits.add("orange")
print(fruits)


print([element for element in fruits if element == "pineapple"])
