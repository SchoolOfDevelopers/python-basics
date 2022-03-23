# open file in write mode
# f = open('data.txt', 'w')
# f.write("more New content for the file. It should not overwrite the old content")
# f.close()
# print("File has been saved.")
#
# f = open('data.txt', 'r')
# print(f.read())
# f.close()

f = open('data.bin', 'wb')
f.write(bytes("more New content for the file. It should not overwrite the old content", 'utf-16'))
f.close()
print("File has been saved.")

f = open('data.txt', 'rb')
print(f.read())
f.close()
