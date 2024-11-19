#Write a program to demonstrate a Floyd triangle pattern?

a = int(input('Enter how many rows you want: '))
b = 1
print("Floyd's triangle")
for c in range(1,a+1):
    for d in range(1,c+1):
        print(b,end="")
        b = b+1
    print()