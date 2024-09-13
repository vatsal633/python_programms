with open("sample.py") as file_handler:
    for each_row in file_handler:
        each_row=each_row.replace("#","")
        print("file content\n")
        print(each_row)
