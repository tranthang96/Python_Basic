#def : define
"""Ngoài từ khóa “def”, Python cũng hỗ trợ cho bạn một cách khác để có  thể khai báo một function object,
 đó chính là lambda. Nó chỉ khác từ  khóa “def” ở chỗ, thay vì def tạo một hàm với một cái tên xác định thì 
 lambda trả về một hàm. Thế nên người ta hay gọi lambda là hàm nặc danh (anonymous).
 Nó thường được sử dụng thường xuyên để có thể tạo ra một hàm chỉ với  một dòng lệnh."""
"""
Giới thiệu lambda
Ta có cú pháp sau:

lambda argument_1, argument_2, …, argument_n : expression

Như đã nói ở trên, lambda hoạt động như khi bạn dùng từ khóa “def” khai báo hàm. 
Tuy nhiên, vẫn có một vài ưu điểm nổi trội của lambda so với cách bình thường:

lambda là một expression, không phải là một câu lệnh. (Khái niệm expression đã được Kteam giới thiệu). 
Do đó lambda có thể có ở một vài chỗ mà “def” không thể có (bạn đọc sẽ biết ở phần sau)
lambda là một dòng expression duy nhất, không phải là một khối lệnh. 
Phần expression của lambda giống với phần khối lệnh của hàm với một lệnh return ở cuối hàm nhưng với 
lambda bạn chỉ cần ghi giá trị mà không cần ghi return. Bạn đọc sẽ hiểu rõ hơn ở phần sau khi biết lambda 
có thể sử dụng các câu lệnh điều kiện mà không cần phải sử dụng tới lệnh “if”. Nhờ được thiết kế như vậy, 
lambda được ưu tiên dùng cho việc tạo ra những hàm đơn giản, còn nếu phức tạp thì ta sẽ sử dụng đến từ khóa “def”.
Để có thể hiểu hơn, mời bạn đọc xem qua các ví dụ sau đây

Đây là khi bạn sử dụng từ khóa “def”
"""
ave = lambda a, b, c: (a + b+ c)/3
ave(1, 3, 2)

kteam_lst = [lambda x: x**2, lambda x: x**3, lambda x: x**4] # một list với các phần tử là các hàm nặc danh

print(kteam_lst[0])
print(kteam_lst[2](3))  #3^4

for i in kteam_lst:
	print(i(5))
# sử dụng lambla trong dicrt
dict_1 = {"Thang": lambda : "bac", 'hehe': lambda : "ho ho"}
print(dict_1["Thang"]())     # key là Thang trả về kq bac
# if trong lambda 
"""if a:

    b

else:

    c
ccách 1:
    b if a else c

cách 2:

   (a and b) or c"""

find_greater = lambda x, y: x if x > y else y
print(find_greater(4,5))
