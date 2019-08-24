"""Cấu trúc vòng lặp while-else và cách hoạt động
Ta sẽ xem cấu trúc trước:

while expression:

    # while-block

else:

    # else-block

Cấu trúc này gần tương tự như while bình thường. Thêm một điều, khi vòng vòng lặp
 while kết thúc thì khối lệnh else-block sẽ được thực hiện."""
k=0;
while k<3:
	print('value of k is', k)
	k+=1
else:
	print("aaaa")