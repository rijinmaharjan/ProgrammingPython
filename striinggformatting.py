#formatmethod
#.format(a,b,c) goes by indexing so a is 0 b is 1 and so on
a=10
b=20
c=a+b
print('The addition of {} and {} is {}'.format(a,b,c))
print('The addition of {1} and {0} is {2}'.format(a,b,c)) #need to index every bracket if you index one
print('The addition of {} and {} is {e}'.format(a,b,e=50)) #if value is assigned in the format it self need to write the variable inside bracket

#fsring method
#cannot do indexing like in format method
#need to pass the variable it self as we did for e in format

print(F'the addition of {a} andf {b} is {c}')