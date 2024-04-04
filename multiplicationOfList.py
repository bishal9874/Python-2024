# Multiplication of 2 Lists Elements using For Loop

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = []

for i in range(len(list1)):
    result.append(list1[i] * list2[i])

print("Result:", result)
