'''def SUM(v1, v2):
    return(v1 + v2)

v1 = 1
v2 = 7
ans = SUM(v1, v2)
print(ans)'''


def SUM(n):
    ans = 0
    for i in n:
        ans += i
    return ans

n = [1, 2, 3, 4, 5]
print(SUM(n))


