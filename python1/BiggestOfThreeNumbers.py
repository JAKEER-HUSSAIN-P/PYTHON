a,b,c=map(int,input("Enter three numbers using ',':").split(','))
if a>b and a>c:
    print(a,"is the biggest number among given numbers")
elif b>a and b>c:
    print(b,"is the biggest number among given numbers")
else:
    print(c,"is the biggest number among given numbers")
