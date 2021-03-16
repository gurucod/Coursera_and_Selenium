def ha(A, K):
    a = list(map(int, A.split()))
    while K != len(a) - 1:
        a[K] = a[K + 1]
        K += 1
    a.pop()
    return a


A = input()
K = int(input())

print(ha(A, K))
