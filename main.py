grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
sorted_list = sorted(my_list)
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
j = sum(grades[2]) / len(grades[2])
k = sum(grades[3]) / len(grades[3])
s = sum(grades[4]) / len(grades[4])
average = {sorted_list[0]: a, sorted_list[1]: b, sorted_list[2]: j, sorted_list[3]: k,
           sorted_list[4]: s}
print(average)
