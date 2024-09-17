word_array = []
word_len = []
def find_longest_word():
    with open("my_text.txt") as fp:
        for each_word in fp:
            
            word_array.append(each_word)
    for word in word_array:
       word_len.append(len(word))
    # print(word_len)
    max_len = len(word_len)
    for word in word_array:
      if len(word)==max_len: 
        print(f"Longest word: {word}, Length: {len(word)}")
find_longest_word()
