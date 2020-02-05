def main():
    userFileName = "Script.csv"

    fileToReadFrom = open(userFileName, "r")

    line = fileToReadFrom.readline()

    # part 1: print name, FavoriteFridge1
    while line != "":
        fields = line.split(',')
        print(fields[0] + "," + fields[1])
        line = fileToReadFrom.readline()

    # part 2: print item totals for customers
    namelist = "Jill,Candice,Alycia"
    names = namelist.split(',')
    index = 0
    while index < len(names):
        total = 0
        fileToReadFrom.seek(0)
        line = fileToReadFrom.readline()
        while line != "":
            fields = line.split(',')
            if names[index] == fields[0]:
                if fields[3] != "":
                    total = total + float(fields[3])
                print(fields[0] + "," + fields[2] + "," + fields[3])
            line = fileToReadFrom.readline()
        print(total)
        index = index + 1

    print ()


main()