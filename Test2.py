text = 'Бородинское сражение произошло 7 сентября 1812'

dict1 = {"а":0,"б":0,"в":0,"г":0,"д":0,"е":0,"ё":0,"ж":0,"з":0,"и":0,"к":0,"л":0,"м":0,"н":0,
         "о":0,"п":0,"р":0,"с":0,"т":0,"у":0,"ф":0,"х":0,"ц":0,"ш":0,"щ":0,"ъ":0,"ы":0,"ь":0,"э":0,"ю":0,"я":0}

for key in dict1.keys():
    dict1[key] = text.count(key)

for key, value in dict1.items():
    if value != 0:
        print(key, ':', value)

# for i in text:
#    dict1[i]+=1
#
# j = len(text)
# while i in range(j):
#     print(dict1)