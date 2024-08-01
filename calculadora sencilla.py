#Importando la libreria/biblioteca de matemáticas de Python:
import math

#DEFINICION DE LAS FUNCIONES:
def mostrar_titulo():
  '''
  input: no hay entradas
  process: mostrar titulo (está implícito en el nombre de la función, se sugiere que sea un verbo) 
  output: no hay salidas
  '''
  print('Ejemplo Calculadora Sencilla (+,-,*,/) por Felipe Escallón:')


def mostrar_menu():
  '''input: no recibe nada (0 entradas)
  process:mostrar menu 
  output: no retorna nada (0 salidas)'''   
  print()
  print("MENU:")
  print("1: Sumar (+)")  
  print("2: Restar (-)")
  print("3: Multiplicar (*)")
  print("4: Dividir (/)")
  print("5: Logaritmo (log10)")
  print("6: Coseno (cos)")
  print()

def ingresar_datos():
  '''input: no hay entradas
  process:ingresar datos (recibir/leer del usuario) 
  output: tres variables que contienen localmente las decisiones del usuario (opcion,numero_uno,numero_dos)'''
  opcion=input("Ingrese la opción deseada del menú: ") # la opción se guarda como cadena
  numero_uno=float(input('Ingrese el primer número de la operación:'))# guarda como flotante (número real)
  numero_dos=float(input('Ingrese el segundo número de la operación:'))# guarda como flotante (número real)
  return opcion,numero_uno,numero_dos


#POR FACILIDAD, LAS 7 FUNCIONES SIGUIENTES TIENEN ENTRADAS Y SALIDAS
def calcular_suma(numero_uno,numero_dos):
  '''input: 2 numeros
  process:calcular suma (sumar)
  output: suma'''
  suma=numero_uno+numero_dos
  return suma
  
def calcular_resta(numero_uno,numero_dos):
  return numero_uno-numero_dos

def calcular_multiplicacion(numero_uno,numero_dos):
  return numero_uno*numero_dos

def calcular_division(numero_uno,numero_dos):
  return numero_uno/numero_dos

def calcular_logaritmo_base10(numero):#x=numero (uno,dos)
  #aquí uso la función logaritmo que está dentro de math
  logaritmo=math.log10(numero)#x=numero
  return logaritmo

def calcular_coseno(angulo_radianes):#x=numero (uno,dos): se debe asociar con un angulo que se toma por defecto en radianes (Si está en grados, debe convertirse a radianes=angulo*3.1416/180)
  #aquí uso la función coseno que está dentro de math
  coseno=math.cos(angulo_radianes)#x=numero (angulo_radianes)
  return coseno

def procesar_y_mostrar_operacion(opcion,numero_uno,numero_dos):  
  '''input: opcion, numero_uno, numero_dos
  process:procesar y mostrar operacion (analizar las posibilidades para ejecutar la calculadora)
  output: no retorna valor porque por dentro imprime por pantalla todo'''
  if opcion=='1' or opcion=='+' or opcion=='Sumar':
    print("Vamos a sumar(+) los dos valores ingresados:")
    resultado=calcular_suma(numero_uno,numero_dos)
    print('La suma es:',resultado)
  if opcion=='2'or opcion=='-' or opcion=='Restar':
    print("Vamos a restar(-) los dos valores ingresados:\n")
    resultado=calcular_resta(numero_uno,numero_dos)    
    print("Resultado=",resultado) 
  if opcion=='3'or opcion=='*' or opcion=='Multiplicar':
    print("Vamos a multiplicar(*) los dos valores ingresados:\n")
    resultado=calcular_multiplicacion(numero_uno,numero_dos)    
    print("Resultado=",resultado)
  if opcion=='4'or opcion=='/' or opcion=='Dividir':
    print("Vamos a dividir(/) los dos valores ingresados:\n")
    #VALIDANDO EL DENOMINADOR (debe ser diferente de cero)
    if numero_dos!=0:
      resultado=calcular_division(numero_uno,numero_dos)    
      print("Resultado=",resultado)      
    else:
      print("¡No es posible dividir entre cero!")
  if opcion=='5'or opcion=='log10' or opcion=='Logaritmo':
    print("Vamos a calcular el logaritmo (log10) de los dos valores ingresados:\n")
    resultado1=calcular_logaritmo_base10(numero_uno)
    resultado2=calcular_logaritmo_base10(numero_dos)    
    print("Resultado1=",resultado1)
    print("Resultado2=",resultado2)

  if opcion=='6'or opcion=='cos' or opcion=='Coseno':
    print("Vamos a calcular el coseno (cos) de los dos valores ingresados:\n")
    resultado1=calcular_coseno(numero_uno)
    resultado2=calcular_coseno(numero_dos)    
    print("Resultado1=",resultado1)
    print("Resultado2=",resultado2)

def llamar_funciones():
  '''input: no hay entradas
  process:llamar funciones (en orden: mostrar_titulo,mostrar_menu, ingresar_datos, procesar_y_mostrar_operacion)
  output: no hay salidas'''
  mostrar_titulo()
  mostrar_menu()
  opcion,numero_uno,numero_dos=ingresar_datos()
  procesar_y_mostrar_operacion(opcion,numero_uno,numero_dos) 


#EJECUCION DEL PROGRAMA:
llamar_funciones()

