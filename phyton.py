varible= 42
decimal= 20.5
verdadero= True 

# string
texto= "hola mundo"
print(texto.upper())   # pone el texto en mayusculas
print(texto.lower())   # minuscula
print(texto.find("mun"))
print(texto.find("Mun"))
print(texto.replace("mun","Ya no hay mun"))
print(texto)
print("mundo" in texto)

#aritmetica
print(5+2)
print(5^2)
print(5*5)
print(5**2)
print(10%3) #modulo

n=10
print(n>=10)
print(n>=11)  #da true o false, no 0 y 1

#INPUT
edad = input("ingresa tu edad")   #mete un string
print(edad)
print(type(edad))

#Conversion variables, cambian o intentar llevar el dato q le pongas dentro al nombre de la funcion

numero =int(edad)
print(type(numero))
str(numero)
float(numero)
bool() # los unicos datos q se pondran falsos son: False , 0 , "", none      (las dos comillas es un string)

#logicos

i=10
print(   i>8  and  i<30   )
print(   i>8  or  i<30   )
print (not( i>7))     #es un negador  como la afirmacion es correcta el negador la cambia y saldra false
