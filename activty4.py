try:
    a=int(input("enter the numder : "))
    print("the number is =",a)
except ValueError as e:
    print(e)
    print("pls enter a number")