def cubesum(n):

 sum = 0
 for i in range(1,n+1):
   sum = sum + (i*i*i)
 return sum

n = 2
print(cubesum(n))
