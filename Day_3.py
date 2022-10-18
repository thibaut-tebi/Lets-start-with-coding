# declaring multiple variables
matrix_1 = [1, 2, 3]
x, y, z = matrix_1
print(x)
print(y)
print(z)
print(type(matrix_1))
my_favourite_fruits = "mango", "apple", "orange"
fruit_1, fruit_2, fruit_3 = my_favourite_fruits
print(fruit_2 + " is my favourite fruit of alltime but sometimes i prefer " + fruit_1 + " and " + fruit_3 + " as well!!")
print(type(my_favourite_fruits))

# defining variables
def func():
    my_favourite_fruits = "grape"
    print(my_favourite_fruits + " is good")
func()

print(my_favourite_fruits)


