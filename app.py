# Selection sort is used to sort the salaries into ascending order
# sorting by finding min_index
def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


salary = [500.0, 300.0, 700.0, 400.0, 600.0, 550.0]
size = len(salary)
selectionSort(salary, size)
print("The employees salaries are as follows in ascending order.")
print(salary)

import numpy as np

# Finds the average of all values in the array
arr = np.array(salary)

total = arr.sum()
avg = np.average(arr)

print('\nThe average salary of all the employees is = ', avg)

# Increases the values in the array by 5 percent
salaryRaise = 1.05
salary = arr*salaryRaise
print('\nThe salaries would be as follows if each employee was given a 5 percent raise.')
print(salary)