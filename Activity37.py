#Write a program to demonstrate the numbers in a diamond pattern?

a = int(input('Enter the amount of rows you want: '))

print('Diamond pattern:')
if a%2==0:
    b = int(a/2)
else:
    b = int(a/2)+1
space = b-1
for c in range(1,b+1):
    for d in range(1,space+1):
        print(end="")
    space = space-1
    e = 1
    for f in range(2*c-1):
     e = e+1
print()
space = 1
for c in range(1,b+1):
    for d in range(1,space+1):
        print(end="")
    space = space-1
    e = 1
    for d in range(1,2*(b-c)):
        print(end=str(e))
        e=e+1
    print()