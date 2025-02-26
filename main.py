#from graphic_arts.start_game_banner import run_screensaver
from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} урон противнику равен {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} урон противнику равен {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} урон противнику равен {5 + randint(-3, -1)}')

    return char_class


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')

    return char_class


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} применил «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил «Защита {10 + 30}»')

    return f'{char_name} не применил специальное умение'


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей.')
    print('Потренируйся управлять своими навыками.')
    print('Введи команду: attack, defence, '
          'speаорпапдпдгфдгдавнквгевгевкллрдрдлрдфвпcial')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))

    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи имя персонажа: Воитель — warrior, '
                           'Маг — mage,' ' Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — воин ближнего боя. Сильный и отважный.')
        if char_class == 'mage':
            print('Маг — воин дальнего боя с высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — заклинатель. Силы из природы, веры и духов.')
        approve_choice = (input('(Y) - подтвердить выбор, '
                                '' 'любая другая кнопка, '
                                '- выбор другого ').lower())
    return char_class


if __name__ == '__main__':

    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
