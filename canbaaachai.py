import math
print("giai phuong trinh bac hai nhap ax^2+bx+c")
a=float(input("nhap a"))
b=float(input("nhap b"))
c=float(input("nhap c"))

if(a!=0):
    delta=b*b-4*a*c
    if(delta<0):
        print("phuong trinh vo nghiem")
    elif (delta==0):
         x=-b/(2*a)
         print("co nghiem kep  x1=x2=", x)
    else:
         x1=(-b-math.sqrt(delta))/(2*a)
         x2=(-b+math.sqrt(delta))/(2*a)
         print("co nghiem kep x1={0} va x2={1}".format(x1,x2))
    


else:
	print("khong phai phuong trong bac 2 ")
