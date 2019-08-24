'''Nào! Cùng ngó sơ cấu trúc, sau đó Kteam sẽ giải thích cho bạn cách mà nó hoạt động

while expression:

     # while-block '''
k=6;
while k>0:
	print("k=",k)
	k -= 1
s="Tran Viet Thang"
idx = 0 #vị trí muốn xử lý chuỗi
length = len(s)
while idx < length:
	print(idx, "In ra", s[idx])
	idx += 1 
#==== câu lệnh break===
five_even_number = [0]
number = 1
while 1:
	if number % 2 == 0:
		five_even_number.append(number) # thêm giá trị number
		if len(five_even_number) >=9: # nếu list đủ 9 phần tử
			break #thoát khỏi vòng lặp của while
	number += 1
print(five_even_number)
print(number)
# lệnh contine: thực hiện lệnh 
"""
Câu lệnh này dùng để chạy tiếp vòng lặp. Giả sử một vòng lặp có cấu trúc như sau:

while expression:

    #while-block-1

    continue

    #while-block-2

Khi thực hiện xong while-block-1, câu lệnh continue sẽ tiếp tục vòng lặp, 
không quan tâm những câu lệnh ở dưới continue và như vậy nó đã bỏ qua while-block-2."""