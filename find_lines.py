
def find_line():
    count = 0
    with open("my_text.txt") as fp:
        for i in fp:
            for temp_i in i:
                if(temp_i=="."):
                    count+=1
    print("threr are total",count,"lines")
find_line()
