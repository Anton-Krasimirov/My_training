line = input()
tot_streigth = 0# stoinosta shte mahne 1 po 1 tolkova stoinosti sled poslednoto >

i = 0# za da spre while cikala

while i < len(line):
    ch = line[i]

    if ch == ">":
        streigth = int(line[i + 1])
        tot_streigth += streigth
    else:
        if tot_streigth > 0:
            line = line[:i] + line[i + 1:]
            i -= 1# za da zapoche ot premahnatata stoinost
            tot_streigth -= 1
    i += 1
print(line)