# subtracting the cost of goods sold (COGS) from its total revenue and dividing 
# that figure by the total revenue. Multiply that figure by 100 to get a percentage.
# COGS - REVENUE / REVENUE * 100

print("Profit Margin Calculator\n")
Revenue = input("Please, Enter the amount of Total Revenue = ")
COGS = input("Please, Enter the amount of Cost of Goods Sold = ")

PROFIT_MARGIN = int(Revenue)-int(COGS)/int(Revenue)*100
print("The Profit Margin Will be =",PROFIT_MARGIN,"%")

 