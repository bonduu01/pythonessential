from os import strerror

try:
    count = 0
    stream = open("../version.txt", "rt")
    contents = stream.read()
    for content in contents:
        print(content, end='')
        count += 1
    stream.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
