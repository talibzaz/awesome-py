t = 1234, 5678, 'hello!'
print(len(t))

basket = {'apple', 'orange', 'mango', 'apple'}

print('orange' in basket)

a = set(basket)

print(a)

dc = {'jack': 4097, 'Mack': 2000}
dc['jack'] = 1

for k, v in dc.items():
    print(k,v)