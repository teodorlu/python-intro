name = input("Hi! I'm Python. Who are you? ")

print("Name some things you like!")
things = []

while True:
    thing = input("I like this: ")
    if thing is "":
        break
    else:
        things.append(thing)

for thing in things:
    print(name + " likes " + thing + "!")
