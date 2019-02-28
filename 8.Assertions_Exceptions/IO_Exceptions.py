import numpy as np

data = []

file_name = input('Provide a name of a file of data ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        # if it is not an empty row
        if new != '\n':  # new line character
            addIt = new[:-1].split(',')  # remove trailing \n and csv
            data.append(addIt)
    fh.close()

gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades]])
        # if last element of a list is not integer, no vote assigned.
        except ValueError:
            gradesData.append([student[:], []])
