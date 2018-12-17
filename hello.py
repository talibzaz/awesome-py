from itertools import combinations

m, s, n = input(), input().split(), int(input())
t = list(combinations(s, n))

print("s: ", s)
print("t: ", t)
f = [i for i in t if 'a' in i]
print(f)
print(len(f)/len(t))


# from collections import OrderedDict
#
# word = 'AABCAADAD'
#
# result = [word[i:i+3] for i in range(0, len(word), 3)]
#
# for i in result:
#     print("".join(OrderedDict.fromkeys(i)))