# Write a program to demonstrate square of every alternate list elements and append it to another list using for loop
original_list = [1, 2, 3, 4, 5, 6]
result_list = []

for i in range(len(original_list)):
    if i % 2 != 0:
        result_list.append(original_list[i] ** 2)

print("Result List:", result_list)
