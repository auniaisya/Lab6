#i/user/bin/phyton

from decimal import Decimal,getcontext
from timeit import default_timer as timer

def pi(precision):
	getcontext().prec = precision
	return sum(1/Decimal(16)**k *
		Decimal(4)/(8*k+1) -
		Decimal(2)/(8*k+4) -
		Decimal(1)/(8*k+5) -
		Decimal(1)/(8*k+6)
for k in range (precision))

start = timer()
values =(1000,1500,2000)
data=list(map(pi,values))
print(data[0])
print("")
print (data[1])
print("")
print(data[2])

end = timer()
print("")
print(f'sequentially:{end - start}')

