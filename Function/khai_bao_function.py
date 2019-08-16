"""
Cú pháp:
def <function_name>(parameter_1, parameter_2, .., parameter_n):

    function-block
def function():   
    pass #Lệnh pass ở trên là một lệnh “giữ chỗ” (placeholder statement) để giúp cho các block 
    		của Python không bị thiếu câu lệnh trong trường hợp bạn chưa biết viết gì cho phù hợp.

Trong cú pháp đó, bạn không được bỏ sót bất kì thứ nào ngoại trừ bạn có thể bỏ trống các parameter.
Bạn có thể thấy, khi in ra hàm kteam, bạn sẽ nhận được một dòng khá tương một một generator expression.
"""
def Thang():
	print("Thang dep trai")
Thang()
#Parameter và Argument
def Inra(text):
	print(text)
Inra("haaaaa")
#Giá trị mặc định của parameter (Default argument)
def guiThu(ten, default_argument = "Hello"):
	print(default_argument, ten, end="! \n")

guiThu("Thang")
guiThu("Tran", "Hi")

# 
def f(lean=[]):
    lean.append('F')
    print(lean)

f()
f()
