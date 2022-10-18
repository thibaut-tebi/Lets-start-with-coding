# data types
nun_char= len(input("what is your name?"))
print("the total number of character in your name is " + str(nun_char))
number= print(int("35"[0])+ int("35"[1]))

#DAY 3 PROJECT: making clinical decisions based on BMI value of patient

height= float(input("Enter your height:"))
weight= float(input("Enter your weight:"))
BMI= weight/height**2
BMI_as_approx=round(BMI,2)
print(" Your BMI value is " + str(BMI_as_approx) + " and,")
if BMI_as_approx < 18.5:
   print("  your  are UNDERWEIGHT")
elif BMI_as_approx > 18 and BMI_as_approx<25:
    print("you are NORMAL WEIGHT")
elif BMI_as_approx >25 and BMI_as_approx <30:
    print("you are OVERWEIGHT")
elif BMI_as_approx > 30 and BMI_as_approx<35:
    print("you are OBESE")
else:
    print("you are CLINICALLY OBESE")

#DAY 3 PROJECT 2: checking leap years

year= int(input("Enter your prefer year:"))
if year % 4==0:
    if year % 100 == 0:
      if year % 400 == 0:
       print("This is a leap year.")
      else:
         print(" This is not leap year.")
    else:
        print("this is not a leap year.")
else:
    print("this is not a leap year.")

#DAY 3 PROJECT 3: calculating the price based on height, age and the price of a roller coaster.

height= int(input("enter your height in cm:"))
if height >= 120:
    print("you can ride the roller coaster")
    age=int(input("Enter your age:"))
    if age < 12:
        bill= 5
        print("your cost is $5")
    elif age >=12 and age <=18:
        bill= 7
        print("your cost is $ 7")
    elif age > 18:
        bill=12
        print("your cost is $ 12")
    photo=input("Enter yes or no for photo:")
    if photo== "yes"
       total_bill= bill +3
        print("your total bill is $ " + str(total_bill))
    else:
        print( "your total bill is $" +str(bill))
else:
    print("you can not ride the roller coaster")

#DAY 3 PROJECT 4...PIZZA******
print("welcome to Tebi's PIZZA!")
PIZZA_size= input("enter the size of PIZZA you want, select, S,M,L:")
if PIZZA_size == "S":
    price= 15
elif PIZZA_size == "M":
    price=20
else:
    price = 25

type_of_pepper= "Y"

if type_of_pepper== "Y":
    if PIZZA_size== "S":
     price += 2
else:
    price+=3

extra_cheese= "Y"
if extra_cheese=="Y":
    price+=1
print("your final bill is " + str(price))

#DAY 3 PROOJECT 5. The love calculator.

love_calculator= print("welcome to my love calculator.")
name1=input("enter your name:\n")
name2=input("enter your partners name:\n")
name= name1 + name2

lowercase_name= name.lower()

t=lowercase_name.count("t")
r=lowercase_name.count("r")
u=lowercase_name.count("u")
e=lowercase_name.count("e")
true=t+r+u+e

l=lowercase_name.count("l")
o=lowercase_name.count("o")
v=lowercase_name.count("v")
e=lowercase_name.count("e")
love=l+o+v+e

love_score= true + love
if love_score<10 or love_score>90:
   print(f"your love score is {love_score}, and you go together like coke and mentos")
elif love_score>10 and love_score<40:
   print(f"your love score is {love_score}, your relationship cant move forward, please stop!")
elif love_score>40 and love_score<50:
    print(f"your love score is {love_score}, you are alright together")
else:
   print(f"your love score is {love_score}, you can stay forever!")


#DAY 3 PROJECT 6: Creating a game.

print("welcome to the treasure island\n")

print('''



print("Your mission is to find the treasure!\n")
choice1 = input("You're at a cross road, where do you want to go? 'left' or 'right':\n").lower()
if choice1 == "left":
    choice2 = input("You can now continue your journey! would you like to 'swim' or 'wait':\n").lower()
    if choice2 == "wait":
        choice3 = input("You have made the right choice!, choose between the colour 'blue', 'red' and 'yellow':\n").lower()
        if choice3 == "yellow":
            print("you win!")
        elif choice3 == "red":
            print("burned by fire. GAME OVER!")
        elif choice3 == "blue":
            print("eaten by shark. GAME OVER!")
        else:
            print("GAME OVER")
#else:
    print("you fell in a pool of fire,GAME OVER!")


#DAY 2 PROJECT: calculating the number of weeks left after my age.

age = int(i+nput("What is your current age?"))
age_int= int(age), can also be used
age_remaining= 90-age
weeks_remaining= age_remaining *52
days_remaining= age_remaining *365
message = print("you have " + str(months_remaining) +" months " + ","+ str(weeks_remaining)+" weeks " + " and " + str(days_remaining) +" days remaining to live on earth.")

modulus; odd numbers give a remender of 1 when divided by 2 and even numbers give 0 when divided by 2.

number= int(input("Enter your number:"))
    print("this is an even number.")
else:
    print("this is an odd number.")
