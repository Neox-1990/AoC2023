import re
import os

example = open(os.path.dirname(os.path.realpath(__file__))+"/example.txt", "r")
example_input = example.readlines()
example.close()

input1 = open(os.path.dirname(os.path.realpath(__file__))+"/input1.txt", "r")
input1_input = input1.readlines()
input1.close()

example2 = open(os.path.dirname(os.path.realpath(__file__))+"/example2.txt", "r")
example2_input = example2.readlines()
example2.close()

#Part 1
print("\n\n======\nPart 1\n")

def decodeLine(s):
    matches = re.findall("\d",s.strip())
    if len(matches) == 1:
        return int(matches[0]+matches[0])
    else:
        return int(matches[0]+matches[-1])

example_input_decoded = map(decodeLine, example_input)
example_input_sum = sum(example_input_decoded)
print("Example solution: {}".format(example_input_sum))

input1_input_decoded = map(decodeLine, input1_input)
input1_input_sum = sum(input1_input_decoded)
print("Input 1 solution: {}".format(input1_input_sum))

#Part 2
print("\n\n======\nPart 2\n")

def decodeLineAdvanced(s):
    s = str(s.strip())
    line = replaceWords(s)
    #print("Pre: {0}\t\t\t\tPost: {1}".format(s,line))
    return decodeLine(line)

def replaceWords(s):
    replaceDict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    while len(re.findall("(one|two|three|four|five|six|seven|eight|nine)", s)) > 0:
        x = re.search("(one|two|three|four|five|six|seven|eight|nine)", s).group()
        s = re.sub(""+x, replaceDict[x], s)
    return s

example2_input_decoded = map(decodeLineAdvanced, example2_input)
example2_input_sum = sum(example2_input_decoded)
print("Example 2 solution: {}".format(example2_input_sum))

input2_input_decoded = map(decodeLineAdvanced, input1_input)
input2_input_sum = sum(input2_input_decoded)
print("Input 2 solution: {}".format(input2_input_sum))