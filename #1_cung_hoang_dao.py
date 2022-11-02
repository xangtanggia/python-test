#phan gioi thieu
print("              chuong trinh moi")
print("_______________________________________________")
print("                phan mem moi:)")
#phan nhap bien
print("nhap ten:")
a=str(input())
print("hello "+a)
print("nhap ngay sinh:")
b=int(input())
print("nhap thang sinh:")
c=int(input())
#phan kiem tra hop le cua bien b va c
if c==1 or c==3 or c==5 or c==7 or c==8 or c==10 or c==12:
	if b>=1 and b<=31:
		print("cung hoang dao cua ban la: ")
	else:
		print("ngay sinh khong hop le")
elif c==4 or c==6 or c==9 or c==11:
	if b>=1 and b<=30:
		print("cung hoang dao cua ban la: ")
	else:
		print("ngay sinh khong hop le")
elif c==2:
	if b>=1 and b<=29:
		print("cung hoang dao cua ban la: ")
	else:
		print("ngay sinh khong hop le")
else :
	print("thang sinh khong hop le")
#phan hien cung hoang dao
if c==1 and b>=1 and b<=19:
	print("ma ket")
elif c==1 and b>=20 and b<=31:
	print("bao binh")
elif c==2 and b>=1 and b<=18:
	print("bao binh")
elif c==2 and b>=19 and b<=29:
	print("song ngu")
elif c==3 and b>=1 and b<=20:
	print("song ngu")
elif c==3 and b>=21 and b<=31:
	print("bach duong")
elif c==4 and b>=1 and b<=20:
	print("bach duong")
elif c==4 and b>=21 and b<=30:
	print("kim nguu")
elif c==5 and b>=1 and b<=20:
	print("kim nguu")
elif c==5 and b>=21 and b<=31:
	print("song tu")
elif c==6 and b>=1 and b<=21:
	print("song tu")
elif c==6 and b>=22 and b<=30:
	print("cu giai")
elif c==7 and b>=1 and b<=22:
	print("cu giai")
elif c==7 and b>=23 and b<=31:
	print("su tu")
elif c==8 and b>=1 and b<=22:
	print("su tu")
elif c==8 and b>=23 and b<=31:
	print("xu nu")
elif c==9 and b>=1 and b<=22:
	print("xu nu")
elif c==9 and b>=23 and b<=30:
	print("thien binh")
elif c==10 and b>=1 and b<=23:
	print("thien binh")
elif c==10 and b>=24 and b<=31:
	print("bo cap")
elif c==11 and b>=1 and b<=22:
	print("bo cap")
elif c==11 and b>=23 and b<=30:
	print("nhan ma")
elif c==12 and b>=1 and b<=21:
	print("nhan ma")
elif c==12 and b>=22 and b<=31:
	print("ma ket")
#phan ket thuc chuong trinh
print("              het chuong trinh")
print("      do baooccho che tao va thu nghiem")
print("_______________________________________________")
input()
