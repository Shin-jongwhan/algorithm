import time
from collections import deque

ls = list(range(0, 1000000000))
dq = deque(ls)

# 리스트 시간 계산
print("리스트 ls = [i] + ls")
flAvg = 0
for i in range(0, 10) : 
	start_time = time.time()
	ls = [i] + ls
	elapsed_time = time.time() - start_time
	flAvg += elapsed_time
	print(elapsed_time)

flAvg = flAvg / 10
print("평균 : {0}\n".format(flAvg))

# deque appendleft() 시간 계산
print("deque appendleft()")
flAvg = 0
for i in range(0, 10) : 
	start_time = time.time()
	dq.appendleft(i)
	elapsed_time = time.time() - start_time
	flAvg += elapsed_time
	print(elapsed_time)

flAvg = flAvg / 10
print("평균 : {0}\n".format(flAvg))