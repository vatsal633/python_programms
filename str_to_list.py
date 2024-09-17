new_list = []

with open("my_text.txt") as fp:
    for word in fp:
        li = word.split(" ")
        new_list.append(li)

print(new_list)
print(len(new_list[0]))
