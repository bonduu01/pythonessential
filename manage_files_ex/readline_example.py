from os import strerror

try:
    character_count = line_count = 0
    stream = open("../version.txt", "rt")
    read_line = stream.readline()

    while read_line != '':
        line_count += 1
        for character in read_line:
            print(character, end='')
            character_count += 1
        read_line = stream.readline()
    stream.close()
    print("\n\nCharacters in file: ", character_count)
    print("Lines in file: ", line_count)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
