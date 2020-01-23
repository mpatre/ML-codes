import itertools
from itertools import permutations
list4=list()
for time in range (1,60):
	list1=['Start the oven ','Switch on the oven ']
	list2=['at 65 degrees ','at 70 degrees ','at 75 degrees ','at 80 degrees ','at 85 degrees ','at 90 degrees ','at 95 degrees ','at 100 degrees ']
	list3=['for %d seconds'%time]
	res=[[i,j,k] for i in list1
				for j in list2
				for k in list3]
	for y in range(len(res)):
			str1=''.join(res[y][x] for x in range(3))
			list4.append(str1)
print(list4)
