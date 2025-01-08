a= 'python'
b= a.upper()

c=b.lower()

d=a.capitalize()

f='python program'
g=f.title()
h=f.swapcase()


print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
#i= a.zfill()
#center()
i=a.center(10,'*')
j=a.ljust(10,'*')
k=a.rjust(10,'*')
print(i)
print(j)
print(k)
#count
m='aaaaabcd'
l=m.count('a')
print(l)
#find and index
n=f.find('p') #or n=f.rfind('p')
print(n)
#for negative index
o=n-len(f)
print(o)
#b=a.isupper() if the all upper then true or false
#b=a.islower() if the lower then true or false
#b=a.istitle() if the first letter is captial then true or false
#b=a.isalpha() if all letter is alphanbet then prints true 
#b=a.isdigit() if all letter is number then prints true
#b=a.isalnum() if contains alphabet or number then prints treu and if has space or any other chracter then false
#b=a.isprintable() if contains only printable chracter then true
#b=a.isspace() if contains \n or break then true
#b=a.startswith('py') true #b=a.startswith('cyt') false
#b=a.endswith('thon') true #b=a.startswith('asfsdf') false





