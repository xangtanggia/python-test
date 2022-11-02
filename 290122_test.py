print("ban bao nhieu tuoi:")
a=int(input())
if a<13:
    print("ban chi co the xem phim P")
elif a<16:
    print("ban co the xem phim C13 hoac phim P")
elif a<18:
    print("ban co the xem phim C13, C16 hoac phim P")
else:
    print("ban co the xem phim C18 :)")
a=input()
import os
os.system('cls')
print("Chao mung ban den voi the gioi cua hat nhan tien sinh")
print("Vui long chon muc tieu cua ten lua:")
print("1. Nhat Ban")
print("2. Han Quoc")
print("3. Hoa Ky")
print("4. Anh")
print("5. Phap")
print("Lua chon cua ban:")
b=int(input())
if b==1:
    print("ありがとう")
elif b==2:
    print("고맙습니다")
elif b==3 or b==4:
    print("Thank you")
elif b==5:
    print("Merci")
else:
    print("Vui long khoi dong lai chuong trinh")
print("Bam phim bat ky de ket thuc chuong trinh")
b=input()
os.system('cls')
print("Phan mem do Kim Jong-un che tao va thu nghiem")
print("chuc ban tot lanh")
