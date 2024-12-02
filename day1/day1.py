
import re
import string

# pt1
with open("./day1.txt") as f:
    num = 0
    for line in f:
        first = ""
        last = ""
        for char in line:
            if char.isnumeric():
                first = char
                break;
        for char in reversed(list(line)):
            if char.isnumeric():
                last = char
                break;
            
        num += int(first + last)
        
    print(num)

word_numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

word_numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

numbers = [num in range(0, 10)]

def findList(string, word_list: list, reversed: bool) -> str:
    string = str(string)
    winning_target = ""
    index = len(string)
    for item in word_list:
        if reversed:
            cur = string.find(item[::-1])
        else:
            cur = string.find(item)
        
        if cur < index and cur != -1:
            winning_target = item
            index = cur
    if (len(winning_target) > 1):
        return str(word_list.index(winning_target)+1)
    return winning_target

with open("./day1.txt") as f:
    sum = 0
    for line in f:
        line = line[:-1]
        first = findList(line, word_numbers, False)
        last = findList(line[::-1], word_numbers, True)
        
        sum += int(first + last)
        
    print(sum)