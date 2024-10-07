from random import randint


number = randint(1, 100)
welcome_text = 'Угадайте число от 1 до 100'

print(welcome_text)

def main():
    while True:
        guess = int(input('Введите число: '))
        
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        
        if guess > number:
            print('Ваше число больше того, что загадано.')
        
        if guess == number:
            break

    print('Отличная интуиция! Вы угадали число :)')
    
main()
