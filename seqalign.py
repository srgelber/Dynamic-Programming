##Simon Gelber - CSC359 Asgn 3
# Identify Best Alignment using DP
import sys

def align(string1, string2, strtable1,strtable2, scoretable, matrix):
    #initial population of base cases
    row = 0
    col = 0
    while col < len(string1):
        if col == 0:
            scoretable[row][col] = matrix['-'][string1[col]]
        else:
            scoretable[row][col] = matrix['-'][string1[col]] + scoretable[row][col-1]
        if col <= 1:
            strtable1[row][col] = string1[col]
            strtable2[row][col] = string2[row]
        else:
            strtable1[row][col] = strtable1[row][col - 1] + string1[col]
            strtable2[row][col] = strtable2[row][col - 1] + string2[row]
        col += 1
    col = 0
    while row < len(string2):
        if row == 0:
            scoretable[row][col] = matrix[string2[row]]['-']
        else:
            scoretable[row][col] = matrix[string2[row]]['-'] + scoretable[row-1][col]
        if row <= 1:
            strtable1[row][col] = string1[col]
            strtable2[row][col] = string2[row]
        else:
            strtable1[row][col] = strtable1[row - 1][col] + string1[col]
            strtable2[row][col] = strtable2[row - 1][col] + string2[row]
        row += 1
    row = 0
    strtable1[0][0] = ''
    strtable2[0][0] = ''
    col = 1
    row = 1
    while row < len(string2):
        while col < len(string1):
            option1 = scoretable[row][col - 1] + matrix['-'][string1[col]]
            option2 = scoretable[row - 1][col] + matrix[string2[row]]['-']
            option3 = scoretable[row - 1][col - 1] + matrix[string2[row]][string1[col]]
            if (option1 >= option2) and (option1 >= option3):
                scoretable[row][col] = option1
                strtable1[row][col] = strtable1[row][col - 1] + string1[col]
                strtable2[row][col] = strtable2[row][col - 1] + '-'
            elif (option2 >= option1) and (option2 >= option3):
                scoretable[row][col] = option2
                strtable1[row][col] = strtable1[row - 1][col] + '-'
                strtable2[row][col] = strtable2[row - 1][col] + string2[row]
            elif (option3 >= option1) and (option3 >= option2):
                scoretable[row][col] = option3
                strtable1[row][col] = strtable1[row - 1][col - 1] + string1[col]
                strtable2[row][col] = strtable2[row - 1][col - 1] + string2[row]
            col += 1
        col = 1
        row += 1


def main(argv):
    matrix = {
        'A' : {
            'A' : 0,
            'C' : 0,
            'G' : 0,
            'T' : 0,
            '-' : 0
        },
        'C': {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            '-': 0
        },
        'G': {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            '-': 0
        },
        'T': {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            '-': 0
        },
        '-': {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            '-': 0
        },
    }
    file = open(argv[1],"r")
    line = file.readline()
    string1 = line.strip()
    line = file.readline()
    string2 = line.strip()
    line = file.readline()
    for row in matrix:
        line = file.readline()
        line = line.strip("ACGT- ")
        scores = line.split()
        index = 0
        for entry in matrix[row]:
            matrix[row][entry] = int(scores[index])
            index += 1
    strtable1 = [["" for i in range(len(string1) + 1)] for j in range(len(string2) + 1)]
    strtable2 = [["" for i in range(len(string1) + 1)] for j in range(len(string2) + 1)]
    scoretable = [[0 for i in range(len(string1) + 1)] for j in range(len(string2) + 1)]
    string1 = list(string1)
    string1.insert(0, '-')
    string2 = list(string2)
    string2.insert(0, '-')
    align(string1, string2, strtable1,strtable2, scoretable, matrix)

    finalstring1 = list(strtable1[len(string2)-1][len(string1) - 1])

    finalstring2 = list(strtable2[len(string2) - 1][len(string1) - 1])

    print("x:", end='')
    for i in finalstring1:
        print(' ' + i, end='')
    print()

    print("y:", end='')
    for i in finalstring2:
        print(' ' + i, end='')
    print()

    print("Score: %d" % scoretable[len(string2) - 1][len(string1) - 1])
    file.close()



if __name__ == "__main__":
    main(sys.argv)