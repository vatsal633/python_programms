word_list=[]
def count_word(filename):
    count=1
    with open(filename) as fp:
        data = fp.read()
        for i in data:
            if i==" ":
                count+=1
    print(count)

fname = input("enter the file name")
count_word(fname)
