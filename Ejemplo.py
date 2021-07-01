import math
from typing import Sequence
print (math.sin(math.pi/2))

def sin(x):
    if 2 * x == pi:
        return 0.9999999
    else:
        return None
pi = 3.14

print(sin(pi/2))
print (math.sin(math.pi/2))

for name in dir(math):
    print (name, end="\t")


from math import sin, cos, tan, pi, ceil, floor, hypot, sqrt

x = 1.4
y = 2.6
ad = 90

print (pi)
print (sin(pi/2))
print (cos(ad))
print (tan(ad))
print (floor(x), floor (y))
print (ceil(x), ceil (y))
print (hypot(x, y))
print (sqrt(144))


from random import random, seed

for i in range(5):
    print (random())

from random import randrange, randint

print (randrange(4), end='')
print (randrange(5, 10), end='')
print (randrange(0, 3, 2), end='')

from platform import machine
print (machine())

from platform import system
print (system())

from platform import machine
print (machine())

from platform import processor
print (processor())

from platform import version
print (version())

from platform import python_implementation, python_version_tuple

print (python_implementation())
print (python_version_tuple())   

palabra = 'por'
print (len(palabra))

vacio = ''
print (len(vacio))

multiLinea = '''Linea #1
Linea #2'''
print (len(multiLinea))


str1 = 'a'
str2 = 'b'

print (str1+str2)
print (str2+str1)
print (5 * 'a')
print ('b' * 4)

ch1= '@'
ch2= ' '
ch3= '[' 

print (ord(ch1))
print (ord(ch2))
print (ord(ch3))

print (chr(64))
print (chr(945))

alpha = "abcdefg"

print (alpha[1:3])
print (alpha[3:])
print (alpha[:3])
print (alpha[::2])
print (alpha[::3])
print (alpha[1::2])

alphabet = "abcdefghijklmnopqrstuvwxyz"

print ("f" in alphabet)
print ("F" in alphabet)
print ("1" in alphabet)
print ("ghi" in alphabet)
print ("Xyz" in alphabet)

alfabeto = "bcdefghijklmnopqrstuvwxy"
alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print (alfabeto)
print (min("aAbByYzZ"))

t = [0, 1, 2]
print (min(t))

print (max("aAbByYzZ"))

t = 'Los Caballeros Que Dicen "¡Ni!"'
print ('[' + max(t) + ']')

t = [0, 1, 2]
print (max(t))

print ("aAbByYzZ".index("b"))
print ("aAbByYzZ".index("Z"))
print ("aAbByYzZ".index("A"))

print (list ("abcabc"))
print ("abcabc".count("b"))
print ("abcabc".count("d"))
print ('aBcD'.capitalize())

print ('['+'Beta'.center(2)+']')
print ('['+'Beta'.center(8)+']')
print ('['+'Beta'.center(12)+']')
print ('['+'gamma'.center(20, '*')+']')

#endswith= evalua si termina en ese caracter especificado

t = "zeta"
print (t.endswith("a"))
print (t.endswith("A"))
print (t.endswith("et"))
print (t.endswith("eta"))

#starswith= evalua si termina en ese caracter especificado

print ("omega".startswith("meg"))
print ("omega".startswith("om"))

t = 'alfabeto'
print (t.find('eto'))
print (t.find('et'))
print (t.find('fa'))
print (t.find('a'))

#isalnum: verifica números o letras

print ('lambda30'.isalnum())
print ('lambda'.isalnum())
print ('30'.isalnum())
print ('@'.isalnum())
print ('lambda_30'.isalnum())
print (''.isalnum())

print ("Mooo".isalpha())
print ("Mu40".isalpha())

print ('2018'.isdigit())
print ('Año2019'.isdigit())

print ("Mooo".islower())
print ("mooo".islower())
print ("______")

print (' \n '.isspace())
print (" ".isspace())
print ('moo moo moo'.isspace())
print ("____________")

print ("Moooo".isupper())
print ("moooo".isupper())
print ("MOOOO".isupper())

print ("SiGmA=60".lower())

print ("www.netacad.com".replace ("netacad.com", "pythoninstitute.org"))
print ("This is it!".replace("is", "are"))
print ("Apple juice".replace ("juice", ""))

print ("Diana       Ladino   Suos".split())

#swapcase = crea nueva cadena y cambia min y mayus (inversa)
#title = primera letra mayus
#upperr = todo mayus

print ("Yo sé que no se nada.".swapcase())
print()
print ("Yo sé que no se nada. Parte 1".title())
print()
print ("Yo sé que no se nada. Parte 2".upper()) 

#método sort= ordena alfabeticamente

secondGreek = ['omega', 'alfa', 'pi', 'gama']
print (secondGreek)

secondGreek.sort()
print (secondGreek)
