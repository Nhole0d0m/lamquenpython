import math
xa=float(input("nhap xa "))
ya=float(input("nhap ya "))
xb=float(input("nhap xb "))
yb=float(input("nhap yb "))
xc=float(input("nhap xc "))
yc=float(input("nhap yc "))

ab=math.sqrt((xb-xa)**2 +(yb-ya)**2)
bc=math.sqrt((xc-xb)**2 +(yc-yb)**2)
ac=math.sqrt((xc-xa)**2 +(yc-ya)**2)

if((ab+ac>bc) and (ab+bc>ac ) and (bc+ac>ab )) :
    print("tao thanh hinh tam giac")
    cv=ab+ac+bc
    print("chu vi =", cv)
    p=cv/2
    p=math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("dien tich =",p)
else:
    print("khong tao thanh hinh tam giac ")