def wordCounter(filename):
    with open(filename) as f:
        list = f.read().split(" ")
        dic = dict()
        for line in sorted(list):
            words = line.split()
            for word in words:
                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1
    print(dic)

file = input("Enter a file: ")
wordCounter(file)
