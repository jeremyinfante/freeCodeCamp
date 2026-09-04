name = 'John Doe' # str
age = 25 # int
male = True # bool 
money = 82.04 # float

# imprimir por pantalla
print(name, age, male, money)

# verificar el tipo de dato usando type()
print(type(name))

# verificar tipo de dato usando isinstance()
# compara entre tipos de datos
# devuelve un valor booleano
print(isinstance(name, int)) # False
print(isinstance(name, str)) # True
