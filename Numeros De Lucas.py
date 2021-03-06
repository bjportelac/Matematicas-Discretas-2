# -*- coding: utf-8 -*-
"""Punto 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oG8iomg5eqv361Golb8BkGLV7dl6DaVq

**6.** Los números de Lucas están relacionado con los números de Fibonacci, y están definidos por la siguiente secuencia $L_{n+2} = L_{n+1} + L_{n}$, $L_0=2$, $L_1=1$. Escriba un programa que imprima la siguiente información. El $18-th$ número de Lucas, el número de Lucas más cercano a $1000$, y el primer número de Lucas más grande que $100$.
"""

import math
def NLbase(n): 
    #Casos base
	if n == 0: 
		return 2
	if n == 1: 
		return 1  
    # recurrencia
	return NLbase(n - 1) + NLbase(n - 2)  

print("El 18º Nº de Lucas es",NLbase(18))
a, b, c = 2, 1, 3
while c < 1000:
	a, b, c = b, c, b+c
print("El número de Lucas más cercano a 1000 es:",c if c-1000<1000-b else b)

k = 0
while NLbase(k) <= 100:
	k+=1
print("El primer numero de lucas mayor a 100 es:",NLbase(k))

