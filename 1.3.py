n = input ("inout a number:")
n = int(n)
sum_n = 0
for i in range(n+1):
    if i in [3,4,5]:
        continue
    sum_n = sum_n + i

# i=0
# while i<=n:
#     sum_n=sum_n+i
#     i=i+1


print (sum_n)
