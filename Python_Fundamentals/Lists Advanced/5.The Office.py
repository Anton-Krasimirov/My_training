# employers = input().split(" ")# map(int, input().split(" "))
# happy_factor = int(input())
#
# filterd = []
#
# for i in employers:
#     b = int(i) * happy_factor
#     filterd.append(b)
# # employers = list(map(lambda x: int(x) * happy_factor, employers))
# filterd = list(filter(lambda x: x >= (sum(filterd) / len(filterd)), filterd))
# # filter priema parametar i spisak : parametara e celiq string v (lambda), filterd e spisaka
# # filter(funkciq, spisak)
# if len(filterd) >= len(employers) / 2:
#     print(f"Score: {len(filterd)}/{len(employers)}. Employers are happy!")
# else:
#     print(f"Score: {len(filterd)}/{len(employers)}. Employers are not happy!")

employers = [int(n) for n in input().split(" ")]
happy_factor = int(input())

happy_index = [v * happy_factor for v in employers]
average = sum(happy_index) / len(employers)
filterd = list(filter(lambda x: x >= average, happy_index))
happy_count = len(filterd)
total_count = len(employers)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employers are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employers are not happy!")

