l = [5, 8, 1, 3, 2]
search_for = 8

result = -1

for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break

print(result)