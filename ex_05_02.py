largest = None
smallest = None
while True:
    num = input('Enter a Number')
    if num == 'done':
        break
        print(num)
    try:
        medium = int(num)
    except:
        print('invalid input')
        continue
    if largest is None:
        largest = medium
    elif medium > largest:
        largest = medium
    if smallest is None:
        smallest = medium
    elif medium < smallest:
        smallest = medium
print('Maximum is', largest)
print('Minimum is', smallest)
