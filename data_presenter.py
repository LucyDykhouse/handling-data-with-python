# Problem 2
open_file = open("CupcakeInvoices.csv")

# Problem 3
for row in open_file:
    print(row)

# Problem 4
open_file.seek(0)
for row in open_file:
    items = row.split(",")
    print(items[2])
    
# Problem 5
open_file.seek(0)
for row in open_file:
    items = row.split(",")
    totals = int(items[3]) * round(float(items[4]), 2)
    print("${:0.2f}".format(totals))
    
# Problem 6
open_file.seek(0)

sum = 0

for row in open_file:
    items = row.split(",")
    totals = int(items[3]) * float(items[4])
    sum += totals
    
print("The sum of all invoice totals is ${:0.2f}".format(sum))

# Problem 7
open_file.close()
    