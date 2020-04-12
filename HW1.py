days = int (input ("Введите количество дней "))
N, sum_meteo, max = 0, 0, 0

while N != days:
    meteo = int (input ("Введите количество осадков в день "))
    sum_meteo =  sum_meteo + meteo
    if meteo > max:
        max = meteo
    N += 1
print ("Количество дней", days)
print ("Сумма осадков зa период ", sum_meteo)
print ("Cреднее количество осадков ", sum_meteo/days)
print ("Максимальноеколичество осадков ", max)


