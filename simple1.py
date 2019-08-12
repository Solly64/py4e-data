while True:
    cost = input("Cost of meal:")
    tax = input("Tax Rate:")
    tip = input("Tip? Yes/No:")

    if  tip == 'yes':
        percent = input("Tip Percentage:")
        paywithtip =  float(cost)* float(tax) * float(percent)
        print("Pay:", paywithtip)
    if tip == 'no':
        paynotip = float(cost) * float(tax)

print(paynotip)
