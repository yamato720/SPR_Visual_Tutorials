# 在此处编写代码
n = int(input())
l = [[],[]]
for i in range(n):
    l[0].append(1)
    for j in range(8):
        string = input()
        l[1].append(string)
    for k in range(0,i-1):
        if l[1][i*8:i*8+8] == l[1][k*8:k*8+8]:
            l[0][i]+=1
print(l[0])