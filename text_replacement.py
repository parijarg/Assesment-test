import os


def replacing():
    with open("example.txt", 'r') as f:
        data = f.read()
        data = data.replace('placement', 'screening')
    with open("example.txt", 'w') as f:
        f.write(data)


def creating():
    with open("example.txt", 'w') as f:
        f.write("This is a placement assignment")


if os.path.isfile("example.txt"):
    replacing()
else:
    print("creating file named example.txt with default content")
    creating()
    replacing()
