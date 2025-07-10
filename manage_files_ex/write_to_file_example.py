from os import strerror

try:
    stream = open("../test_write_file.txt", 'wt')
    for i in range(10):
        s = "line #" + str(i + 1) + "\n"
        for ch in s:
            stream.write(ch)
    stream.close()
except IOError as e:
    print("I/O Exception error", strerror(e.errno))
