# desafio 20
import random
print(f'\033[4;30;41m{"Desafio 20":=^30}\033[m')
a1 = input('Digite o nome do aluno:')
a2 = input('Digite o nome de outro aluno:')
a3 = input('Digite o nome de outro aluno:')
a4 = input('Digite o nome do ultimo aluno:')
ordem = [a1, a2, a3, a4]
random.shuffle(ordem)
print(f'a ordem de presentação é :\n\033[4;44m{ordem}\033[m')

# desafio 21
print('{:=^30}'.format('Desafio 21'))
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
