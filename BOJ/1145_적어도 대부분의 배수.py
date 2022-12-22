N = list(map(int,input().split()))
x = 4
while(True):
    cnt = 0
    for n in N:
        if x % n == 0:
            cnt = cnt + 1
    if (cnt >= 3):
        break
    x = x + 1
print(x)

# S2onsal_log