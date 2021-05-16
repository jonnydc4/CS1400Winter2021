# Put your code here
def isSorted(list):
    #if list is sorted print true
    list_length = len(list)
    if list_length <= 1:
        return True
    else:
        index = 2
        while index < list_length:
            if list[index] < list[index - 1]:
                return False
            index += 1
        return True

# A main for testing your code
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst), lyst)
    lyst[9] = 3
    print(isSorted(lyst), lyst[8], lyst[9])

main()