print("Лабораторная работа 1")
import math
print("Введите коэффициенты для уравнения")
print("a*x^4+b*x^2+c=0: ")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if a==0:
    if b==0:
        if c==0:
            print("x-Любое число")
        else:
            print ("Корней нет")
    elif c == 0:
        print("x=0")
    else:
        if (c * (-1) / b) > 0:
            x1 = math.sqrt(c*(-1)/b)
            x2 = math.sqrt(c * (-1) / b)*(-1)
            print("x1=%.2f \nx2=%.2f"%(x1,x2))
        elif (c * (-1) / b) < 0:
            print ("Корней нет")

elif b==0:
    if c==0:
        print("x=0")
    else:
        if (c * (-1) / a) > 0:
            x1 = math.sqrt(math.sqrt(c * (-1) / a))
            x2 = math.sqrt(math.sqrt(c * (-1) / a)) * (-1)
            print("x1=%.2f \nx2=%.2f" % (x1, x2))
        elif (c * (-1) / a) < 0:
            print ("Корней нет")
elif c==0:
    x1 = 0
    if (b* (-1) / a) > 0:
        x2 = math.sqrt(b * (-1) / a)
        x3 = math.sqrt(b * (-1) / a) * (-1)
        print("x1=%.2f \nx2=%.2f \nx3=%.2f" % (x1, x2, x3))
    elif (b * (-1) / a) <0:
        print ("Корней нет")
else:
    D=b**2-4*a*c
    if D>0:
        x12=(b*(-1)+math.sqrt(D))/(2*a)
        x22=(b*(-1)-math.sqrt(D))/(2*a)
        if x12<0:
            x1=math.sqrt(x22)
            x2 = math.sqrt(x22)*(-1)
            print("x1=%.2f \nx2=%.2f" % (x1, x2))
        elif x22 < 0:
            x1 = math.sqrt(x12)
            x2 = math.sqrt(x12) * (-1)
            print("x1=%.2f \nx2=%.2f" % (x1, x2))
        else:
            x1 = math.sqrt(x22)
            x2 = math.sqrt(x22) * (-1)
            x3 = math.sqrt(x12)
            x4 = math.sqrt(x12) * (-1)
            print("x1=%.2f \nx2=%.2f\n x3=%.2f \nx4=%.2f" % (x1, x2, x3, x4))
    elif D==0:
        x12=b*(-1)/(2*a)
        if x12>0:
            x1 = math.sqrt(x12)
            x2 = math.sqrt(x12) * (-1)
            print("x1=%.2f \nx2=%.2f" % (x1, x2))
        elif x12<0:
            print ("Корней нет")
        else:
            print("x=0")
    else:
        print ("Корней нет")

