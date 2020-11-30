import csv
import numpy as np
import itertools

def main():

    with open('input.txt', newline='') as file:
        reads = csv.reader(file, delimiter=',')

        for row in reads:
            evenrow = fix_length(row)
            div = calc_len(evenrow)
            split = np.array_split(evenrow, div)

            for verb, noun in itertools.product(range(99), range(99)):
                fixedRow = fix_row(evenrow, verb, noun)

                for spl in split:
                    processOpCode(spl,fixedRow)
                    if fixedRow[0] == 19690720:
                        print(fixedRow[0])
                        print("Verb: ", verb)
                        print("Noun: ", noun)
def fix_row(array, verb, noun):
    array[1] = verb
    array[2] = noun
    return array

def fix_length(row):
    evenrow = row
    i = 0
    while len(evenrow) % 4 != 0:
        evenrow += row[i]  # keep adding char at alternate indexes
        if i == len(row) - 1:  # if we are at the end of the string, reset
            i = 0
        else:
            i += 1  # else move to next char
    return evenrow

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def calc_len(df):
    length = len(df)/4
    return length.real

def processOpCode(OpCode, array):
    if OpCode[0].astype(np.int) == 1:
        return opcode1(OpCode[1].astype(np.int), OpCode[2].astype(np.int), array, OpCode[3].astype(np.int))
    elif OpCode[0].astype(np.int) == 2:
        return opcode2(OpCode[1].astype(np.int), OpCode[2].astype(np.int), array, OpCode[3].astype(np.int))
    else:
        return array[0]

def opcode1(loc1,loc2, array, outloc):
    array[outloc] = int(array[loc1]) + int(array[loc2])


def opcode2(loc1, loc2, array, outloc):
    val = int(array[loc1]) * int(array[loc2])
    array[outloc] = val


def opcode99():
    return calcStatus()


def calcStatus():
    return input[0]


if __name__== "__main__":
  main()
