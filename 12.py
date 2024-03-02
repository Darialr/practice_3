att = float(input('ATT: '))
com = float(input('COM: '))
yd = float(input('YD: '))
td = float(input('TD: '))
intrc = float(input('INT: '))
per = (((com/att - 0.3)*5 + (yd/att - 3)*0.25 + (td/att)*20 + 2.375 - (intrc/att)*25)/6)*100
print(per)
