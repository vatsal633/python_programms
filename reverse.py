reverse_list =[]

with open("secrete_scosity.txt") as fp:
    for each_row in fp:
        word_list = each_row.rstrip().split(" ")
        for each_word in word_list:
            reverse_list.append((each_word[::-1]))
        print(" ".join(reverse_list))
        reverse_list.clear()
