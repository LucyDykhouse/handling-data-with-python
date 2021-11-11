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


# Part 3 - to run in replit
import matplotlib.pyplot as plt

open_file.seek(0)

choc_amt = 0
van_amt = 0
str_amt = 0

for row in open_file:
    items = row.split(",")
    if items[2] == "Chocolate":
        choc_amt += int(items[2])
    elif items[2] == "Vanilla":
        van_amt += int(items[2])
    else:
        str_amt += int(items[2])

cupcake_types = ["Chocolate", "Vanilla", "Strawberry"]
type_quantities = [choc_amt, van_amt, str_amt]

plt.bar(cupcake_types, type_quantities)
plt.xlabel("Cupcake Type")
plt.ylabel("Amount purchased")
plt.title("Cupcake Sales Vs Type")
plt.show()