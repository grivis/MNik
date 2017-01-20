## Кто твой отец?
dict = {"Антон":"Павел","Михаил":"Сергей","Александр":"Анатолий"}
name = input("name: ")
#print(dict[name])
if name in dict:
    print(dict[name])
else:
    father = input("Father`s name :")
    dict[name] = father
    print(dict[name])
