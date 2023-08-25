student_count = int(input())
students = dict()

for _ in range(student_count):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grade in students.items():
    print(f"{student} -> {' '.join(str(f'{grade:.2f}') for grade in grade)} (avg: {str(f'{sum(grade)/len(grade):.2f}')})")