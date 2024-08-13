num=int(input("ENTER A NUMBER:"))
i=1
count=0
while (i<=num):
    if num%i==0:
        count=count+1
    i+=1

if count==2:
    print(num,"IS a prime number")
else:
    print(num,"is not a prime number")
    
