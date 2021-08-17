a = [19,2,31,45,6,11,121,27]

def sortdown(a):
    lenght = len(a)
    for i in range(lenght):
        for j in range(0,lenght-i-1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print(sortdown(a))