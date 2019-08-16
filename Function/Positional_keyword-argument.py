#Function trong Python - Positional và keyword argument
def LeanPython(a,b):
	pass # lệnh giữ chỗ.
LeanPython(13,"Tran Thang") # 3, "Tran Thang" là một positional 
LeanPython(a=13, b = "Tran Thang") # a,b là một keyword argument

#với keyword argument không cần truyền đúng thứ tự,
LeanPython(b = "Tran Thang",a=13)

#Bắt buộc (force) Positional argument và keyword argument
#Trong Python, có một số hàm bắt chúng ta buộc phải pass argument một cách rõ 
	#  ràng rành mạch như hàm sorted.
sorted([3, 4, 1], reverse=True)   
'''
#+++Python cho phép chúng ta tạo ra các parameter chỉ nhận giá  trị bằng việc pass argument 
theo kiểu keyword argument.

Cú pháp
def function (*, key_arg1, key_arg2):

# function-block

Khi tạo một hàm mà có một parameter *. Thì Python sẽ hiểu đó không phải là parameter mà chính 
là syntax để rồi nó biến các parameter sau * thành các keyword only argument 
(chỉ nhận giá trị theo kiểu keyword argument)

Ví dụ là dễ hiểu nhất!'''
def kteam(pos_or_key_arg, *, key_arg1, key_arg2):  #sau * thành các keyword only argument 
	print(pos_or_key_arg)							# có thể thay thế * thành *identifier, tuy nhiên phổ biến là *
	print(key_arg1)
	print(key_arg2)          
"""
Bạn còn nhớ hàm input chứ:
input(prompt=None, /)

Dấu / chính là một syntax để force parameter prompt trở thành positional only argument. 
Có nghĩa là bạn chỉ có thể pass argument cho parameter prompt theo kiểu positional. 
Chính xác thì dấu / sẽ biến các parameter đứng trước nó thành positional only argument

Tuy nhiên chúng ta sẽ không đi sâu vào positional argument vì ở phiên bản Python 3.6.X trở đi 
không hỗ trợ positional only argument.

Lưu ý: 3.6.X trở đi không hỗ trợ không có nghĩa những bạn cũ hơn một chút xíu như 3.5, 
3.4 có hỗ trợ.
"""
help(sorted)