#QUESTION 1
# price=int(input('Enter price of the item:'))
# if price>1000:
#     price=price-(price*0.10)
# elif price>500:
#     price= price-(price*0.05)
# print(f'final price is {price}')

#QUESTOIN 2
# choice = input("do you want vegetarian or non vegetarian? ").lower()
# if choice == "vegetarian":
#     dish = input("salad or pasta? ")
# elif choice == "non vegetarian":
#     dish = input("chicken or fish? ")
# print(f"You chose {dish}.")


#QUESTION 3
# salary = int(input("Enter monthly salary: "))
# if salary > 50000:
#     print("High Earner")
# elif salary > 20000:
#     print("Mid Earner")
# else:
#     print("Low Earner")


#QUESTOIN 4
# number = int(input("Enter a number: "))
# if number%2==0:
#     if number%5==0:
#         print("The number is divisible by both 2 and 5.")
#     else:
#         print("The number is divisible by 2 and not by 5")
# else:
#     print("The number is not divisible by 2.")


#QUESTION 5
# marks = int(input("Enter the student's marks: "))
# if marks>90:
#     print("Excellent")
# elif marks>50:
#     print("Good")
# else:
#     print("Fail")


#QUESTION 6
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if a >= b:
#     if a >= c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b >= c:
#         largest = b
#     else:
#         largest = c
# print(f"The largest number is: {largest}")


#QUESTOIN 7
# print("Welcome to the Forest Adventure!")
# path = input("will you go left or right? ").lower()
# if path == "left":
#     choice = input("will you explore or rest? ").lower()
#     if choice == "explore":
#         print("You found treasure!")
#     else:
#         print("Game Over.")
# else:
#     print("You fell into a trap. Game Over.")


#QUESTION 8
# print("Welcome to the Jungle Survival Challenge!")
# path=input("search for food or build a shelter? enter here:").lower()
# if path=="search for food":
#     choice=input("hunt or gather? :").lower()
#     if choice=="hunt":
#         print("You were attacked by a wild animal. Game Over.")
#     else:
#         print("You found enough food. You Win!")
# else:
#     print("Your shelter collapsed in the rain. Game Over.")


#QUESTION 9
# print("Welcome to the Space Adventure!")
# choice = input("Choose: land on Mars or fly to Jupiter? ").lower()
# if choice == "land on mars":
#     action = input("Choose: explore or build a base? ").lower()
#     if action == "explore":
#         print("You found alien artifacts. You Win!")
#     else:
#         print("You ran out of resources. Game Over.")
# else:
#     print("Your spaceship crashed. Game Over.")


#QUESTION 10
# print("Welcome to the Haunted Castle!")
# path=input("enter the castle or run away? ").lower()
# if path=="enter the castle":
#     door=input(" red, green, or black? ").lower()
#     if door=="red":
#         print("You entered a room full of flames. Game Over.")
#     elif door == "green":
#         print("You found the treasure. You Win!")
#     else:
#         print("You were captured by ghosts. Game Over.")
# else:
#     print("You escaped safely.")


#QUESTION 11
# print("Welcome to the Underwater World!")
# choice=input("dive deeper or surface? ").lower()
# if choice=="dive deeper":
#     action=input("search for pearls or chase the fish? ").lower()
#     if action=="search for pearls":
#         print("You found a rare pearl. You Win!")
#     else:
#         print("You got lost underwater. Game Over.")
# else:
#     print("You returned safely.")


#QUESTION 12
# print("Welcome to the Pirate Ship Adventure!")
# choice=input("search for treasure or battle enemy ships? ").lower()
# if choice=="search for treasure":
#     action=input("dig on the island or explore the cave? ").lower()
#     if action=="dig on the island":
#         print("You found a hidden treasure chest. You Win!")
#     else:
#         print("You were trapped inside. Game Over.")
# else:
#     action=input("attack or defend? ").lower()
#     if action=="attack":
#         print("You won the battle. You Win!")
#     else:
#         print("You were outnumbered. Game Over.")


#QUESTION 13
# print("Welcome to the Wizarding World")
# subject=input("spells or potions: ").lower()
# if subject == "spells":
#     choice = input("Practice magic or compete in duels: ").lower()
#     if choice == "practice magic":
#         print("You mastered a powerful spell. You Win!")
#     else:
#         print("You lost to a rival wizard. Game Over.")
# elif subject == "potions":
#     choice = input("Brew an elixir or create poison: ").lower()
#     if choice == "brew an elixir":
#         print("You healed a village. You Win!")
#     else:
#         print("Your potion backfired. Game Over.")


#QUESTION 14
# print("Welcome to the Cybersecurity Mission")
# hack= input("Trace the hacker or secure the system: ").lower()
# if hack== "trace the hacker":
#     task = input("Track their IP or decode their message: ").lower()
#     if task == "track their ip":
#         print("You caught the hacker. You Win!")
#     else:
#         print("The message was a trap. Game Over.")
# elif hack == "secure the system":
#     task = input("Shut down the server or upgrade the firewall: ").lower()
#     if task == "shut down the server":
#         print("The attack was stopped. You Win!")
#     else:
#         print("The hacker bypassed it. Game Over.")


#QUESTION 15
# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 7 == 0:
#     print("double seven")
# elif num % 2 == 0:
#     print("even")
# elif num % 7 == 0:
#     print("lucky seven")
# else:
#     print(num)


#QUESTION 16
# num = int(input("Enter a number: "))
# if num > 100:
#     print("big number")
# elif num >= 50:
#     print("medium number")
# else:
#     print("small number")


#QUESTOIN 17
# color = input("red \ngreen\nyellowEnter a color: ").lower()
# if color=="red":
#     print("Stop")
# elif color=="yellow":
#     print("Slow Down")
# elif color=="green":
#     print("Go")
# else:
#     print("Invalid Signal")


#QUESTONI 18
# temp=int(input("Enter temperature in Celsius: "))
# if temp>40:
#     print("Hot")
# elif temp>=20:
#     print("Warm")
# else:
#     print("Cold")

#QUESTION 19
# bmi=float(input("Enter your BMI: "))
# if bmi<18.5:
#     print("underweight")
# elif bmi < 24.9:
#     print("normal weight")
# elif bmi < 29.9:
#     print("overweight")
# else:
#     print("obesity")


#QUESTION 20
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# if num1%2==0 and num2%2==0:
#     print(num1 + num2)
# elif num1%2==0 or num2%2==0:
#     print(abs(num1 - num2))
# else:
#     print(num1 * num2)



#QUESTOIN 21
# price = int(input("Enter price: "))
# if price>1000:
#     print(price * 0.8)
# elif price >= 500:
#     print(price * 0.9)
# else:
#     print(price)


#QUESTION 22
# age=int(input("Enter age: "))
# gender=input("Enter gender (M/F): ").lower()
# income=int(input("Enter income: "))
# if age>=18 and age<60:
#     if gender=="m":
#         if income>1000000:
#             print("Tax:30%")
#         elif income>=500000:
#             print("Tax:20%")
#         else:
#             print("Tax:10%")
#     else:
#         if income>1000000:
#             print("Tax:25%")
#         elif income>=500000:
#             print("Tax:15%")
#         else:
#             print("Tax:5%")
# else:
#     if income>1000000:
#         print("Tax:20%")
#     else:
#         print("Tax:10%")


#QUESTION 23
# age = int(input("Enter age: "))
# gender = input("Enter gender (m/f): ").lower()
# score = int(input("Enter score: "))
# if 18 <= age <= 25:
#     if gender == "m":
#         if score >= 85:
#             print("full scholarship")
#         elif score >= 70:
#             print("partial scholarship")
#         else:
#             print("no scholarship")
#     else:
#         if score >= 80:
#             print("full scholarship")
#         elif score >= 65:
#             print("partial cholarship")
#         else:
#             print("no scholarship")


#QUESTION 24
# age=int(input("Enter age: "))
# gender=input("Enter gender (m/f): ").lower()
# experience=int(input("Enter experience inyears: "))
# if 21<=age<=35:
#     if gender=="m":
#         if experience >= 5:
#             print("senior developer")
#         else:
#             print("junior developer")
#     else:
#         if experience >= 5:
#             print("senior analyst")
#         else:
#             print("junior aalyst")
# else:
#     print("manager role")


#QUESTINO 25
# age=int(input("Enter age: "))
# gender=input("Enter gender (M/F): ").lower()
# show=input("Enter show type (morning/evening): ").lower()

# if age < 12:
#     if show == "morning":
#         ticket_price = 500
#     else:
#         ticket_price = 700
# elif age >= 12 and age < 60:
#     if gender == "m":
#         if show == "morning":
#             ticket_price = 800
#         else:
#             ticket_price = 1000
#     else:
#         if show == "morning":
#             ticket_price = 700
#         else:
#             ticket_price = 900
# else:
#     ticket_price = 600

# print(f"the ticket price is {ticket_price}")


#QUESTION 25
# age = int(input("Enter age: "))
# gender = input("Enter gender (m/f): ").upper()
# membership = input("Enter membership type (monthly/yearly): ").lower()

# if age >= 18 and age < 30:
#     if gender == "M":
#         if membership == "monthly":
#             membership_cost = 50
#         else:
#             membership_cost = 500
#     else:
#         if membership == "monthly":
#             membership_cost = 45
#         else:
#             membership_cost = 450
# elif age >= 30 and age <= 50:
#     if membership == "monthly":
#         membership_cost = 60
#     else:
#         membership_cost = 600
# else:
#     if membership == "monthly":
#         membership_cost = 40
#     else:
#         membership_cost = 400

# print(f"Membership cost is {membership_cost}")






