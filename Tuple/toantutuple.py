# toán tử trong tuple
# toán tử giống vs chuỗi.
# .......

#=== cộng 2 tuple===
tup = (1,2,3)
tup += (1,3,4,5)
print(tup)
#==== truy xuất tuple ====
a = tup[1]  # lưu ý là ngoặc vuông
print(a)
#=== đo độ dài, dùng hàm len====
b = len(tup)
print(b)
#......
# Tuple và chuỗi đều là một dạng hash object (immutable).
# Do đó việc bạn muốn thay đổi nội dung của nó trên lí thuyết là không.
# Nếu giá trị bên trong là một list (un hash object) thì ta có thể thay đổi nội dung được
tup1 = ([1,2,3]) # là một list
print(tup1)