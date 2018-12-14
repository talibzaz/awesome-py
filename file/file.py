import json

f = open('text.txt', 'r+')
# f.write("Hello from python")

print(f.read())
x = {
	"name": "David",
	"title": "Principal"
}

print(json.dumps(x))

print(json.loads(open('text.txt', 'r').read()))