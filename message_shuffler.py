# -*- coding: utf-8 -*-
'''
Created on 15 de jul de 2017

@author: henrique
'''
from random import shuffle

message = 'Você sabia que o cérebro humano consegue ver palavras agrupadas como uma imagem, e não somente por letras ?'

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
