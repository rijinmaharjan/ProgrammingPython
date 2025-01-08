#QUESTION 1
# for i in range(10):
#     print('softwarica')


#QUESTION 2
# S=[1,2,3,4,5]
# sum=0
# for i in S:
#     sum=sum+i
# print(sum)


#QUESTION 3
# a='softwarica'
# for i in range(len(a)):
#     print(a[i])

#QUESTION 4
# l=[1,'a','c',2,3,4]
# for i in l:
#     if isinstance(i,int):
#         print(i)

#QUESTION 5
# l=[4,5,3,2]
# m=1
# for i in l:
#     m=m*i
# print(m)


#QUESTOIN 6
# a=int(input('Enter a number:'))
# for i in range(1,11):
#     print(f'{a}*{i}','=',a*i)

#QUESTION 7
# a=[1,2,3,4]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

#QUESTION 8
# a=[1,2,3,4]
# new=[]
# for j in a:
#     j=j+1
#     new.append(j)
# print(new)  

#QUESTION 9
# lst=[1,2,3,4]
# for i in lst:
#     if i==1 or i==4:
#         print(i)

#QUESTION 10
# lst=[1,2,3,4]
# for i in lst:
#     if i==1 or i==4 or i==2:
#         print(i)

#QUESTOIN11
# a=[1,2,3,4]
# new=[]
# j=2
# for i in a:
#     if i==2:
#         new.append('a')
#     else:
#         if i==1:
#             new.append(i)
#         else:
            
#             new.append(j)
#             j+=2    
# print(new)  


#QUESTION 12
# a=[1,2,3,4,5]
# e=[]
# o=[]
# for i in a:
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)   
# print('the even numbers are:')
# for even in range(len(e)):
#     print(e[even])
# print('the odd numbers are:')
# for odd in range(len(o)):
#     print(o[odd])    


#QUESTION 13
# a=[1,2,3,'d',4,5,'a']
# n=[]
# s=[]
# for i in a:
#     if isinstance(i,int):
#         n.append(i)
#     else:
#         s.append(i)
# print(f'Interger data types: {n}')       
# print(f'Str data types:{s}') 

#QUESTION 14 (same as 13)
# a=[1,2,3,4,'a','b']
# n=[]
# s=[]
# for i in a:
#     if isinstance(i,int):
#         n.append(i)
#     else:
#         s.append(i)
# print(f'Interger data types: {n}')       
# print(f'Str data types:{s}') 

#QUESTOIN 15
# a=input('Enter:')
# dig=0
# let=0
# spa=0
# for i in a:
#     if i.isalpha():
#         let+=1
#     elif i.isdigit():
#         dig+=1
#     elif i==' ':
#         spa+=1
# print(f'digits:{dig}')  
# print(f'Letters:{let}')
# print(f'Spaces:{spa}')      


#QUESTION 16
# username='something'
# pasw='nothing'
# for i in range(2,-1,-1):
#     user=input('enter username:')
#     pas=input('Enter password:')
#     if user!=username or pas!=pasw:
#         if i==0:
#             print('BLOCKED')
#             continue
#         print(f'{i} attemps left')
        
#     else:
#         print('logged in')
#         break

#QUESTION 17
# a=int(input('Enter a number:'))
# if a%2==0:
#     print('EVEN')
# else:
#     print('ODD')

#QUESTION 18
# a=int(input('Enter a number for its factorial'))
# fact=1
# for i in range(a,0,-1):
#     fact=fact*i
# print(fact) 

#QUESTION 19
# a=[1,2,3,4,5,6,7,8]
# for m in a:
#     for i in range(1,11):
#         print(f'{m}*{i}','=',m*i)
#     print('\n')

#QUESTION 20
# lst=[1,2,3,4]
# for i in lst:
#     if i==1 or i==2:
#         print(i)

#QUESTION 21 and QUESTION 22
# s=int(input('Enter starting point:'))
# e=int(input('Enter ending point:'))
# even=[]
# odd=[]
# sum1=0
# sum2=0
# for i in range(s,e):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# for sumeven in even:
#     sum1=sum1+sumeven
# print(f'Sum of even numbers is :{sum1}')
# for sumodd in odd:
#     sum2=sum2+sumodd
# print(f'Sum of even numbers is :{sum2}')

#QUESTION 22(in 21 combined)

#QUESTION 23
# a=input('Enter:')
# spa=0
# for i in a:
#     if i==' ':
#         spa+=1
# print(f'Spaces:{spa}') 

#QUESTION 24
# a=[1,2,3,4]
# new=[]
# for j in a:
#     j=j*j*j
#     new.append(j)
# print(new)  

#QUESTION 25
# a='programming'
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

#questoin 26
# for i in range(50):
#     print(i)
#     if i==7:
#         break

#QUESTION 27
# a=input('enter:')
# for i in range(len(a)):
#     print(a[i])

#QUESTION 28
# name=[]
# howmanynames=int(input('how many names do ypu want to enter:'))
# for i in range(howmanynames):
#     namein=input('Enter name:')
#     name.append(namein)
# for j in name:
#     print('Hello!',j)

#QUESTION 29
# name=[]
# howmanynames=int(input('how many names do ypu want to enter:'))
# for i in range(howmanynames):
#     namein=input('Enter name:')
#     name.append(namein)
# for j in name:
#     print(f'Dr.{j}')

#QUESTION 30
# number=[]
# new=[]
# howmanynumbers=int(input('how many numbers do ypu want to enter:'))
# for i in range(howmanynumbers):
#     numberenter=int(input('Enter number:'))
#     number.append(numberenter)
# print(number)    
# for j in number:
#     j=j*j
#     new.append(j)
# print(new)    

#QUESTION 31
# lst1=[111,32,-9,-45,-17,9,85,-10]
# positive=[]
# for i in lst1:
#     if i>=0:
#         positive.append(i)
# print('new list with only positive values',positive)        

#QUESTION 32
# ls=[0,1,2,3,4,5,6]
# for i in ls:
#     if i==3 or i==6:
#         continue
#     else:
#         print(i)

#QUESTION 33
# lst=[1,2,'hello','ok']
# new=[]
# for i in lst:
#     new.append(type(i))
# print(lst)
# print(new)

#QUESTION 34
# for i in range(4):
#     print(i)
# else:
#     print('done')

#QUESTION 35
# for i in range(105,6,-7):
#     print(i)

#QUESTION 36
# bad_chars = [';', ':', '!', '*',' ']
# string = "py;th* o:n ! ;py * t*h:o !n"
# for i in bad_chars:
#     string=string.replace(i,'')
# print(string)    

#QUESTION 37
# e=0
# o=0
# for i in range(20):
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print(f'Number of odd:{o} and number of even:{e}')

#QUESTION 38
# sum=0
# for i in range(3,100):
#     if i%3==0 or i%5==0:
#         sum+=i
# print(f'sum of all multiples of 3 or 5 in range3 to 99 is {sum}')

#QUESTION 39
# sumeven=0
# sumodd=0
# for i in range(1,101):
#     if i%2==0:
#         sumeven+=i
#     else:
#         sumodd+=i
# print(f'sum of even number in range 1 to 100 is {sumeven} \n sum of odd numbers in range 1 to 100 is {sumodd}')

#QUESTION 40
# a=input('enter a number')
# areverse=''
# for i in (len(a)-1,-1,-1):
#     areverse=areverse+a[i]
# if areverse==a:
#     print('it is palindrome')
# else:
#     print('it is not palindrome')

#QUESTION 41
# num = input("Enter a number: ")
# numdigits = len(num)
# sumofpowers = 0

# for i in range(len(num)):
#     sumofpowers += int(num[i]) ** numdigits

# if sumofpowers == int(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

#QUESTION 42
# a=input('enter:')
# lst=['a','e','i','o','u']
# for i in lst:
#     a=a.replace(i,'')
# print(a)

#QUESTION 43
# num = int(input("Enter a number: "))
# sum= 0
# for i in range(1, num):
#     if num%i== 0:
#         sum+=i
# if sum==num: 
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")


#QUESTION 44
# lst1=[1,2,3,4,5]
# lst2=[3,4,5,6,7]
# new=[]
# for i in lst1:
#     for j in lst2:
#         if i==j:
#             new.append(j)
# print(f'common:{new}')

#QUESTION 45
# num = int(input("Enter a number: "))

# if num < 2:
#     print(f"{num} is not a prime number.")
# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
