count_student = int(input())
course_lectures = int(input())
additional_bonus = int(input())

max_bonus = {}
for i in range(count_student):
    student_attendances = int(input())
    total_bonus = (student_attendances / course_lectures) * (5 + additional_bonus)
    total_bonus = round(total_bonus)
    max_bonus[total_bonus] = student_attendances
print(f'Max Bonus: {max(max_bonus.keys())}.\nThe student has attended {max(max_bonus.values())} lectures.')
#
# count_student = int(input())
# course_lectures = int(input())
# additional_bonus = int(input())
#
# max_bonus = []
# max_lactures = []
# for i in range(count_student):
#     student_attendances = int(input())
#     total_bonus = (student_attendances / course_lectures) * (5 + additional_bonus)
#     total_bonus = round(total_bonus)
#     max_bonus.append(total_bonus)
#     max_lactures.append(student_attendances)
# count_max_bonus = max(max_bonus)
# num = max_bonus.index(count_max_bonus)
#
# print(f'Max Bonus: {count_max_bonus}.')
# print(f'The student has attended {max_lactures[num]} lectures.')





