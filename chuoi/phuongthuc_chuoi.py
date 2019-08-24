#phương thức chuỗi trong python
a = '12'
print (int(a))
print (type(a))
#các biến có type là str ta có thể áp dụng các phương thức chuỗi

#viết hoa chữ đầu tiên
strA = "tran viet thang"
strB = strA.capitalize() # Tran viet thang => viết hoa chữ cái đầu tiên
print(strB)
#viết hoa full
strC = strA.upper()
print(strC) # TRAN VIET THANG 
# Viết Thường lower
print(strC.lower())
# Viết Hoa thành viết thường, viết thường thành viết Hoa
print(strB.swapcase())
# Viết Hoa chữ đầu tiên trong từ
print(strA.title())
# Phương thức in ra một chuỗi mã hoá
strtest = "Trần Việt Thắng"
strEncode = strtest.encode(encoding='utf-8',errors='strict')
#strEncode1 = strtest.encode()
print(strEncode)
#print(strEncode1)
#=======cộng chuỗi======
strjoin  = strA.join(['1','2','3']) # 1+strA+2+strA+3
print(strjoin)
#======== thay thế =====
thaythe = strA.replace('t','saf',2) # .replace([kí tự cần thay thế],[kí tự thay thế],[số lần thay thế, ko ghi mặc định thay thế toàn bộ])
print(thaythe)
#========xoá các kí tự 2 đầu====
a="b caffff l"
b=a.strip('b') #xoá kí tự b. ko có gì mặc định khoảng trắng
	#lstrip bên trái
	#rstrip bên phải....
print(b)
