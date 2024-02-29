x,y,n = map(int, input('').split())
cent = (y * n) % 100
rub = x*n + ((y*n)//100)
print(f'{rub} руб. {cent} коп.')
