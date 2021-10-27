from datetime import datetime
import unittest
now=datetime.now()
x=now.strftime("%-M")
a=10
n= int(x) % 2
print(x)
if n==0:
	b=4
else:
	b=2
c=a/b	
print(c)
