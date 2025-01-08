#QUESTION 8
# import random
# a=random.randint(1,30)
# b=random.randint(1,30)
# c=a*b
# print(f'The multiplication of {a} and {b}')
# while True:
#     e=int(input('Guess the number:')) 
#     if e==c:
#         print('correct')
#     else:
#         print('incorrect')
#     f=input('Do you want to continue?')    
#     if f=='exit':
#         break
#     a=random.randint(1,30)
#     b=random.randint(1,30)
#     c=a*b

#     print(f'The multiplication of {a} and {b} is:')
    

#QUESTION 1
# while True:
#     age=int(input("Enter your age"))
#     if age<18:
#         print('You are a minor')
#     elif age>=18 and age<=60:
#         print('You are an Adult')
#     else:
#         print('You are a senior citizen')
#     stop=input('stop or continue')
#     if stop=='stop':
#         break
# print('exitted')    


#QUESTION 2
# while True:
#     a=input('Enter a vehicle:')
#     if a=='bus':
#         print('finally the wait is over')
#         break
#     else:
#         print('waiting')

#QUESTOIN 3
# while True:
#     a=input('Enter a fruit:')
#     if a=='apple':
#         print('YOU GOT IT')
#         break
#     else:
#         print('Try again')


#QUESTION 4
# while True:
#     a=input('Guess the password:')
#     if a=='open sesame':
#         print('Acccess granted')
#         break
#     else:
#         print('Try again')


# #QUESION 5
# while True:
#     a=input('Enter a day of the week:')
#     if a=='sunday':
#         print('Enjoy your weekend.')
#         break
#     else:
#         print('not the weekend yet')

#QUESTION 6
# import random
# a=random.randint(1,10)
# while True:
#     b=int(input('guess the number:'))
#     if b>a:
#         print('guess lower')
#     elif b<a:
#         print('guess higher')
#     else:
#         print('correct')
#         break

#QUESTION 7
# while True:
#     user=input('Enter your username:')
#     pasw=input('Enter your password:')
#     if user=='admin' and pasw=='1234':
#         print('Login Sucessful')
#         break
#     else:
#         print('incorrect user name or password')
# user='hello'
# passw='world'
# i=3
# while i>0:
#     i-=1
#     usem=input('enter username:')
#     pas=input('Enter password:')
#     if pas==passw and usem==user:
#         print('Logged in')
#         break
#     else:
#         print(i,' attemts left')
# print('Blocked')

#QUESTION 9
# import random
# while True:
#     a = random.randint(1, 30)
#     if a > 1:
#         for i in range(2, a):
#             if a % i == 0:
#                 print(f'{a} not prime number')
#                 break
#         else:
#             print(f'{a} prime number')
#     else:
#         print(f'{a} not prime number')
    
#     b = input('Exit or continue: ')
#     if b=='exit':
#         break

#QUESTION 10
# secret='iamhere'
# while True:
#     a=input('Enter secret code:')
#     if a==secret:
#         print('congrats,this is correct.')
#         break
#     else:
#         print('it is wrong.')
#         b=input('try again or quit:')
#         if b=='quit':
#             break

#Question 11
# i=1
# while True:
#     a=input('Enter a phrase:')
    
#     if a=='good luck':
#         print(f'{a} entered. Times:{i}')
#         i=i+1
#     if i==4:
#         print(f'You entered the same word 3 times')
#         break
    