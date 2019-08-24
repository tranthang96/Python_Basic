for i in (1,2,3):
	print(i)
else:
	print('Done!')
#++++ có break
for i in (1,2,3):
	print(i)
	if(i%2==0): 
		break      # gặp break thoát khỏi vòng for_else luôn
else:
	print('Done!')
#=====continue
for i in (1,2,3):
	if(i%2==0): 
		continue        # gặp continue bỏ qua lệnh bên dưới quay lại for => program ko in 2
	print(i)
else:
	print('Done!')
# VD tính tổng
set_ = {0,1,2,3,4,5}
S=0
for i in set_:
	S=S+i
else:
	print(S)