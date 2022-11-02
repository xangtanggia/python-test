print("nhap canh a =")
a=int(input())
print("nhap canh b =")
b=int(input())
print("nhap canh c =")
c=int(input())
if a+b>c and a+c>b and b+c>a:
	kt=bool(True)
else:
	kt=bool(False)
if kt==True:
	print("Day la do dai 3 canh cua mot tam giac")
	if a==b or a==c or b==c:
		print("Day la tam giac can")
	if a==b and a==c and b==c:
		print("Day la tam giac deu")
	if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
		print("Day la tam giac vuong")
else:
	print("Day khong phai la do dai 3 canh cua mot tam giac")
input()