fp = open("file1.txt","r")
fp2 = open("file2.txt","w")

for content in fp:
    fp2.write(content)


fp.close()
fp2.close()
