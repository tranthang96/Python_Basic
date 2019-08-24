"""Sử dụng constructor Dict
Với dict, ta có 4 cách để khởi tạo một Dict bằng constructor:

Khởi tạo một Dict rỗng
Cú pháp:

dict()

Ví dụ:"""
dic = dict()
print(dic)

"""
Khởi tạo một dict từ một mapping object  
Cú pháp:

dict(mapping)

Trong đó:

Mapping object cũng gần giống so với dict object.

Một object là Mapping object khi có đủ hai phương thức keys và __getitem__.
Dict object cũng là một mapping object. Tuy nhiên, không phải mapping object
nào cũng là dict object vì dict object không chỉ có hai phương thức keys và __getitem__ 
và còn nhiều phương thức khác.
"""
class Map_Class:
        def keys(self):
               return [1, 2, 3]
        def __getitem__(self, key):
           return key * 2

map_obj = Map_Class()
dic = dict(map_obj)
print(dic)               #{1: 2, 2: 4, 3: 6}
# Khởi tạo bằng iterable 
#Iterator là các đối tượng cho phép ta lấy từng phần tử của nó, hành động này có thể được lặp đi lặp lại
"""iterable này đặc biệt hơn hơn các iterable mà bạn dùng để khởi tạo List hay Tuple,
 đó là các phần tử trong iterable phải có 2 value đó chính là cặp key-value.
Bạn có thể dùng List, Tuple hoặc bất cứ container nào 
(trừ mapping object) để chứa cặp key-value."""
iter_ = [('name', 'Thang'), ('member', 69)]
dic = dict(iter_)
print(dic)
print(type(dic))
#==== Khởi tạo bằng keyword arguments===
	#Cứ hiểu đơn giản là giống như việc bạn khởi tạo biến và giá trị rồi đưa cho dict đó giữ giùm.
	#Một lưu ý là những biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
name = 'SpaceX'
member = 696969
dic = dict(name='Thang', member=69)
print(dic)          #{'name': 'Kteam', 'member': 69}
""">>> name
'SpaceX'
>>> member
696969
Không ảnh hưởng tới giá trị , đơn giả là trùng tên"""

# ============Sử dụng phương thức fromkeys
#Công dụng: Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. 
#Các giá trị này đều sẽ nhận được một giá  trị với mặc định là None
iter_ = ('name', 'number')
dic_none = dict.fromkeys(iter_)
print(dic_none)
		#{'name': None, 'number': None}
dic = dict.fromkeys(iter_, 'non None value')
print(dic)
		#{'name': 'non None value', 'number': 'non None value'}