a = [4, 15, 17, 20, 9, 7]
m = len(a)

def peak(a, n):
    if a[0] >= a[1]:
        return 0
    if a[n-1] >= a[n-2]:
        return n -1
    for i in range (1, n-1):
        if a[i] >= a[i-1] and a[i] >= a[i+1]:
            return i

print("The index of peak is", peak(a, n))