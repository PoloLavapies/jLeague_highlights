w = open('files.txt', 'w')
for line in open('files_tmp.txt'):
    w.write("file '{0}'\n".format(line[:-1]))