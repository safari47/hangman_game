from hangman import display_hangman
from random_list import *

def play(word):
    print(' Давайте играть в угадайку слов! ')
    word_completion = ['_' for i in range(len(word))]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print(' Рандом загадал  вам какое-то словечко: ', *word_completion)

    while tries>0:
        print(display_hangman(tries))
        abc=input('Введите букву или слово ')
        while is_valid(abc)==False:
            abc=input('Ошибочка, ты ввел что-то не правильно ')
        if len(abc)==1:                                          ##Игра в 1 букву
            if abc in guessed_letters:
                print('Вы уже вводили эту букву')
                continue
            for i in range(len(word)):
                if abc==word[i]:
                    word_completion[i]=abc
            if '_' not in word_completion:
                guessed=True
                break
            else:
                print('Словечко теперь выглядит вот так ', *word_completion )
                tries-=1
                guessed_letters.append(abc)   
        if len(abc)>1:
            if abc in guessed_words:
                print('Вы уже вводили это слово')
                continue
            if abc==word:
                guessed=True
                break
            else:
                print('Ваше слово совсем не совпадает с загаданным')
                tries-=1
                guessed_words.append(abc)

        
    print(display_hangman(tries))
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')
  

again = 'д'

while again.lower() == 'д':
    word = random_work()
    play(word)
    again = input('Играем еще раз? (д = да, н = нет):')
