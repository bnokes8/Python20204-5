# Brady Nokes 9/23/20 Cash Register Assignment
numItems = 4
costPerItem = 10.00
taxRate= 0.08

subTotal = costPerItem * numItems
taxAmount = subTotal * taxRate
totalPrice = subTotal + taxAmount

print("SALES RECEIPT")
print("Number of Items: " + str(numItems))
print("Cost per Item      : " ,"$"+ str(costPerItem) )
print("Tax Rate               : " + str(taxRate),)
print("Tax Amount        : " ,"$"+ str(taxAmount))
print("Total Sale Price  : ","$"+ str(totalPrice))

