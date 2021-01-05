import os

min_1=0
min_2=0

sec_1=0
sec_2=0
while min_1 != 6:
	if sec_2 == 9  or sec_1 == 6 and sec_2 == 0:
		sec_2 = 0
		if sec_1 == 6 and sec_2 == 0:
			sec_1 =0
			if min_2 ==9:
				min_2 = 0
				min_1 += 1
			else:
				min_2 += 1
		else:
			sec_1 += 1
	else:
		sec_2 +=1
	print(str(min_1) + str(min_2) +str(sec_1) +str(sec_2) )