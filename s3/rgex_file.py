lookup = "import pulumi_aws as aws\n"


file1 = open("import.txt",'r')
file1_lines = file1.readlines()

for i in range(len(file1_lines)):

    if file1_lines[i] == lookup:
        print('s')
        num = i+1
        with open(r"import.txt", 'r+') as fp:
            # read a store all lines into list
            lines = fp.readlines()
            # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()
            # print(num)
            # start writing lines except the comment line
            # lines[1:] from line 2 to last line
            fp.writelines(lines[num - 2:])


with open("import.txt") as f:
    with open("import_resource.py", "w") as f1:
        for line in f:
            f1.write(line)
