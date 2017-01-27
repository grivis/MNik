text = 'Бородинское сражение произошло 7 сентября 1812'
#counters = ("1","2","3","4","5","6","7","8","9","0")
counters = set('0123456789')

i =0
for letter in text:
    try:
        i += int(letter)
    except ValueError:
        continue


print(i)