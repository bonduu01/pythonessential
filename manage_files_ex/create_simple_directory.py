from os import mkdir, listdir, makedirs, chdir, getcwd, rmdir, removedirs

mkdir("my_first_directory")
print(listdir())

'''Make directories and change to current directory'''
makedirs("my_first_directory/second_directory")
chdir("my_first_directory/second_directory")
print(listdir())

'''Returns pwd'''
print(getcwd())

'''Remove Directory'''
rmdir("my_first_directory")
print(listdir())

removedirs('my_first_directory/second_directory')
print(listdir())
