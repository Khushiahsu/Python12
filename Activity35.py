#Write a program to demonstrate a right angle triangle pattern?

print('Half the pyramid patterns of stars (*)') 
a = int(input('Enter the amount of rows you want: ')) 

for i in range(a):
    for b in range(i+1):
        print('*' ,end="")

    print()
