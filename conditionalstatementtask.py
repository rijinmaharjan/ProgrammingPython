#QUESTION 1
# a=int(input('ENTER ANOTHER NUMBER))
# b=int(input('ENTER ANOTHER NUMBER))
# tem=a
# print(f'The value of a is {a} and b is {b} ')
# a=b
# b=tem
# print(f' The valu of a is {a} and b is {b} after swapping')


#QUESTION 2
# print('WELCOME TO TREASURE LAND')
# print('THE GAME STATS NOW')
# direc=input('DO YOU WANT TO GO LEfT OR RIGHT? \n TYPE IT HERE: ').lower()
# if direc=='right':
#     print('GAME OVER')
# elif direc=='left':
#     sw=input('Congrats you move on. \n Now do you want to swim or wait? \n TYPE IT HERE: ').lower()
#     if sw=='swim':
#         print('Game over')
#     elif sw=='wait':
#         colour=input('Congrats you move on. \n Now choose a colour between red yellow and blue: ').lower()
#         if colour in ['red','blue']:
#             print('Game over')
#         elif colour=='yellow':
#             print('You win')
#         else:
#             print('invalid choice')   
#     else:
#         print('invalid choice')   
# else:
#     print('invalid choice')   

         
#QUESTION 3
# x=int(input('ENTER A NUMBER: '))
# if x>=0:
#     if x==0:
#         print('ZERO')
#     else:
#         print('POSITIVE')
# else:
#     print('NEGATIVE')        


#QUESTION 4
# x=int(input('ENTER A NUMBER: '))
# if x%2==0:
#     print(f'THE NUMBER {x} is even')
# else:
#     print(f'THE NUMBER {x} is odd') 


#QUESTION 5
# sub1=int(input('Enter first subject marks: '))
# sub2=int(input('Enter second subject marks: '))
# sub3=int(input('Enter third subject marks: '))
# sub4=int(input('Enter fourth subject marks: '))
# total=sub1+sub2+sub3+sub4
# print(f'The total marks is {total}')
# per= (total*100)/4
# print(f'The percentage is {per}%')
# if per>=70 and per <=100:
#     print('distinction')
# elif per>=60 and per<70:
#     print('first div')
# elif per>=40 and per<60:
#     print('pass')
# elif per<40:
#     print('fail')
# else:
#     print('invalid marks')


#QUESTION 6
# bike=int(input('Enter the prince of the bike : '))
# if bike>100000:
#     tax=(bike*15)/100
#     print(f'The tax on bike is {tax}')
# elif bike>50000 and bike<=100000:
#     tax=(bike*10)/100
#     print(f'The tax on bike is {tax}')
    
# elif bike<=50000:
#     tax=(bike*5)/100
#     print(f'The tax on bike is {tax}')
# else:
#     print('invalid amount')
    

#QUESTION 7
# per1=int(input('Enter first age: '))
# per2=int(input('Enter second age: '))
# per3=int(input('Enter third age: '))
# per4=int(input('Enter fourth age: '))
# youngage=per1
# if per2<youngage:
#     youngage=per2
# if per3<youngage:
#     youngage=per3
# if per4<youngage:
#     youngage=per3
# print(f'The youngest age is {youngage}')


#QUESTION 8
# per1=int(input('Enter first age: '))
# per2=int(input('Enter second age: '))
# per3=int(input('Enter third age: '))
# per4=int(input('Enter fourth age: '))
# oldage=per1
# if per2>oldage:
#     oldage=per2
# if per3>oldage:
#     oldage=per3
# if per4>oldage:
#     oldage=per3
# print(f'The youngest age is {oldage}')


#QUESTION 9
# per=int(input('Enter first subject marks: '))
# if per>=80 and per <=100:
#     print('A+')
# elif per>=60 and per<80:
#     print('A')
# elif per>=50 and per<60:
#     print('B+')
# elif per>=45 and per<50:
#     print('B')
# elif per>=25 and per<45:
#     print('C')
# else:
#     print('D')


#QUESTION 10
# bon=int(input('Enter the prince of the bike : '))
# if bon>10:
#     print('The bonus is 10%')
# elif bon>=6 and bon<=10:
#     print(f'The bonus is 8%')
    
# elif bon<6:
#     print('The bonus is 5% ')
# else:
#     print('invalidexp')


#QUESTION 11
# day=int(input('Enter days: '))
# if day>=2 and day<6:
#     cost=day*2
#     print(f'The cost is {cost} ')
# elif day >=6 and day<=10:
#     cost=day*3
#     print(f'The cost is {cost} ')
# elif day>10 and day<=15:
#     cost=day*4
#     print(f'The cost is {cost} ')
# else:
#     cost=day*5
#     print(f'The cost is {cost} ')


#QUESTION 12

# service=int(input('total service years: '))
# if service > 5:
#     salary=int(input('What is your salary: '))
#     bonus=salary*5/100
#     print(f'The bonus is {bonus}')
# else:
#     print('WORK MORE YEARS')


#QUESTION 13
# radius=int(input('Enter radius: '))
# area=3.14*radius*radius
# print(f'The area is {area}')


#Question 14
# stud=int(input('Enter number of students in first class:'))
# stud2=int(input('Enter number of students in second class:'))
# stud3=int(input('Enter number of students in third class:'))

# desk2=(stud2/2)
# desk3=(stud3/2)
# if stud%2==0:
#     desk=(stud//2)
#     print(f'The minimum amount of desk required for {stud} students is {desk}')
# else:
#     desk=(stud//2)+1
#     print(f'The minimum amount of desk required for {stud} students is {desk}')
# if stud2%2==0:
#     desk2=(stud2//2)
#     print(f'The minimum amount of desk required for {stud2} students is {desk2}')
# else:
#     desk2=(stud2//2)+1
#     print(f'The minimum amount of desk required for {stud2} students is {desk2}')
# if stud3%2==0:
#     desk3=(stud3//2)
#     print(f'The minimum amount of desk required for {stud3} students is {desk3}')
# else:
#     desk3=(stud3//2)+1
#     print(f'The minimum amount of desk required for {stud3} students is {desk3}')
# tdesk=desk+desk2+desk3
# print(f'Total required desk is {tdesk}')



#QUESTION 15
# stud=int(input('Enter number of students:'))
# apl=int(input('Enter number of apples:'))
# if apl%stud==0:
#     aplforstud=apl//stud
#     print(f"Each student will get {aplforstud} apples with no apples left in the basket.")

# else:
#     aplforstud=apl//stud
#     leftapl=apl%stud
#     print(f"Each student will get {aplforstud} apples with {leftapl} remaning in the basket.")


#QUESTION 16
# age=int(input('ENTER YOUR AGE TO CHECK ELIGIBILITY:'))
# if age>0 and age<18:
#     print('You need to be 18 to be eligible to vote.')
# elif age>18:
#     print('You are eligible to vote')
# else:
#     print('You entered a invalid age')


#QUESTION 17
# city=input('enter a city \n1.delhi \n2.agra \n3.jaipur \ntype it here:').lower()
# if city=='delhi':
#     print(f'the monument in {city} to watch is RED FORT')
# elif city=='agra':
#     print(f'the monument in {city} to watch is TAJ MAHAL')
# elif city=='jaipur':
#     print(f'the monument in {city} to watch is JAL MAHAL')
# else:
#     print('invalid city')


#QUESTION 18
# nu=int(input('Enter a number:'))
# if nu%2==0 and nu%3==0:
#     print(f'The number {nu} is divisible by both 2 and 3')
# else:
#      print(f'The number {nu} is not divisible by 2 or 3')


#QUESTION 19
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# oper=input('Enter a operator +,-,*,/:')
# if oper=='+':
#     print(F'The sum of {a} and {b} is {a+b}')
# elif oper=='-':
#     print(F'The difference of {a} and {b} is {a-b}')
# elif oper=='*':
#     print(F'The mul of {a} and {b} is {a*b}')
# elif oper=='/':
#     print(F'The div of {a} and {b} is {a/b}')
# else:
#     print('invalid operator')


#QUESTION 20
# total=int(input('Total number of class:'))
# abs=int(input('Total absent days:'))
# pres=total-abs
# per=(pres*100)/total
# if per<75 :
#     print(f'You will not be able to sit in exam. Your attendance percentage is {per}%')
# else:
#     print(f'You will be able to sit in exam. Your attendance percentage is {per}%')


#QUESTION 21
# per=int(input('Enter percentage: '))
# if per>=64 and per <=100:
#     print('Excellent')
# elif per>=55 and per<65:
#     print('Good')
# elif per>=40 and per<55:
#     print('Fair')
# else:
#     print('Fail')


#QUESTION 22
# age=int(input('Enter age: '))
# gen=input('Enter gender M or F').lower()
# if age>=18 and age<30:
#     if gen=='m':
#         print('Your wage per day is 700')
#     elif gen=='f':
#         print('Your wage per day is 750')
#     else:
#         print('INVALID GENDER INPUT')
# elif age>=30 and age<=40:  
#     if gen=='m':
#         print('Your wage per day is 800')
#     elif gen=='f':
#         print('Your wage per day is 850')
#     else:
#         print('INVALID GENDER INPUT')
# else:
#     print('Invalid age')


#QUESTION 23
# a = True
# b = True
# c = True
# d = True
# print(c)
# print(d)
# print(not a)
# print(not b)
# print(not c)
# print(not d)
# print(a and b)
# print(a or b)
# print(a and b or c)
# print(not a or b or c)
# print(not a or not b or not c)
# print(not(not a or not b or not c))


#QUESTION 24
# a=int(input('Enter a number:'))
# if a%5==0:
#     if a%3==0:
#         print('FizzBuzz')
#     else:
#         print('buzz')
# elif a%3==0:
#     print('fizz')
# else:
#     print(F'the number is {a}')


#QUESTION 25
# user='admin'
# pasw='password123'
# username=input('USERNAME: ')
# password=input('PASSWORD: ')
# if username==user and pasw==password:
#     print('ACCESS GRANTED')
# else:
#     print('INCORRECT PASSWORD OR USERNAME')


#QUESTION 26
# num1=int(input('Enter first number:'))
# num2=int(input('Enter second number:'))
# if num1>=num2:
#     if num1==num2:
#         print('both numbers are equal')
#         if num1>0:
#             print('The numbers are positive')
#         elif num1==0:
#             print('The numbers are zero') 
#         else:
#             print('The number is negative')       
#     else:
#         print(f'{num1} is greater than {num2}')
# else:
#     print(f'{num2} is greater than {num1}')


#QUESTION 27
# marks=int(input('Enter marks: '))
# if marks>=90 and marks<=100:
#     print('Congrats')
# elif marks>=50 and marks<90:
#     print('You can imporve')
# else:
#     print('retake the course')


#QUESTION 28
# age=int(input('Enter your age:'))
# degree=input('do you have a degree? (yes/no):').lower()
# exp=int(input('Enter your years of experience:'))
# if age>=18 and degree=='yes':
#     if exp>3:
#         print('highly Eligible.')
#     elif xp<=3 and exp>=1:
#         print('Eligible.')
#     else:
#         print("Under Review.")
# else:
#     print('NOT QUALIFIED')        


#QUESTION 29
# w = int(input("Enter the weight of package: "))
# u = input("urgent delivery? (yes/no): ").lower()
# if w < 5:
#     cost = 5
# elif 5 <= w <= 20:
#     cost = 10
# else:
#     cost = 20
# if u == "yes":
#     cost += 5
# print(f'The cost is {cost}.')


#QUESTION 30
# salary=int(input('Enter your salary :'))
# cred=int(input('Enter your credit score: '))
# if salary>=50000:
#     if cred>=700:
#         print('eligible')
#     elif cred>=600 and cred<700:
#         print('Your loan is approved with higher interest') 
#     else:
#         print('not enough credit score. not approved')
# else:
#     print('not eligible. not enough salary')


#QUESTOIN 31
# weather=input('Is it sunny or rainy outside:').lower()
# if weather=='sunny':
#     print('I recommend outdoor activities like a picnic if its sunny today')
# elif weather=='rainy':
#     rain=input('Do you have a raincoat or an umbrella? yes/no:').lower()
#     if rain=='yes':
#         print('You can go to a mall or a museam nearby')
#     else:
#         print('stay home and watch movie')
# else:
#     print('weather not valid')


#QUESTION 32
# print('WELCOME TO THE HAUNTED HOUSE')
# print('THE GAME STARS NOW')
# direc = input('DO YOU WANT TO GO UPSTAIRS OR DOWNSTAIRS? \nTYPE IT HERE: ').lower()
# if direc == 'downstairs':
#     print('GAME OVER')
# elif direc == 'upstairs':
#     sw = input('Congrats you move on. \nNow do you want to enter the room or stay outside? \nTYPE IT HERE: ').lower()
#     if sw == 'enter the room':
#         print('GAME OVER')
#     elif sw == 'stay outside':
#         creature = input('Congrats you move on. \nNow choose between ghost, vampire, or werewolf: ').lower()
#         if creature in ['ghost', 'vampire']:
#             print('GAME OVER')
#         elif creature == 'werewolf':
#             print('YOU WIN')
#         else:
#             print('INVALID CHOICE')
#     else:
#         print('INVALID CHOICE')
# else:
#     print('INVALID CHOICE')


#QUESTION 33
# print('WELCOME TO THE JUNGLE ADVENTURE')
# print('THE GAME STARS NOW')
# direc = input('DO YOU WANT TO GO LEFT OR RIGHT? \nTYPE IT HERE: ').lower()
# if direc == 'right':
#     print('GAME OVER')
# elif direc == 'left':
#     sw = input('Congrats you move on. \nNow do you want to climb a tree or explore the cave? \nTYPE IT HERE: ').lower()
#     if sw == 'climb a tree':
#         print('GAME OVER')
#     elif sw == 'explore the cave':
#         creature = input('Congrats you move on. \nNow choose between bear, tiger, or snake: ').lower()
#         if creature in ['bear', 'tiger']:
#             print('GAME OVER')
#         elif creature == 'snake':
#             print('YOU WIN')
#         else:
#             print('INVALID CHOICE')
#     else:
#         print('INVALID CHOICE')
# else:
#     print('INVALID CHOICE')


#QUESTION 34
# print('WELCOME TO THE MAGIC FOREST')
# print('THE GAME STATS NOW')
# direc = input('DO YOU WANT TO GO NORTH OR SOUTH? \nTYPE IT HERE: ').lower()
# if direc == 'south':
#     print('GAME OVER')
# elif direc == 'north':
#     sw = input('Congrats you move on. \nDo you want to cross the river or follow the path? \nTYPE IT HERE: ').lower()
#     if sw == 'cross the river':
#         print('GAME OVER')
#     elif sw == 'follow the path':
#         creature = input('Congrats you move on. \nNow choose between fairy, ogre, or elf: ').lower()
#         if creature in ['ogre', 'fairy']:
#             print('GAME OVER')
#         elif creature == 'elf':
#             print('YOU WIN')
#         else:
#             print('INVALID CHOICE')
#     else:
#         print('INVALID CHOICE')
# else:
#     print('INVALID CHOICE')


#QUESTION 35
# print('WELCOME TO THE SPACE MISSION')
# print('THE GAME STATS NOW')
# direc = input('DO YOU WANT TO GO TO THE MOON OR TO MARS? \nTYPE IT HERE: ').lower()
# if direc == 'to mars':
#     print('GAME OVER')
# elif direc == 'to the moon':
#     sw = input('Congrats you move on. \nDo you want to land on the surface or stay in orbit? \nTYPE IT HERE: ').lower()
#     if sw == 'land on the surface':
#         print('GAME OVER')
#     elif sw == 'stay in orbit':
#         object = input('Congrats you move on. \nNow choose between alien, asteroid, or satellite: ').lower()
#         if object in ['alien', 'asteroid']:
#             print('GAME OVER')
#         elif object == 'satellite':
#             print('YOU WIN')
#         else:
#             print('INVALID CHOICE')
#     else:
#         print('INVALID CHOICE')
# else:
#     print('INVALID CHOICE')


#QUESTION 36
# print('WELCOME TO THE PIRATE ISLAND')
# print('THE GAME STATS NOW')
# direc = input('DO YOU WANT TO GO LEFT OR RIGHT? \nTYPE IT HERE: ').lower()
# if direc == 'right':
#     print('GAME OVER')
# elif direc == 'left':
#     sw = input('Congrats you move on. \nDo you want to dig for treasure or sail the ship? \nTYPE IT HERE: ').lower()
#     if sw == 'dig for treasure':
#         print('GAME OVER')
#     elif sw == 'sail the ship':
#         creature = input('Congrats you move on. \nNow choose between shark, pirate ship, or mermaid: ').lower()
#         if creature in ['shark', 'pirate ship']:
#             print('GAME OVER')
#         elif creature == 'mermaid':
#             print('YOU WIN')
#         else:
#             print('INVALID CHOICE')
#     else:
#         print('INVALID CHOICE')
# else:
#     print('INVALID CHOICE')
