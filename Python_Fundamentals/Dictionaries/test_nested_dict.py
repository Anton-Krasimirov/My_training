# test_dict = {'gfg': {'best': 4, 'good': 5},
#              'is': {'better': 6, 'educational': 4},
#              'CS': {'priceless': 6}}
# print("The original dictionary : " + str(test_dict))
#
# rem_val = 6
#
# def rem_vals(ele):
#     global rem_val
#     key, val = ele
#     return val != rem_val
#
#
# res = dict()
# for key, val in test_dict.items():
#     if isinstance(val, dict):
#         res[key] = dict(filter(rem_vals, val.items()))
#     else:
#         res[key] = val
# print("Dictionary after removal : " + str(res))
#======================================================================================
# from collections import OrderedDict
# from operator import getitem
# # initializing dictionary
# test_dict = {'Nikhil': {'roll': 24, 'marks': 17},
#              'Akshat': {'roll': 54, 'marks': 12},
#              'Akash': {'roll': 12, 'marks': 15}}
# # printing original dict
# print("The original dictionary : " + str(test_dict))
#
# # using OrderedDict() + sorted()
# # Sort nested dictionary by key
# res = OrderedDict(sorted(test_dict.items(), key=lambda x: getitem(x[1], 'marks')))
# #
# # # print result
# print("The sorted dictionary : " + str(res))
#..........................................................................
# # initializing dictionary
# test_dict = {'Nikhil': {'roll': 24, 'marks': 17},
#              'Akshat': {'roll': 54, 'marks': 12},
#              'Akash': {'roll': 12, 'marks': 15}}
#
# # printing original dict
# print("The original dictionary : " + str(test_dict))
#
# # using sorted()
# # Sort nested dictionary by key
# res = sorted(test_dict.items(), key=lambda x: -x[1]['marks'])
#
# # print result
# print("The sorted dictionary by marks is : " + str(res))


# from collections import OrderedDict
#
# ordered = OrderedDict(sorted(a.items(), key=lambda i: i[1]['price']))
# #------------------------------
# for s in sorted(a.iteritems(), key=lambda (x, y): y['price']):
#        print s
# from collections import OrderedDict
# res = OrderedDict(sorted(a.items(), key=lambda x: x[1]['price'], reverse=False))
#     print res
# #---------------------------------------------------------
# сортиране на влоожен речник работещо решиение
# from collections import OrderedDict
# from operator import getitem
#
# sorted_dict = OrderedDict(sorted(a.items(), key = lambda x:getitem(x[1],'price')))
#
# # print(sorted_dict)
# NestedDict = {'1': {2: 0.3, 7: 0.5, 4: 0.4, 3: 0.75},
#               '2': {5: 0.3, 7: 0.5, 4: 0.4, 1: 0.75},
#               '3': {15: 0.3, 7: 0.5, 4: 0.4, 70: 0.75}}
#
# keys = [k for k in NestedDict.keys()]
# print(keys)
# dict_values = [v for v in NestedDict.values()]
# print(dict_values)
# dict_values = [dict(sorted(x.items(), key=lambda kv: -kv[1])) for x in dict_values] # or OrderedDict
# print(dict_values)
# NestedDict = dict(zip(keys, dict_values)) # or OrderedDict
# print(NestedDict)
#=============================================================================
# сортиране на влоожен речник работещо решиение
nesteddict = {'Nikola': {'Part One Interview': '120', 'C# Fundamentals': '200'},
              'Tanya': {'C# Fundamentals': '350', 'Algorithms': '380', 'Part One Interview': '220', 'Js Fundamentals': '400'}}

keys = [k for k in nesteddict.keys()]
print(keys)
dict_value = [v for v in nesteddict.values()]
print(dict_value)
dict_values = [dict(sorted(x.items(), key=lambda kv: kv[1], reverse=True)) for x in dict_value]
print(dict_values)
nesteddict = dict(zip(keys, dict_values))

print(nesteddict)
for k, v in nesteddict.items():
    print(k)
    for n in v:
        print(n, v[n])
#=================================================================================
# принтиране на вложен речник
# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
#
# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
#
#     for key in p_info:
#         print(key + ':', p_info[key])