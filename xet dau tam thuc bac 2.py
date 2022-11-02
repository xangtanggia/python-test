import math
a=int(input())
b=int(input())
c=int(input())
Delta=b*b-4*a*c
x1=int()
x2=int()
g=int()
if Delta < 0 :
	if a > 0:
		print("f(x) > 0 voi moi x")
	if a < 0:
		print("f(x) < 0 voi moi x ")
if Delta == 0:
	x1=-b/(2*a)
	if a > 0:
		print("f(x) > 0 voi moi x, tru x =",x1)
	if a < 0:
		print("f(x) < 0 voi moi x, tru x =",x1)
if Delta > 0:
	x1=(-b+math.sqrt(Delta))/(2*a)
	x2=(-b-math.sqrt(Delta))/(2*a)
	if x2 > x1:
		g=x2
		x2=x1
		x1=g
	if a > 0:
		print("f(x) > 0 trong khoang (-vo cuc;",x2,")U(",x1,";+vo cuc), < 0 trong khoang (",x2,";",x1,")")
	if a < 0:
		print("f(x) < 0 trong khoang (-vo cuc;",x2,")U(",x1,";+vo cuc), > 0 trong khoang (",x2,";",x1,")")
d=input()