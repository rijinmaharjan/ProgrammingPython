# day =int(input('Enter value day:'))
# if day==1:
#     print('sunday')
# elif day==2:
#     print('monday')
# elif day==3:
#     print('tuesday')
# elif day==4:
#     print('wednesday')
# elif day==5:
#     print('thursday')
# elif day==6:
#     print('friday')
# elif day==7:
#     print('saturday')
# else:
#     print('invalid input')


#QUESTION 1
# a=int(input('Enter value for a:'))
# b=int(input('Enter value for b:'))
# if a==b:
#     print(1)
# elif a>b:
#     print(2)
# else:
#     print(3)


#QUESTION 2
# a=int(input('Enter value to check even or odd:'))
# if a%2==0:
#     print(F'the entered value {a} is even')
# else:
#     print(F'the entered value {a} is odd')


#QUESTION 3:
# month_val=int(input('Enter value from 1 to 12 to display month:'))
# if month_val>=1 and month_val<=12:
#     if month_val==1:
#         print('january')
#     elif month_val==2:
#         print('february')
#     elif month_val==3:
#         print('march')
#     elif month_val==4:
#         print('april')
#     elif month_val==5:
#         print('may')
#     elif month_val==6:
#         print('june')
#     elif month_val==7:
#         print('july')
#     elif month_val==8:
#         print('august')
#     elif month_val==9:
#         print('september')
#     elif month_val==10:
#         print('october')
#     elif month_val==11:
#         print('november')
#     else:
#         print('december')
# else:
#     print('ERROR : enter value from 1 to 12')


#QUESTION 4
# marks=int(input('Enter the marks:'))
# if marks>80 and marks<=100:
#     print('YOUR GRADE IS A')
# elif marks>60 and marks<=80:
#     print('YOUR GRADE IS B')
# elif marks>50 and marks<=60:
#     print('YOUR GRADE IS C')
# elif marks>45 and marks<=50:
#     print('YOUR GRADE IS D')
# elif marks>25 and marks<=45:   
#     print('YOUR GRADE IS E')
# elif marks<=25:
#     print('YOUR GRADE IS F')
# else:
#     print('invalid marks')


#QUESTION 5
# num1=int(input('Enter a number:'))
# if num1%7==0:
#     print(F'{num1} is divisible by 7')
# else:
#     print(F'{num1} is not divisible by 7')


#QUESTION 6
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


#QUESTION 7
# a=int(input('Enter a number:'))
# if a%5==0:
#     print('HELLO')
# else:
#     print('BYE')


#QUESTION 8
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


#QUESTION 9
# v=input('Enter aplhabet:').lower()
# if v in 'aeiou':
#     print(F' {v} is vowel')
# else:
#     print(F' {v}is consonant')


#QUESTION 10
# marks=int(input('Enter the marks:'))
# if marks>89 and marks<=100:
#     print('YOUR GRADE IS A')
# elif marks>79 and marks<=89:
#     print('YOUR GRADE IS B')
# elif marks>69 and marks<=79:
#     print('YOUR GRADE IS C')
# elif marks<=69:
#     print('FAIL')


#QUESTION 11
# age=int(input('Enter age'))
# if age<13:
#     print(F'CHILD WITH AGE {age}')
# elif age>=13 and age<=19:
#     print(F'TEENAGER WITH AGE {age}')
# elif age>19:
#     print(F'ADULT WITH AGE {age}')
# else:
#     print('age is invalid')


#QUESTION 12
# al=input('Enter alphabet:')
# if (al.isupper()):
#     print(F'{al} is upper case')
# elif (al.islower()):
#     print(F'{al} is lower case')
# elif (al.isdigit()):
#     print(F'{al} is digit')
# else:
#     print('invalid')


#QUESTION 13
# a=input(' 1. RED\n 2. YELLOW \n 3. GREEN\nENTER THE COLOUR:').lower()
# if a=='red':
#     print('stop')
# elif a=='yellow':
#     print('ready to go')
# elif a=='green':
#     print('go')
# else:
#     print('invalid')


#QUESTION 14
# age=int(input('Enter age'))
# experience=int(input('enter experience'))
# if age>18 and experience>=2:
#     print('YOU ARE ELIGIBLE FOR THE JOB')
# else:
#     print('YOU ARE NOT ELIGIBLE')


#QUESTION 15
# tem=int(input('Enter temperature:'))
# if tem<15:
#     print('Its cold, wear warm clothes!')
# elif tem>=15 and tem<=30:
#     print('Enjoy the weather!')
# else:
#     print('its hot stay hydrated')


#QUESTION 16
# op=(input('1.PIZZA \n 2.BURGER \n 3.PASTA \n ENTER menu choice:')).lower()
# if op=='pizza':
#     print('PRICE:$10')
# elif op=='burger':
#     print('PRICE:$7')
# elif op=='pasta':
#     print('PRICE:$8')
# else:
#     print('item not available')


#QUESTION 17
# height=int(input('Enter your height in feet : '))
# if height>=6:
#     print('YOU ARE SELECTED')
# elif height<6:
#     print('SORRY YOU ARE NOT SELECTED')
# else:
#     print('error')


#QUESTION 18
# age=int(input('Enter age'))
# experience=int(input('enter experience'))
# if age>=18:
#     print('YOU ARE ALLOWED TO WATH THIS MOVIE')
# else:
#     print('YOU ARE NOT ALLOWED TO WATCH')


#QUESTION 19
# user='admin'
# pasw='password123'
# username=input('USERNAME: ')
# password=input('PASSWORD: ')
# if username==user and pasw==password:
#     print('ACCESS GRANTED')
# else:
#     print('INCORRECT PASSWORD OR USERNAME')


#QUESTION 20
# month_val=int(input('Enter value from 1 to 12 to display season:'))
# if month_val in [1,2,12]:
#     print('winter')
# elif month_val in [3,4,5]:
#     print('spring')
# elif month_val in [6,7,8]:
#     print('summer')
# elif month_val in [9,10,11]:
#     print('autumn')
# else:
#     print('invalid month')


#QUESTION 21
# salary=int(input('Enter your salary :'))
# cred=int(input('Enter your credit score: '))
# if salary>=50000 and cred>=700:
#     print('eligible')
# else:
#     print('not eligible')


#QUESTION 22
# n=int(input('ENTER A NUMBER'))
# if n>=1 and n<=100:
#     print(F'The number you entered is {n} and is between 1 -100')
# else:
#     print('the number is not between 1-100')