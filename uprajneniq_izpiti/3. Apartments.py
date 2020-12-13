data = input()

split_data = data.split(" -> ")
neighborhood = split_data[0]
bl_num_str = split_data[1].split(",")
# l_bl_num = list(map(int, bl_num_str[::-1]))
l_bl_num = map(str, bl_num_str[::-1])
neigh_and_bl = list(map(lambda n: split_data[0] + "&" + n, l_bl_num))

print(neigh_and_bl)

