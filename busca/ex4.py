a = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == x:
            print(a[i], a[j])

#O(nˆ2)