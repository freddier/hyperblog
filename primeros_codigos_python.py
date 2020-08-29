def conversor(moneda, tasa):
    pesos = input("¿Cuantos "+ moneda + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/tasa
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes USD" + dolares + " dolares")


def adivina_numero():
    """ Mini juego para adivinar un numero del 1 al 100, generado previamente de forma aleatoria
        
        no necesita param, ya que el unico numero (numero_elegido) se pide dentro de la funcion
    """        
    import random # para importar el modulo randon
    numero_aleatorio = random.randint(1, 100) #funcion randint (rand int) del modulo random
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    i=1
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            numero_elegido= int(input('Busca un numero mas grande: '))
        else:
            numero_elegido= int(input('Busca un numero mas pequeño: '))
        i+=1
    print('¡GANASTE!')
    print('En ' +str(i) +' intentos')


def main():
    """ funcion principal, menu de mini-proyectos
    """
    opcion = int(input('''     Que desea hacer?
        1. Adivina un numero
        2. Conversor de monedas
        3. Saber si un numero es par
        4. Saber si un numero es primo
        5. Generar una contraseña
        6. Comparar edad
        7. Enumeracion Exhaustiva
        8. Aproximacion
        9. Busqueda Binaria
        10. Factorial
        11.Fibonacci
     opcion: '''))
    if opcion == 1:
        print('******* Adivina un numero ******* ')
        adivina_numero()
    elif opcion == 2:
        opcion = 0
        while opcion < 1 or opcion > 3:
            print('******* Conversor de monedas ******* ')
            opcion = int(input('''Escoge la moneda que deseas convertir a dolares
                1. Bolivares
                2. Pesos Argentinos
                3. Pesos Chilenos )
                opcion: '''))
            if opcion == 1:
                conversor('Bolivares', 280000)
            elif opcion == 2:
                conversor('pesos Argentinos', 115)
            elif opcion == 3:
                conversor('pesos Chilenos', 730)
            else: 
                print('Elige una opcion valida')
                


if __name__ == '__main__':
    main()