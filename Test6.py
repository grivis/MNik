## Кто твой отец? Версия 2
dict = {"Антон":{"Father":"Павел","Grandfather":"Иван"},"Михаил":{"Father":"Сергей","Grandfather":"Семён"},\
        "Александр":{"Father":"Анатолий","Grandfather":"Николай"}}
name = input("name: ")
#print(dict[name])
if name in dict:
    print(dict[name]["Father"])
    print(dict[name]["Grandfather"])
else:
    father = input("Father`s name :")
    gf = input("Grandfather name: ")
    dict[name] = {'Father':father, 'Grandfather': gf}
    #print(dict[name])
    print(dict[name]["Father"])
    print(dict[name]["Grandfather"])