import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row['first_name'],': ',row['phone_number'])
        line_count +=1

    #for row format we can write
    #csv_reader = csv.DictReader(csv_file)
    # line_count == 0:
    #   line_count += 1
    # else:
    #   print(row[1])
    #   line_count +=1
