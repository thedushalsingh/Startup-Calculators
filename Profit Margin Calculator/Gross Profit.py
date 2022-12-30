# Gross Profit Formula = Revenue – Cost of goods sold
Revenue = input("Enter Your Revenue = ")
COGS = input("Please,Enter the amount of Cost of Goods Sold = ")
Gross_Profit = int(Revenue) - int(COGS)

if Revenue > COGS :
    print("The Gross Profit will be", Gross_Profit)

else :
    print("Negative Margin =",Gross_Profit)
