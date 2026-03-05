import numpy as np

order1 = input("Enter the numbers for array1: ")
list_1_of_numbers = order1.split()

order2 = input("Enter the numbers for array2: ")
list_2_of_numbers = order2.split()

array1 = np.array(list(map(int, list_1_of_numbers)))
array2 = np.array(list(map(int, list_2_of_numbers)))

array_sum = array1 + array2
print(array_sum)
