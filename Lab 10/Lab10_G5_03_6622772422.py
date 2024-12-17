import numpy as np

data = np.loadtxt("TSV/grade.tsv", delimiter=" ", dtype=float)

student_ids = data[:, 0]
student_grades = data[:, 1:]

credits = np.array([3, 2, 1, 3, 3, 3])

gpas = np.sum(student_grades * credits, axis=1) / np.sum(credits)

print("Student ID \t GPA")
for i in range(len(student_ids)):
    print("%s \t %.2f" % (student_ids[i], gpas[i]))