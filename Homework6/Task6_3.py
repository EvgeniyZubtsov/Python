import os

filedir = input("Введите путь директории: ")
for file in os.listdir(filedir):
    if file.endswith(".dat"):
        print(os.path.join(filedir, file))
        f = open(file)
        for line in f:
            print(line)