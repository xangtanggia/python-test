from base64 import encode
import array
import hashlib
from multiprocessing.dummy import Array
from re import A
from this import d
from typing_extensions import Self
print("__________________________________________so do online______________________________________________")
class nha:
    def __init__(self,so_tang,so_nha, dien_tich, nguoi_so_huu="",before_hash=""):
        self.before_hash=before_hash
        self.so_tang=so_tang
        self.so_nha=so_nha
        self.dien_tich=dien_tich
        self.nguoi_so_huu=nguoi_so_huu
        self.nonce=0
        self.so_hash=self.taoHash()    
        
    def taoHash(self):
        data=str(self.so_nha)+str(self.so_tang)+str(self.dien_tich)+self.nguoi_so_huu+self.before_hash+str(self.nonce)
        encoded=data.encode()
        result =hashlib.sha256(encoded).hexdigest()
        return result
    def xayNha(self,DoKhoXayNha):
        a=[]
        a.append("0")
        while (self.so_hash[0:DoKhoXayNha]!=a):
            self.nonce+=self.nonce
            self.so_hash=self.taoHash()
        print("Ma xay nha",self.so_hash)
class khu_pho:
    def __init__(self):
        self.dokhoxaynha=1
        self.nha=[nha(0,0,0,"Block khoi tao","0")]
        self.so_nha=self.soNha()
    
    def soNha(self):
        return len(self.nha)
    def addNha(self,nhaMoi):
        nhaMoi.before_hash=self.NhaCuoiDay().so_hash
        nhaMoi.xayNha(self.dokhoxaynha)
        self.nha.append(nhaMoi)
    def NhaCuoiDay(self):
        return self.nha[len(self.nha)-1]
    def CheckNha(self):
        for i in range(1,len(self.nha)):
            nhaHienTai=self.nha[i]
            nhaTruoc=self.nha[i-1]
            if nhaHienTai.so_hash !=nhaHienTai.taoHash():
                return False
            if nhaHienTai.before_hash != nhaTruoc.so_hash:
                return False
        return True
a=khu_pho()

print("xayNha1")
a.addNha(nha(15,196,40,"Nguyen Viet Duc"))
print("xayNha2")
a.addNha(nha(30,198,40,"Ha Anh Tuan"))
a.addNha(nha(110,322,900,"Tan Hoang Minh and Hong Dang"))


# def taoSoDoMoi(so_tang,so_nha,dien_tich,nguoi_so_huu):
#     a.addNha(nha(so_tang,so_nha,dien_tich,nguoi_so_huu))
# taoSoDoMoi(15,909,500,"Lương Thùy Linh")
# for i in range(len(a.nha)):
#     print(a.nha[i].so_hash)
#     print(a.nha[i].nguoi_so_huu)
#     print(a.nha[i].so_nha)
#     print(a.nha[i].so_tang)
#     print("_______________________________________________")
# print(a.NhaCuoiDay().so_hash)
# print(a.CheckNha())