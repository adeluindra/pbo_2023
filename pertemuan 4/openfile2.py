# opean a file
file1 = open("rill.txt", "r")
teks="Latihan Python\n"

file2 = open("rill.txt", "a")
file2.write(teks)
file2.close()

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()