budget = 2000.00
print("welcome to your grocery budget checker!")
print(f"Your maximum shopping budget is : Rs.{budget}")

total_cost = float(input("enter the total cost of your items: Rs."))

if total_cost <=budget:
    print("great ! ypu have enough money in your budget.")
else:
    print("warning: you are over budget ! Put some items back.")
