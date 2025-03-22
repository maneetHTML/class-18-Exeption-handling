try:
    a=int(input("enter the numder : "))
    if a%2==0:
      print("the number",a,"is even")
    else:
      print("the number",a,"is odd")
except ValueError as e:
    print(e)
    print("pls enter a number")