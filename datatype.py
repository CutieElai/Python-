#Hablemos de STRINGS

#Podemos crear Strings a partir de comillas, o comillas dobles.
print("Hello World")
print("""Hello World""")
print('Hello World')
print('''Hello World''')

#Tambien podemos poner en el comander cmd "type("Hello world")" para ver que tipo de dato es. Nos tendria que salir que es STR.
#Tambien podemos directamente ponerlo aca Ej. 

print(type("Hello world"))

print("Bye" + "World")
#Lo que nos permite el simbolo + es unir dos string. Esta operacion se llama concadenar, 

#Hablemos de NUMEROS

#Integor/Entero
print(10)

#Float/Decimal
print(30.5)

#Booleam/Penamiento logico, sirve para describir un estado.
True
False

#List/agrupa datos
[10, 20, 30, 40, 50]
#Pondremos corchetes para agrupar los numeros.
#Para indicar que son distintos numeros, y que no se suman pondremos comas.
[10, "Hello", "Bye", 10.5, True]

#Tuples/agrupa datos. La diferencia con la Lista es que esta si se pueden cambiar los datos. Mientras que en Tuples no. Los datos seran asi para siempre.
(10, 20, 30)

#Dictionary
{"name":"Elisa",
"Last name":"Busson Roca",
"Nickname":"Elito"
}

#Las comas sirven para separar datos. Los dictionarys son datos que pertenecen a un mismo grupo. 
print(type({"name":"Elisa",
"Last name":"Busson Roca",
"Nickname":"Elito"
}))

None 
#None sirve para decir que aun no tenemos definido ningun tipo de dato