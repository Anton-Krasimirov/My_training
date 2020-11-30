import re

text = input()

pattern = r'(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b'

phone = re.findall(pattern, text)

print(', '.join(phone))

# import re
#
# text = input()
#
# pattern = r'(\+359-2-\d{3}-\d{4}\b)|(\+359 2 \d{3} \d{4}\b)'
#
# phone = re.finditer(pattern, text)
# for x in phone:
#     print(x.group(0))