
def computepay(float(hours) * float(pay))
    if float(hours) < 40:
        return 'pay'
    elif float(hours) > 40:
        return '498.75'
print(computepay(hours))
