# -*- coding: utf-8 -*-
'''
Created on 15 de jul de 2017

@author: henrique

    "Quando lemos uma palavra conhecida, nosso cérebro está na verdade vendo-a como uma
    imagem única e não um grupo de letras que precisam ser processadas e traduzidas em
    sequência" O GLOBO, 25/03/2015

'''
from random import shuffle

message = 'Todos nós desejamos ajudar uns aos outros. Os seres humanos são assim. Desejamos
            viver para a felicidade do próximo - não para o seu infortúnio. Por que havemos de
            odiar ou desprezar uns aos outros? Neste mundo há espaço para todos.'

def convert(text):
    message_new = ''
    text = text.split(' ')
    for word in text:
        if len(word) > 3:
            word = shuffle_word(word)
        message_new += word + ' '
    return message_new

def shuffle_word(word):
    fix = word
    word = list(word)
    meio = word[1:-1]
    shuffle(meio)
    meio = ''.join(meio)
    return fix[0] + meio + fix[-1]

new = convert(message)
print(new)
