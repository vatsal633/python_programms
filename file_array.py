array = []

with open("my_text.txt") as fp:
    for line in fp:
        array.append(line)
    print(array)

print(len(array[3]))
