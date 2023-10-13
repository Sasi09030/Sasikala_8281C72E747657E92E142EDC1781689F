def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#take input from the user
num=int(input("enter a number:"))
#check is the number is negative
if num<0:
  print("sorry, factorial does not exist for negative numbers")
elif num==0:
  print("the factorial of 0 is 1")
else:
  print("the factorial of",num,"is",factorial(num))