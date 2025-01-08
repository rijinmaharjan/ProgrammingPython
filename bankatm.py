print('Welcome to mybank ATM')
print('Please choose a option')
print('1. check balance')
print('2. withdraw cash')
print('3. deposit cash')
print('4. exit')
bal=10000

choice=int(input('CHOOSE A OPTION: '))
if choice == 1:
    print(F'Your current balance is {bal}')
elif choice == 2:
    amt=int(input('Enter the amount you want to withdraw : '))
    if amt>bal:
        print('insufficient balance')
    else:
        bal=bal-amt
        print(F'withdraw successful and your new balance is {bal} ')
elif choice==3:
    amt=int(input('Enter the amount you want to deposit :'))
    if amt<=0:
        print('invalid amount')
    else:
        bal=bal+amt
        print(F'withdraw successful and your new balance is {bal} ')
elif choice==4:
    print('EXITTING. BYE')
else:
    print('invalid choice please retry')
    