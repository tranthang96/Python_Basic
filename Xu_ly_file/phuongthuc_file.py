#phuong thuc file
# write 
file_object = open("test.txt",mode="a+") #mode a+ đưa con trỏ về cuối file luôn
data = file_object.write(" - Ha Noi Univercity of techonogy")
print(data)   # trả về độ dài file ghi vào
file_object.close()
#===========Phương thức seek===============
'''Cú pháp:
<File>.seek(offset, whence=0)

Với Python 3.X. Một text file sẽ chỉ được sử dụng whence = 0. whence = 1 hoặc whence = 2 
chỉ sử dụng với binary file.

Với Python 2.X thì bạn không phải quan tấm vấn đề này.

Do đó, ta cũng không cần quan tâm tới parameter whence.

Công dụng: Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự.
 Và parameter offset phải là một số tự nhiên.

Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file.
Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file.'''
file_object = open("test.txt",mode="r")
print(file_object.read())
file_object.seek(0)    #đưa con trỏ về đầu file
print(file_object.read())
file_object.close()
# with với file trong python
"""
with expression [as variable]:
    with-block 
Nhớ rằng with-block nằm thụt vào so với dòng with expression 
(theo chuẩn PEP8 là 4 space và là dùng space không dùng tab)

Câu lệnh này liên quan đến phương thức __enter__ và __exit__ của đối tượng. 

Đặc điểm của câu lệnh with khi sử dụng với file là. Khi kết thúc with-block. 
File sẽ được đóng.
"""
with open('test.txt') as fobj:
    data = fobj.read()
print(data)

