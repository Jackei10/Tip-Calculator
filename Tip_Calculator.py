print("Welcome to the Tip calculator")
bill=float(input("Enter total bill amount\n"))
percent=int(input("how much percent tip you want to add\n"))
buyers=int(input("Enter no. of people who are going to split the bill\n"))
extra= bill* percent/100
Total_Bill=(bill+extra)/buyers
print(f"You have to pay {round(Total_Bill,2)} per person")
