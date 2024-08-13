a=int(input("Enter a number:"))
sum=0
while(a>0):
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)
