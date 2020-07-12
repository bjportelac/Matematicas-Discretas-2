#solicitud de entradas para la codificacion
print("Ingrese el codigo a enviar:")
m=int(input())

print("Ingrese el numero primo P:")
p=int(input())
print("Ingrese el numero primo Q (diferente a P):")
q=int(input())

#primero estimamos el algoritmo de euclides para obtener el MCD 
def egcd(a, b):
	if a == 0:
		return b, 0, 1
	else:
		gcd, x, y = egcd(b % a, a)
		return gcd, y - (b//a) * x, x

#Determinamos valore n tales que n seal el producto de los primos y fn sea el producto de los mismos restando uno a cada primo antes de multiplicar
def n_a(p,q):
  return p*q
def fn(p,q):
  return (p-1)*(q-1)
 
# Generamos aleatoriamente las llaves
def generate_keys(phi):
  for e in range(2, phi):
  	gcd, discard, d = egcd(phi, e)
  	if gcd == 1:
  		return e, d

#Haciendo uso del algorimo de RSA encriptamos el mensaje.
def encrypt(m,d,n):
  return pow(m,d,n)
 

n=n_a(p,q)
f_n=fn(p,q)
 
print("Valor de n:",n)
 
e, d = generate_keys(f_n)
 
print("Llave Publica:",e)
print("Llave Privada:",d)
 

encrypted = encrypt(m,e,n)
print("Mensaje Encriptado:",encrypted)
print("Mensaje Desencriptado:",encrypt(encrypted,d,n))
print("Mensaje Plano:",m)
