num=int(input("Enter a number:"))
first,second=0,1
print(f"{first}\n{second}")
for i in range(2,num):
    third=first+second
    print(third)
    first=second
    second=third
    
