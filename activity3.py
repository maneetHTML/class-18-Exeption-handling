try:
    a=int(input("enter the dividend : "))
    b=int(input("enter the dividend : "))
    c=a/b
    if b==0:
       raise ZeroDivisionError
    else:
        print("answer : ",c)
except ZeroDivisionError:
    print("the divisor should not be Zer0")

finally:
    print("thank you")