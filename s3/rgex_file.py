lookup = 'pulumi_aws'

with open('import.txt') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            with open(r"import.txt", 'r+') as fp:
                # read a store all lines into list
                lines = fp.readlines()
                # move file pointer to the beginning of a file
                fp.seek(0)
                # truncate the file
                fp.truncate()
                #print(num)
                # start writing lines except the comment line
                # lines[1:] from line 2 to last line
                fp.writelines(lines[num - 2:])


with open("import.txt") as f:
    with open("import_resource.py", "w") as f1:
        for line in f:
            f1.write(line)
