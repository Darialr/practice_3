time = int(input('Введите количество секунд: '))
hour = time // 3600
mnt = (time % 3600) // 60
sec = (time % 3600) % 60
print(f'Текущее время: {hour}ч. {mnt}мин. {sec}сек.')
