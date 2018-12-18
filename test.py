# word = 'aabbbccdea'
# dc = {}
# w = set(word)
# for i in w:
#     dc[i] = word.count(i)
# print(dc)

n = int(input())
integer_list = map(int, input().split())
tup = ()
for i in integer_list:
    tup = tup + (i,)

print(tup)