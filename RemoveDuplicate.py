#  Remove Duplicate Elements from a List

original_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for num in original_list:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List:", unique_list)
