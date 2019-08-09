#thay thế %s %d .... bằng giá trị nằm trong nháy đơn
a = "My name is %s"%('Thắng')
print(a)
tuoi = "i'm %d %s year old" %(20," <3 ")
print(tuoi)
#gán chuỗi
s="%s %s"
result = s %(1,3)
print(result)
"""format trong python"""
strA = 'a:{}, b:{}, c:{}' .format(1,2,3)
print(strA)
#tương tự str A như trên. 
strB = "a:%d ,b:%d, c:%d" %(1,2,3)
print(strB)
#sắp xếp thứ tự hiện thị
strC = 'a:{2}, b:{0}, c:{1}' .format(1,2,3)
print(strC)