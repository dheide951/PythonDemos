import csv
#with open('ch9.py', 'r') as f:
#    print(f.read())

##with open('ex1.txt', 'w') as f:
##    for i in range(4):
##        userIn = input("type a number: ")
##        f.write(userIn + "\n")

lst = [["Top Gun", "Risky Business", "Minority Report"],
       ["Titanic", "The Revenant", "Inception"],
       ["Training Day", "Man On Fire", "Flight"]]

with open('ex2.csv', 'w') as f:
    w = csv.writer(f, delimiter=",")
    for x in lst:
        w.writerow(x)

with open('ex2.csv', 'r') as f:
    r = csv.reader(f ,delimiter=",")
    for row in r:
        print(", ".join(row))
