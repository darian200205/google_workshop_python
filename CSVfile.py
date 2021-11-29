import csv

with open("testData.csv", "w") as csv_file:

    cars = [
        ['Brand', 'Model', 'An', 'CP'],
        ['Opel', 'Astra', 2002, 101],
        ['Mazda', 6, 2012, 120],
        ['Ford', 'Focus', 2009, 105]
    ]

    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerows([car for car in cars])




with open("dataFile.txt", "r") as file:
    my_data = []
    for line in file:
        my_data.append(line[:-1].split(","))

        #print(my_data)
    #my_list = my_data.split(",")
    #print(my_data[0])

