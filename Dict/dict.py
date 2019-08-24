"""Dict(Dictionary) cũng là một container như LIST, TUPLE. Có điều khác biệt là những 
container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng 
các key để phân biệt.

Chắc bạn cũng dùng từ điển tiếng Anh để tra từ vựng rồi nhỉ? 
Có rất nhiều từ vựng trong đó nhưng mà không từ vựng nào giống nhau. Có chăng chúng chỉ giống nhau về nghĩa? Và đó cũng như Dict(Dictionary) hoạt động trong Python

Một Dict gồm các yếu tố sau:

Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
Các phần tử của Dict phải là một cặp key-value
Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
Các key buộc phải là một hash object"""
#========== Cú pháp =====
# {<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}
dic = {'name': 'Thang', 'member': 96 }
print(dic)
print(type(dic))
#khởi tạp dict rỗng
empty_dic={}
print(empty_dic)
print(type(empty_dic))
# sử dụng set comprehension
dic = {key: value for key, value in [('name', 'Thang'), ('member', 69)]}
print(dic)
#=== sử dụng contructor dict==
