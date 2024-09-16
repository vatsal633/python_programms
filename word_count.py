occurencesce_of_words = dict()
total_words = 0

with open("quots.txt") as file_handler:
    for each_row in file_handler:
        word = each_row.rstrip().split()
        total_words += len(word) 
        for each_word in words:
            occurrence_of_words[each_word] = occurrence_of_words.get(each_word, 0) + 1
    print("The number of times each word appears in a sentence is")
    print(occurencesce_of_words)
    print(f"Total number of words in the file are {total_words}")
