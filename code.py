name = input("Enter your real name:")
print(name.upper())
favourite_colour = input(" Enter favourite_colour")
print(favourite_colour.upper())
print("my name is " + name + " and my favourite colour is" + favourite_colour)
date_of_birth = input("Enter your current date of birth")
print(date_of_birth.replace("current", "actual"))
age = 2022 - int(date_of_birth)
print(float(age))
if age <= 25:
    print(" you are eligible")
else:
    print("not eligible")
