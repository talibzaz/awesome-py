def ask_ok(prompt, retries=3, reminder='Please try again!'):

    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def func(a, L=[]):
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def funcWithTupple(kind, *arguments, **keywords):
    print("Value of kind is: ", kind)

    for arg in arguments:
        print(arg)

    for kw in keywords:
        print(kw, ":", keywords[kw])

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(1))
print(f(2))

# print(func(1))
# print(func(2))

# ask_ok('Do you really want to quit?')

# parrot(10)

# funcWithTupple("myKind", "it is raining", "it is really raining", shopkeeper="Michael", client="Jim")
