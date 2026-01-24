bill_ammont = float(input("enter the bill"))
paid = float(input("enter the price"))
def dueammount(bill_ammont,paid):
    return bill_ammont - paid
due = dueammount(bill_ammont,paid)
print("the price is ",due)