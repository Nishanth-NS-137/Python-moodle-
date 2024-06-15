n = int(input())
student_dict = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    test_mark, assignment_mark, lab_mark = map(int, data[1:])
    student_dict[name] = (test_mark, assignment_mark, lab_mark)

average_scores = {name: sum(marks) / len(marks) for name, marks in student_dict.items()}

highest_average_score = max(average_scores.values())
highest_average_students = sorted([name for name, score in average_scores.items() if score == highest_average_score])

highest_assignment_mark = max([marks[1] for marks in student_dict.values()])
highest_assignment_students = sorted([name for name, marks in student_dict.items() if marks[1] == highest_assignment_mark])

lowest_lab_mark = min([marks[2] for marks in student_dict.values()])
lowest_lab_students = sorted([name for name, marks in student_dict.items() if marks[2] == lowest_lab_mark])

lowest_average_score = min(average_scores.values())
lowest_average_students = sorted([name for name, score in average_scores.items() if score == lowest_average_score])

print("\n".join([
    " ".join(highest_average_students),
    " ".join(highest_assignment_students),
    " ".join(lowest_lab_students),
    " ".join(lowest_average_students)
]))
