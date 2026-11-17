# Strings / Cadenas

# 🎯 Objetivos
# Emplear varios métodos para concatenar cadenas con otras cadenas así como con otros tipos de datos.
# Utilizar la conversión de tipo con tipos numéricos primitivos.
# Identificar y utilizar la sintaxis correcta para las cadenas “f”.
# Concatenar múltiples variables en una cadena utilizando el método .format() con los argumentos apropiados.
# Familiarizarse con los métodos de cadena comúnmente utilizados y dónde encontrar más información.
# https://youtu.be/7HZaNDbkYAI

# 🧾 Cadena literal
# Las cadenas son secuencias de caracteres, pueden incluir letras, números, símbolos, y se colocan entre comillas simples o dobles. Por ejemplo:

print("Esta es una cadena de caracteres")
print('Esta es una cadena de caracteres con comillas simples')

# ➕ Concatenar cadenas y variables con la función print

# Existen distintas maneras en las que podemos imprimir una cadena que contenga información de variables.
#  Una de ellas es añadiendo una coma después de la cadena seguido de una variable.
#  Esto ocasiona que la función print() agregue un espacio entre los elementos separados por comas.

nombre = input("Ingresar nombre ") #Ingresado por teclado
print("Me llamo", nombre) #Concatenando con una , (coma)

# Otra manera es concatenando el contenido con la ayuda de +.

apellido = input("Ingresar apellido ") # Ingresado por teclado
print("Mi apellido es "+ apellido) # No se añade un espacio entre las cadenas

# A diferencia de la primera forma, esta no agrega ningún espacio entre las cadenas,
#  por lo que si queremos alguno es necesario colocarlo explícitamente. 
# Además de esta diferencia, entre las dos formas de concatenar, 
# existe otra distinción muy importante. 
# ¿Qué te parece si intentas concatenar una cadena con un entero usando +? ¡Nos da un error!

#ejemplo

#print("¿Cuántas vocales hay? " + 5) 
#ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5


# 🔄 Conversión de tipos (Type Casting) o Conversión de tipo explícito
# Python no tiene manera de unir una cadena con un número, pero sí de juntar dos cadenas. Entonces es necesario convertir el número a cadena para poder “sumar” ambos valores.

# Podemos hacer la conversión también de cadena a número, por ejemplo:


tiempo_preparacion = 1
tiempo_horneado = "2"
# tiempo_total = tiempo_preparacion + tiempo_horneado 
# #ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_horneado) #Imprime: 3
# 🧩 Interpolación de cadenas
# También tenemos la posibilidad de insertar variables en nuestras cadenas, una práctica conocida como interpolación de cadenas. Existen distintas maneras de llevar a cabo esta tarea.

# ejemplo 2
numero1 = int(input("Ingrese el primer numero"))
#Ingresa valor y lo transforma a entero
numero1 = float(input("Ingrese el segundo numero"))
#Ingresa valor y lo transforma a decimal


# 🧬 Cadenas »f» (Interpolación de cadenas literal)
# A partir de la versión 3.6 de Python, se pueden utilizar las cadenas “f” para interpolar cadenas. La sintaxis es la siguiente: escribimos una f justo después de la comilla inicial. Después, dentro de la cadena escribimos la variable dentro de llaves.

nombre = "Marcelo"
edad = 29
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")

#Tarea: Crear variables con input.
# Ingresar nombre, anio_nacimiento, anio_actual, calcular edad
# Y mostrar en pantalla con f string

nombre1 = input("ingresa un nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = int(input("Ingresa el año actual: "))
edad1 = anio_actual - anio_nacimiento
print(f"Mi nombre es: {nombre1} y tengo {edad1} años.")

# 🛠️ string.format()
# Antes de que se introdujeran las cadenas “f”, esta misma funcionalidad se lograba con el método
#  .format(). Para usar este método, escribimos la cadena completa y colocamos llaves ({}) 
# en los espacios en los que queremos desplegar el valor de la variable. 
# Después invocamos al método format y pasamos las variables como argumentos 
# en el orden que debieran llenarse los parámetros {}. Por ejemplo:

nombre2 = "Marcelo"
edad2 = 29
print("Mi nombre es {} y tengo {} años de edad.".format(nombre2, edad2))


# ejercicio: Crear variables con input
# ingresar nombre_mascota, edad_mascota , especie_mascota
# mostrar en pantalla con .format()
# Frase libre 

nombre_mascota = input("Ingresa el nombre de tu mascota")
edad_mascota = input("Ingresa la edad de tu mascota")
especie_mascota = input("Ingresa la especie de tu mascota")

print("Mi mascota {} tiene {} años y su especie es {}".format(nombre_mascota, edad_mascota, especie_mascota))

# #Imprime: Mi nombre es Marcelo y tengo 29 años de edad.
# print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre))

# #Imprime: Tengo 29 años de edad y mi nombre es Marcelo
# Nota que el método format lee la cadena de caracteres de izquierda a derecha, y va reemplazando las {} con el valor de las variables dadas en orden. Es importante entender que dado a esto, el número de {} debe ser el mismo número de argumentos dados a la función.

# 🧮 %-formatting
# Quizás en algún código te puedas topar con un método que se utilizaba antes de que existiera las formas vistas antes de interpolación. En lugar de utilizar llaves, se utiliza el símbolo % para indicar un parámetro; %s para indicar una cadena y %d para indicar un número. Una vez establecida la cadena, se coloca de nuevo % para separar el texto de las variables que serán interpoladas. Por ejemplo:

# nombre = "Marcelo"
# edad = 29
# print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))

# #Imprime: Mi nombre es Marcelo y tengo 29 años de edad.