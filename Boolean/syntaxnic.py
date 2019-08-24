# Syntaxnic (cú pháp) sugar cho việc so sánh trong Python
"""
Nếu bạn từng học một số ngôn ngữ lập trình khác. Bạn đôi lúc phải kiểm 
tra những trường hợp như kiểu tra một số n có nằm trong khoảng (a; b), 
đoạn [a; b], nửa khoảng (a; b], nửa khoảng [a; b) hay không? hoặc là 
kiểm tra xem một số k có bằng một trong những số như x, y hoặc z hay không. 
Đương nhiên, những lần làm như vậy cũng làm bạn hơi cực
"""
n = 5
n > 1 and n < 6 # kiểm tra xem n có nằm trong khoảng (1; 6) hay không
#True
n > 1 and n < 4 # kiểm tra xem n có nằm trong khoảng (1; 4) hay không
#False

#Nhưng với Python, bạn có thể làm thế này.
a = 5
1 < a < 6
#True
b = -4
b < -3 < -1 < 0 < a < 6 # thậm chí là dài như thế này
#True

#Với trường hợp nếu bạn muốn kiểm tra xem một số k có bằng x hoặc y 
	#hoặc là z hay không thì thường bạn phải viết khá dài.

k = 4
k == 3 or k == 4 or k == 5
#True

#Tuy nhiên, bạn cũng có thể

k in (3, 4, 5) # nên dùng () hơn là [] hoặc thứ gì khác
#True