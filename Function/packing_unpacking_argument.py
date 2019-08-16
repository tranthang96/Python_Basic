# Function trong Python - Packing và unpacking arguments
# Unpacking arguments với *
# Giả sử, bạn có một hàm thế này
def thang(a,b,c,d):
	print(a)
	print(b)
	print(c)
	print('hết roài', d)
lst = ['123',"hahahaa",123,111]

thang(lst[0],lst[1],lst[2],lst[3])
# Phức tạp vấn đề lên một chút nào! Sẽ ra sao nếu bạn có 
	#50 parameter và phải gõ hết 50 indexing để truyền vào cho hàm khi gọi nó?

#Vậy nên, Python cho phép làm điều đó đơn giản chỉ bằng một dấu *
thang(*lst)       
"""Khi bạn sử dụng *, bạn không chỉ có thể unpack được các List mà bên cạnh đó bạn có thể 
unpack các container khác như Tuple, Chuỗi, Generator, Set, Dict (chỉ lấy được key).

Lưu ý:

Pass argument bằng cách unpacking argument như thế này là đang truyền vào dưới dạng positional argument.
 Hãy cẩn thận sử dụng kĩ thuật này với những hàm có parameter dạng keyword-only argument.

 Bạn còn nhớ hàm print chứ? Nó có khả năng nhận được bao nhiêu argument cũng được. 
 Làm sao nó làm được như thế?

Đó chính là nhờ packing argument. 
Đôi lúc, bạn sẽ không thể biết trước được bạn sẽ pass vào bao nhiêu argument. 
Việc kiểm soát điều đó đôi lúc là bất khả thi.

Khi bạn sử dụng packing argument. Đồng nghĩa với việc bạn nhờ  một biến đi gói tất cả các giá trị truyền 
vào cho hàm bằng positional argument thành một Tuple. Nếu không có gì để gói 
(bạn không truyền vào bất cứ argument nào) thì bạn sẽ nhận được một tuple rỗng.
 Để giao nhiệm vụ cho một biến làm công việc này, bạn đặt một dấu * trước nó."""
def Packing_arg(*args):
	print(args)
	print(type(args))
Packing_arg(*(x for x in range(2,16,2)))

def Packing_arg(*args,var1):
	print(args)
	print(type(args))
	print(var1)
Packing_arg(*(x for x in range(2,16,2)),var1="heeee") # cần truyền vào keyword argument
"""
Ở những ví dụ trên các bạn có thể thấy Kteam sử dụng biến packing có tên là args. 
Đó không phải là ngẫu nhiên mà là một quy ước nhỏ của các Pythonist với nhau. 
Thường người ta sẽ sử dụng biến có tên là args (viết gọn của arguments) để làm biến packing.
"""
Packing arguments với **
Đã có unpacking với ** thì cũng phải có packing. Khác với dấu * là gói những 
positional argument thì ** lại gói các keyword argument. 
Và đương nhiên, nó sẽ gói trong một Dict. Nếu không truyền gì vào sẽ 
là một dict rỗng.

>>> def kteam(**kwargs):
...     print(kwargs)
...     print(type(kwargs))
...

>>> kteam(name='Kteam', member=69)
{'name': 'Kteam', 'member': 69}
<class 'dict'>
1
2
3
4
5
6
7
8
Tên biến kwargs (viết gọn của keyword arguments) cũng là một quy ước đặt tên.

>>> def kteam(**kwargs):
...     for key, value in kwargs.items(): # phương thức items của kiểu dữ liệu Dict
...         print(key, '=>', value)
...
>>> kteam(id=3424, name='Henry', age=18, lang='Python')
id => 3424
name => Henry
age => 18
lang => Python

Lưu ý: bạn không được phép bỏ các positional parameter sau biến packing mà có ** giống như với *.

>>> def f(**a, b):
  File "<stdin>", line 1
    def f(**a, b):
               ^
SyntaxError: invalid syntax
1
2
3
4
5
Nhờ những kiến thức trên, bạn có thể có một hàm cực kì linh hoạt như sau

def best_function_ever(*args, **kwargs):
# việc còn lại của bạn là thỏa sức biến tấu
	pass

Bạn hãy nắm chắc kĩ thuật này, tuy đơn giản nhưng lại được sử dụng rất nhiều.