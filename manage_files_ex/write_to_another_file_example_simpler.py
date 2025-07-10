from os import strerror

try:
    stream = open("../newfile.txt", 'wt')
    for ch in range(10):
        stream.write("Page Number: " + str(ch) + "\n")
    stream.close()

except IOError as e:
    print("I/O error", strerror(e.errno))
