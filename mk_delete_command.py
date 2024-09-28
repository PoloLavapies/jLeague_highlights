w = open("file_delete.sh", "w")
for line in open("files_to_delete.txt"):
    w.write('rm "{0}"\n'.format(line[:-1]))