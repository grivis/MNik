text = 'В конце ноября, в оттепель, часов в девять утра, поезд Петербургско-Варшавской железной дороги \
на всех парах подходил к Петербургу. Было так сыро и туманно, что насилу рассвело; в десяти шагах, вправо \
и влево от дороги, трудно было разглядеть хоть что-нибудь из окон вагона. Из пассажиров были и \
возвращавшиеся из-за границы; но более были наполнены отделения для третьего класса, \
и всё людом мелким и деловым, не из очень далека. Все, как водится, устали, у всех отяжелели за ночь глаза, \
все назяблись, все лица были бледно-желтые, под цвет тумана.'

dict1 = {}
textl = text.lower()
words = textl.split()

print(words)

for word in words:
    if dict1.get(word) == None and word.isalpha():
        dict1[word] = words.count(word)


# for word in sorted(dict1.keys(), reverse=True):
#     print(word, ':', dict1[word])

wordtuples = []
for key, value in dict1.items():
    wordtuples.append((value, key))

for wt in sorted(wordtuples, reverse=True):
    print(wt[1], ' : ', wt[0])
