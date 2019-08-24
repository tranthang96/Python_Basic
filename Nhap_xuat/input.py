'''
	cú pháp: input(prompt=None)
Lưu ý: Có lúc bạn sẽ nhìn thấy cú pháp của nó là input(prompt=None, /). 
Cái phần thêm vào là kí tự / chỉ là một kí tự cho biết parameter prompt 
chỉ nhận giá trị dưới dạng positional argument. Nghĩa là khi bạn truyền vào cho hàm, 
bạn không được phép điền thêm chữ prompt
Parameter prompt là một parameter tùy chọn. Bạn có thể nhập hoặc không vì nó đã có giá trị mặc
 định là None.

Công dụng: Hàm này giúp chúng ta đọc một chuỗi từ standard input (hiểu nôm na là việc bạn nhập 
dữ liệu lên trên Shell) sau đó trả về cho chúng ta. Và vì nó là đọc một chuỗi, nên dù bạn có nhập 
cái gì đi  chăng nữa thì nó  vẫn là một chuỗi dù là số, list, tuple, set, dictionary,…

Việc nhập sẽ kết thúc sau khi bạn nhấn phím enter. Ở đây, khi bạn nhấn phím enter (phím return) 
thì cũng đồng nghĩa với việc bạn gửi vào một kí tự newline. Nhưng kí tự newline này sẽ bị bỏ đi.

Nếu trong lúc nhập bạn nhấn EOF

'''
value = input() # prompt để None
print('first value is =>', value)
next_value = input('please enter one more value: ')
print('The second value is =>', next_value)
#=============== input : nhập vào là một chuỗi====
# reading input
int_num = input('Enter an integer: ')
float_num = input('Enter a float: ')
lst = input('Enter a list: ')
tup = input('Enter a tuple: ')
set_ = input('Enter a set: ')
dict_ = input('Enter a dict: ')

# print out output
print('Type of int_num', type(int_num))
print('Type of float_num', type(float_num))
print('Type of lst', type(lst))
print('Type of tup', type(tup))
print('Type of set_', type(set_))
print('Type of dict_', type(dict_))

value = input('Enter something => ')
print('You just entered', value)
print('__repr__ method: %r' %value)