def alphabetizer(filename):
    file = open(filename, 'r')
    contents = file.read()
    words = contents.split(" ")
    print(sorted(words))

filename = input("Enter a file: ")
alphabetizer(filename)
