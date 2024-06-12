from itertools import product

list_A = [[1,2,3],[2,3,4]]
res = list(product(*list_A)) # 표현 주의!
print (*res, sep='/')
product()