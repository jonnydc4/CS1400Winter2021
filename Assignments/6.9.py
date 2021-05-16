def average(x, y):
    ave = x / y
    print(f'The average is {ave}')

def convert_to_int(text_file):
    file = open(text_file,'r')
    count = 0
    sum = 0

    for line in file:
        x = 0
        line.rstrip('\n')
        str_numbers = line.split(" ")

        for number in str_numbers:
            number = float(str_numbers[x])
            x += 1
            count += 1
            sum += number
    average(sum, count)
    file.close()

# convert_to_int('6.9number.txt')
file = input("Enter the input file name:")
convert_to_int(file)
