# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.

iterations = int(input())
students = [[input(), float(input())] for _ in range(iterations)]


scores = set()
for student in students:
    name = student[0]
    score = student[1]
    scores.add(score)

sorted_scores = sorted(scores)
second_lowest = sorted_scores[1]

names = []
for name, score in sorted(students):
    if score == second_lowest:
        names.append(name)

print("\n".join(names))


# Sample Input

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39


# Sample Output

# Berry
# Harry


