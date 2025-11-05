print("SCIENTIC CALCULATOR")
operation=(int(input("CHOOSE THE OPERATION{1.Arithmetic 2.trigo fun 3.other operation}:")))

if(operation==1):
 x=int(input("Enter the no of digit: "))
 a=[]
 for i in range(1,x+1):
    num=int(input("Enter the number:"))
    a.append(num)
 def add(b):
    total=0
    for num in b:
        total+=num
    return total       
 def sub(c):
    total=0
    for num in c:
        total-=num
    return total
 def multi(d):
    total=1
    for num in d:
        total*=num
    return total  
 def div(e):
    total=1
    for num in e:
        total/=num
    return total    
 y=int(input("choose the Arithmetic operation{1.addition 2.subtraction 3.multiplication 4.division}:"))
 if(y==1):
    print("The addition is", add(a))
 if(y==2):
    print("The subtraction is", sub(a))
 if(y==3):
    print("The multiplication is", multi(a))
 if(y==4):
    print("The division is",div(a))  


if(operation==2):
 import math
 trigo=int(input("choose the trigo function{1.sin 2.cos 3.tan 4.cot 5.sec 6.cosec}:"))
 degree=float(input("Enter the degree:"))
 rad=math.radians(degree)
 sin=math.sin(rad)
 cos=math.cos(rad)
 tan=math.tan(rad)
 cot=1/tan
 sec=1/cos
 cosec=1/sin

 if(trigo==1):
    print(sin)

 if(trigo==2):
    print(cos)

 if(trigo==3):
   print(tan)

 if(trigo==4) :
    print(cot)  

 if(trigo==5):
    print(sec)
 if(trigo==6):
    print(cosec)    

if(operation==3): 
 x=int(input("Enter the value:"))
 y=int(input("Enter the base power:"))    

 import math
 def log(a,b):
    logg=math.log(a,b)
    return logg
 def exp(expo):
   exponential=math.exp(expo)
   return exponential
 
 def square(sqre):
    square=sqre*sqre
    return square

 def sqrt(c):
    square_root=math.sqrt(c)
    return c

 def fact(num):
    factorial=1
    for i in range(1,num+1):
     factorial*=i
    return factorial

 choice=int(input("choose the option{1.log 2.exponential 3.square 4.sqare_root 5.factorial}:"))
 if(choice==1):
    print("the log is",log(x,y))

 if(choice==2):
     print("The exponential is",exp(x))
  
 if(choice==3):
    print("The square is",square(x))


 if(choice==4):
    print("The sqare root is",sqrt(x))
 
 if(choice==5):
        print("The factorial is",fact(x))
