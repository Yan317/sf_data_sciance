'''Игра угадай число.
Компьютер сам угадывает число'''

import numpy as np

def random_predict(number:int=1) -> int:
    '''Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1
        
    Returns:
        int: Число попыток
    '''
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предпологаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def score_game(def_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадает наш алгоритм

    Args:
        def_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список числе
    
    for number in random_array:
        count_ls.append(def_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


def optimal_predict(number:int=1) -> int:
    '''Угадываем число за минимальное количество поыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1
        
    Returns:
        int: Число попыток
    '''
    
    count = 0   # обнуляем счётчик попыток
    min_number = 1  # минамально число для угадывания
    max_number = 101  # максимальное число для угадывания (!!! нужно больше 100 для возможности выбрать 100 при делении между min и max)
    
    while True:
        count += 1
        if min_number != max_number:    # если диапозон для угадывания более одного числа
            predict_number = min_number + (max_number-min_number)//2    # всегда для проверки выбираем число посередине
            #print(predict_number)
            if predict_number < number:
                min_number = predict_number
            elif predict_number > number:
                max_number = predict_number
            else:
                break   # если не больше и не меньше, значит угадали => вызожим из цикла
    return(count)
    

# RUN
if __name__ == '__name__':
    score_game(optimal_predict)