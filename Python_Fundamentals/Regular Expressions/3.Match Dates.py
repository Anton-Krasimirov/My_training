import re
pattern = r"(\d{2})([\.\-/])([A-Z][a-z]{2})\2(\d{4})"# moje i s \b....\b ako e nujno v judj

text = input()

res = re.findall(pattern, text)
for r in res:
    day, sim, month, year = r
    print(rf"Day: {day}, Month: {month}, Year: {year}")

# import re
# pattern = r"(?P<day>\d{2})(?P<separator>[\./\-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
#
# text = input()
#
# res = re.finditer(pattern, text)
# for r in res:
#     x = r.groupdict()
#     print(rf"Day: {x['day']}, Month: {x['month']}, Year: {x['year']}")