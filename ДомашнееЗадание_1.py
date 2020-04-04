#Задание 1

Year = int (input ("Введите год  "))
Year >= 0
if Year <= 0:
    raise SystemExit 
else:
    Year

Month = int (input ("Введите месяц  "))
if Month >= 13:
     raise SystemExit 
elif Month <= 0:
    raise SystemExit 
else:
    Month

Day = int (input ("Введите день  "))
if Day < 1:
     raise SystemExit 
elif Day > 31:
     raise SystemExit 
elif (Month == 4 or Month == 6 or Month == 9 or Month == 11) and Day > 30:
    raise SystemExit
elif Month == 2 and (Year % 4 == 0 and Year % 400 == 0) and Day > 29:
      raise SystemExit 
elif Month == 2 and (Year % 4 and Year % 100 == 0 ) and Day > 28:
      raise SystemExit 
else:
   Day


if (Month == 4 or Month == 6 or Month == 9 or Month == 11) and (Day + 1) == 31:
  print (1, (Month + 1), Year)
elif Month == 12 and Day == 31:
    print (1, 1, (Year + 1))
elif (Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12) and (Day + 1) == 32:
  print (1, (Month + 1), Year)
elif Month == 2 and (Day + 1) == 30 and (Year % 4 and Yaer % 400 == 0):
    print (1, (Month + 1), Year)
elif Month == 2 and (Year % 4 == 0 and Year % 100 == 0) and (Day + 1) == 29:
    print (1, (Month + 1), Year)
else:
    print ((Day + 1), Month, Year)



# Задание 2

print ("Введите коэффиценты для уравнения (ax^ + bx + c = 0): ")
a = float (input ("a = "))
b = float (input ("b =  "))
c = float (input ("c =  "))

discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))