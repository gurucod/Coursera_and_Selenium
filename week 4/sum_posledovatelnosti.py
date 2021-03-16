def nsun():
    n = int(input())
    if n != 0:
        n = n + nsun()
    return n


print(nsun())
