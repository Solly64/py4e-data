text = "X-DSPAM-Confidence:    0.8475";
numbers = text.find(' ')
decibel = text.find('5', numbers)
floater = text[numbers + 1 : decibel + 1]
floating = floater.strip()
print(floating)
