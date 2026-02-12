pravilnye_otveti = (1, 2, 3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 3, 2, 1, 2, 1, 2, 1)
otvet = []
for i in range(len(pravilnye_otveti)):
    otvet.append(int(input("Введите ответ ")))
if otvet == list(pravilnye_otveti):
    print("Экзамен сдан")
else:
    print("Экзамен провален")








































































