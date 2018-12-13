words = ['cat', 'dogs', 'elephants']

for w in range(len(words)):
    print(w, words[w])


x = int(input("Please enter an integer number: "))

if x < 0:
    print("x is less than 0")

elif x > 0 and x <100:
    print("value of x is between 1 and 99")
else:
    print("x is greater or equal to 100")