# Phương thức với dict
#====== Copy=====
dic = {'name': 'Thang', 'member': 96 }
print(dic)
dic1 = dic.copy() # tạo ra 1 vùng nhớ mới
print(dic1)
#====== clear ====
dic1.clear()
print(dic1)
#====== get ====
 #get theo key, trả về giá trị
value = dic.get('name') 
print(value) 
	#ko có giá trị trả về None 
value = dic.get('dsafdaf') 
print(value) 
	# 
value = dic.get('ghfy' ,'không có đâu' ) # <Dict>.get(key [,default])nếu ko có giá trị thì trả về giá trị default
print(value) 
#============items()===========
#Công dụng: Trả về một giá trị thuộc lớp dict_items. Các giá trị của dict_items 
#sẽ là một tuple với giá trị thứ nhất là key, giá trị thứ hai là value.
value = dic.items() 
value1 = list(dic.items())
print(value) 
print(value1[0])
#==== phương thức keys:  lấy ra danh sách key====
value = dic.keys() 
print(value) 
#==== phương thức values:  lấy ra danh sách value====
value = dic.values() 
print(value) 
#===== phương thức pop : bỏ đi phần tử có key và trả về giá trị của key đó

dic = {'name': 'Thang', 'member': 96 }
print(dic)
value = dic.pop("name")
print(value)
print(dic)
 #nếu ko có giá trị ko có. báo lỗi, thêm default thì trả về giá trị default
value = dic.pop("aaaaa" , "lỗi ko có")
print(value)
print(dic)
#=====Phương thức popitem
"""Cú pháp:
<Dict>.popitem()
Công dụng: Trả về một 2-tuple với key và value tương ứng bất kì 
(vấn đề này liên quan đến giá trị của hash của key. 
Do đó bạn cũng hiểu vì sao key buộc phải là một hash object) trong Dict. 
Và cặp key-value sẽ bị loại bỏ ra khỏi Dict.

Nếu Dict là một empty Dict. Sẽ có lỗi KeyError"""
dic = {'name': 'Thang', 'member': 96 }
print(dic)
value = dic.popitem()
print(value)

#====Setdefault===
"""
<Dict>.setdefault(key [,default])

Công dụng: Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default. Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.

Default mặc định là None"""
dic = {'name': 'Thang', 'member': 96 }
print(dic)
value = dic.setdefault("sffasff")
print(value)
print(dic)  # {'name': 'Thang', 'member': 96, 'sffasff': None}
value = dic.setdefault("aaaaaa","gia tri moi") 
print(dic) #{'name': 'Thang', 'member': 96, 'sffasff': None, 'aaaaaa': 'gia tri moi'}

#==== Phương thức update=====
# cú pháp: <D>.update([E,]**F)
	#Phương thức giúp bạn cập nhật nội dung cho Dict.
	#F là một Dict được tạo thành bởi packing arguments
#update theo kiểu sử dụng packing arguments.
d = {'a': 1}
print(d)
d.update(b=2,c=3)
print(d) # {'a': 1, 'b': 2, 'c': 3}
# update theo truyền E với E là một đối  tượng có phương thức keys
d = {'a': 1}
E = {'b': 2, 'c': 3}
d.update(E)
print(d) #{'a': 1, 'b': 2, 'c': 3}
# truyền vào một E với  E có các giá chứa hai giá trị
d = {'a': 1}
E = [('b', 2), ('c', 3)]
d.update(E)         #{'a': 1, 'b': 2, 'c': 3}
E_f = (['d', 69], ['e', 96])
d.update(E_f)
print(d)            #{'a': 1, 'b': 2, 'c': 3, 'd': 69, 'e': 96}
# update giá trị cùng key
E_g = (["d",234],['e',"Thang"])
d.update(E_g)
print(d)           #{'a': 1, 'b': 2, 'c': 3, 'd': 234, 'e': 'Thang'}
