t = 1234, 5678, 'hello!'
print(len(t))

basket = {'apple', 'orange', 'mango', 'apple'}

print('orange' in basket)

a = set(basket)

print(a)

states = {
    'Jammu and Kashmir': 'J&K',
    'Punjab': 'PB',
    'Madhya Pradesh': 'MP',
    'Maharashtra': 'MH'
}

for k, v in states.items():
    print(k, v)

state = states.get('Maharashtra')
print(state)
print(states['Punjab'])

