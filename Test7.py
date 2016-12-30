## Дни рождения
months = {'января':(0,12,'январь'), 'февраля':(0,11,'февраль'),'марта':(0,10,'март'),'апреля':(0,9,'апрель'),
          'мая': (0, 8, 'май'),'июня':(0,7,'июнь'),'июля':(0,6,'июль'),'августа':(0,5,'август'),
          'сентября': (0, 4, 'сентябрь'),'октября':(0,3,'октябрь'),'ноября':(0,2,'ноябрь'),'декабря':(0,1,'декабрь'),}
# children = int(input())
# for i in range(children):
line = ' '
while len(line)>0:
    line = input('> ')
    if len(line) >0:
        month = line.split()[-1]
        f, w, n = months[month]
        months[month] = (f+1, w, n)


for bd in sorted(months.values(), reverse=True):
    if bd[0] > 0:
        print(bd[2], bd[0])

