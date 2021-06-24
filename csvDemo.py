import csv

# read data from csv file
with open('utilities/loanData.csv') as csvFile:
    # # create reader object
    csvReader = csv.reader(csvFile, delimiter=',')
    # # display csvReader object
    # print(csvReader)
    # # display list of csv file content
    # print(list(csvReader))

    # create two empty lists: names, stats
    names = []
    stats = []
    # loop to append data to the two lists
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

# display two lists
print("Names: ", names)
print("Status:", stats)

# find index of each name and display status of that name by index
index = names.index('Tom')
loanStatus = stats[index]
print("Tom's loan status: ", loanStatus)

# write data to csv file
with open('utilities/loanData.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "Approved"])
