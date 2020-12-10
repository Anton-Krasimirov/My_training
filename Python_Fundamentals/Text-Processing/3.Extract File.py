text = input().split("\\")

info = text[-1]

name, extention = info.split(".")

print(f'File name: {name}\nFile extension: {extention} ')