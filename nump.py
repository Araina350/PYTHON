import numpy as np
sd = [('name','S15'),('class',int),('height',float)]
student_d = [('Raj',5,48.5),('Araina',5,63),('Anam',5,61),('Subhanah',5,65)]
student = np.array(student_d, dtype=sd)
print("Original Array:")
print(student)
print("After sorting by height:")
print(np.sort(student, order="height"))