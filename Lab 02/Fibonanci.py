num=int(input("enter number:"))
num1=0
num2=1
Fibonanci=1
for i in range(0,num):
    print(Fibonanci)
    Fibonanci=num1+num2
    num1=num2
    num2=Fibonanci
    if Fibonanci>num:
         break