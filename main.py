# Visualize number of object in annotation files (YOLO)

import matplotlib.pyplot as plt
import numpy as np
import os

directory = os.getcwd()
classes = []

with open('merge_from_ofoct.txt', 'r') as txt:
    lines = txt.readlines()

for line in lines:
    line = line.strip()
    if line:
        classes.append(line[0])

print("Classes: " + str(classes))

unique = np.unique(classes)

object = []
quantity = []

for i in unique:
    print("Class " + i, "occurs: " + str(classes.count(i)) + " x")
    object.append(i)
    quantity.append(classes.count(i))
    plt.bar(object, quantity)

plt.title("Number of classes in the set")
plt.show()


