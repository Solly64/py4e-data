hours = input("enter hours")
rate = input("enter rate")
pay = float(hours) * float(rate)
if float(hours) < 40:
    print(pay)
if float(hours) > 40:
    overtime = input("enter overtime")
    overpay = input("enter overpay")
    overtimepay = float(pay) + float(overtime) * float(rate) + float(overpay)
print(overtimepay)
