import random

from processing import pr
alphabet = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}
def sh(data):
    with open('key.txt','a+') as file:
        num = []
        for value in range(len(data)):
            num.append(random.randint(0,10))
        for value in num:
            for j in alphabet.keys():
                if value == alphabet[j]:
                    file.write(j)
                    continue
    with open('key.txt', 'r+') as file:
        key = file.readline()
        for i,j in zip(data, key):
            n1 = 0
            n2 = 0
            for value in alphabet.keys():
                if i == value:
                    n1 = alphabet[value]
                if j == value:
                    n2 = alphabet[value]
            answer = n1^n2
            with open('ciphertext.txt', 'a+') as chiphertext:
                for value in alphabet.keys():
                    if alphabet[value] == answer:
                        chiphertext.write(value)


def un_sh(key):
    with open('ciphertext.txt', 'r+') as file:
        data = file.readline()
        for i,j in zip(data, key):
            n1 = 0
            n2 = 0
            for value in alphabet.keys():
                if value == i:
                    n1 = alphabet[value]
                if value == j:
                    n2 = alphabet[value]
            answer = n1^n2
            with open('answer_text.txt', 'a+') as ttt:
                for value in alphabet.keys():
                    if alphabet[value] == answer:
                        ttt.write(value)

question = input('1 - зашифровать текст\n2 - расшифровать текст\n')
if question == '1':
    with open('text.txt', 'r+') as file:
        text = file.read()
        if len(text) == 0:
            print('Пустой файл!')
            exit()
        new_text = pr(text)
        sh(new_text)
elif question == '2':
    with open('ciphertext.txt', 'r+') as file:
        text = file.read()
        if len(text) == 0:
            print('Пустой файл!')
            exit()
        with open('key.txt', 'r+') as file_key:
            text_key = file_key.read()
            if len(text_key) == 0:
                print('Нет ключа!')
                exit()
            if len(text_key) != len(text):
                print('Ключ не соответствует необходимым требованиям!')
                exit()
            new_text = pr(text)
            un_sh(text_key)