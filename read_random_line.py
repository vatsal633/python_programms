import random
word_list = []
with open("demo3.txt") as fp:
    count=0
    for line in fp:
        word_list.append(line)
        for word in line:
            if word=="\n":
                count+=1
    num = int(random.random() * count+1)
    print(num)
    print(word_list[num])
