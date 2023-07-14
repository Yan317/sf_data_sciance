'''Игра угадай число'''

from cgi import print_directory
import numpy as np

number = np.random.randint(1, 101)      # загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input("Угадайте число от 1 до 100: "))
    
    if predict_number > number:
        print('Число должно быть меньше!')
        
    elif predict_number < number:
        print('Число должно быть больше!')
    
    else:
        print(f'Вы угадали число! Это чило = {number}, за {count} попыток')
        break # конец игры, выход из цикла