import math
number=int(input("enter the number"))
root=math.sqrt(number)
if int(root+0.5)**2==number:
	print("given number is a perfect square ")
else:
	print(number,"is not a perfect square")