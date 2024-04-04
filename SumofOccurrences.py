# Write a program to find the number of occurrence of an element in a numeric only list and find the sum of that element and store it in another list.
original_list = [1, 2, 2, 3, 4, 4, 5]
element_to_find = 2

occurrences = original_list.count(element_to_find)
sum_of_occurrences = occurrences * element_to_find

print("Number of occurrences of", element_to_find, ":", occurrences)
print("Sum of occurrences:", sum_of_occurrences)
