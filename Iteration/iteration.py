# ========iteration : là một khái niệm chung cho việc lấy từng phần tử của một đối tượng nào đó, 
# bất cứ khi nào bạn sử dụng vòng lặp hay kỹ thuật nào đó để lấy được giá trị một nhóm phần 
# tử thì đó là thì chính là iteration

#==========iterable object trong python=============
#Iterable object là một object có phương thức __iter__ trả về một iterator, 
#hoặc là một object có phương thức __getitem__ cho phép bạn lấy bất cứ phần tử nào của nó
#bằng indexing ví dụ như Chuỗi, List, Tuple
 # (hiểu đơn giản là tập hợp của nhiều thằng kết hợp lại, có sự liên kết vs nhau)
'''
#Giới thiệu iterator object trong Python
Iterator object đơn giản chỉ là một đối tượng mà cho phép ta lấy "từng giá trị" một của nó. 
Có nghĩa là bạn không thể lấy bất kì giá trị nào như ta hay làm với List hay Chuỗi.

Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ trợ như 
file object sẽ có phương thức seek.

Iterator sử dụng hàm next để lấy từng giá trị một. 
Và sẽ có lỗi StopIteration khi bạn sử dụng hàm next lên đối tượng đó trong khi nó hết giá trị đưa ra cho bạn.

Các iterable object chưa phải là iterator. Khi sử dụng hàm iter sẽ trả về một iterator. 
Đây cũng chính là cách các vòng lặp hoạt động.'''
#VD:
itera = [x for x in range(3)]
print(itera)                  # ngoặc vuông là một list 
itera = (x for x in range(3))
print(itera)                  #<generator object <genexpr> at 0x0369AC70> là 1 iteration hay
							  # đây là một cách tạo ra iteratio
print(next(itera)) 			#truy xuất từng thằng với next
print(next(itera)) 	
print(next(itera)) 	
# print(next(itera)) 	# lỗi , do hết phần tử
# generator object không thể truy xuất trực tiếp với index của nó
#   VD :  print(itera[0]) ==> lỗi
#===== tạo iteration với list
list1 = [x for x in range(4)] + [[1,2,3]]
print(list1)
iter_list = iter(list1)
print(iter_list)     #<list_iterator object at 0x02F0FDD0>
#   print(iter_list[0]) # đương nhiên, iterator không hỗ trợ indexing
print(next(iter_list))   #0
print(next(iter_list))		#1
print(next(iter_list))		#2 
print(next(iter_list))		#3 
print(next(iter_list)[-2])  #4 [1,2,3] vị trí trừ 2 có giá trị là 2
# # iterator này cũng dính một vấn đề như List, Dict đó chính là chỉnh một, thay đổi hai. do cùng lấy giá 
#trị tại một chỗ
it_1 = iter('Thang')
print(it_1)  			#<str_iterator object at 0x01670910>
it_2 = it_1
print(next(it_1))
print(next(it_1))
print(next(it_2))      # lấy tiếp giá trị in ra  là chữ: a
