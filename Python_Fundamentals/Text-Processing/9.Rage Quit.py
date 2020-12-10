line = input()
total_result = ""
mid_result = ''
i = 0
while i < len(line):
    ch = line[i]
    if ch.isdigit():
        count = ch
        idx = i + 1
        if idx < len(line) and line[idx].isdigit():
            count += line[idx]
            i += 1
        total_result += mid_result.upper() * int(count)
        mid_result = ''
    else:
        mid_result += ch
    i += 1
print(f'Unique symbols used: {len(set(total_result))}')
print(total_result)


# line = input()
# total_result = ""
# mid_result = ''
#
# for i in range(len(line)):
#     if line[i].isdigit():
#         ch = line[i]
#         idx = i + 1
#         while idx < len(line) and line[idx].isdigit():
#             ch += line[idx]
#             idx += 1
#         total_result += mid_result.upper() * int(ch)
#         mid_result = ''
#
#
#     else:
#         mid_result += line[i]
# print(f'Unique symbols used: {len(set(total_result))}')
# print(total_result)

