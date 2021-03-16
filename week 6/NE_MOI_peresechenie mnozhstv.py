a = list(map(int, input().split()))
b = list(map(int, input().split()))


def Intersection(A, B):
    r = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            r.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
    return r


print(*Intersection(a, b))
