# xử lí file trong file python
# Mở file bằng hàm open
#Cú pháp:
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

#Công dụng: Ở mức độ cơ bản, chúng ta sẽ chỉ quan tâm đến 2 parameter: file và mode.
""" mode 
r : Mở để đọc. đây là mặc định
r+: Mở để đọc và ghi
w : Mở để ghi, trước đó sẽ xoá hết nội dung của file hiện có. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
w+: Mở để đọc và ghi, trước đó sẽ xoá hết nội dung của file hiện có. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
a : Mở để ghi. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
a+: Mở để ghi, đọc. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào"""

file_object = open('test.txt', mode='r+') # trỏ đến cùng đường dẫn với file py đang hoạt động
print(file_object)
print(type(file_object))
# đọc file
'''Cú pháp:
<File>.read(size=-1)

Công dụng: Nếu size bị bỏ trống hoặc là một số âm. Nó sẽ đọc hết nội dung của 
file đồng thời đưa con trỏ file tới cuối file. Nếu không nó sẽ đọc tới n kí tự 
(với n = size) hoặc cho tới khi nội dung của file đã đọc xong.

Sau khi đọc được nội dung, nó sẽ trả về dưới một dạng chuỗi.
Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0'''
data = file_object.read(-1)
print(data)
# đóng file
file_object.close()

#readline : đọc từng dòng 
'''Cú pháp:
<File>.readlines(hint=-1)

Ở mức độ cơ bản, ta không phải quan tâm đến parameter hint.

Công dụng: Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. 
Với các phần tử trong list là mỗi dòng của file.

Con trỏ file sẽ được đưa  tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines. 
Bạn sẽ nhận được một list rỗng.'''
file_object = open("test.txt")
print(file_object.readline()) 
print(file_object.readline())
file_object.close()
# readlines đọc full.
file_object = open("test.txt")
print(file_object.readlines())  #['Hello everybody\n', "My name's Thang\n", 'HUST']
file_object.close()
# cũng có thể là 1 list . 1 tuple
file_object = open("test.txt")
print(list(file_object))        #['Hello everybody\n', "My name's Thang\n", 'HUST']
file_object.close()
file_object = open("test.txt")
print(tuple(file_object))       #('Hello everybody\n', "My name's Thang\n", 'HUST')
		# đều đưa con trỏ file về cuối file..
