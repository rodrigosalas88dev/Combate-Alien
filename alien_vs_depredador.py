from random import randint
import os

VIDA_INICIAL_ALIEN = 80
VIDA_INICIAL_DEPREDADOR = 90

vida_alien = VIDA_INICIAL_ALIEN
vida_depredador = VIDA_INICIAL_DEPREDADOR

TAMANIO_BARRA_VIDA = 20

print("COMBATE ALIEN VS DEPREDADOR\n"
      "---------------------------\n")

while vida_alien > 0 and vida_depredador > 0:
    #Se desenvuelven los turnos de combate

    #Turno del alien
    print("Es el turno del Alien")
    ataque_alien = randint(1, 2)

    if ataque_alien == 1:
        #Ataque Aguijon Letal
        print("El Alien ataca con Aguijon Letal")
        vida_depredador -= 10
    else:
        #Ataque Decapitacion
        print("El Alien ataca con Decapitacion")
        vida_depredador -= 11

    if vida_alien < 0: #SE DEFINE PARA QUE LA VIDA NUNCA SE MUESTRE EN NEGATIVO
        vida_alien = 0

    if vida_depredador < 0:
        vida_depredador = 0

    barra_depredador = int(vida_depredador * TAMANIO_BARRA_VIDA / VIDA_INICIAL_DEPREDADOR)
    print("DEPREDADOR:    [{}{}] ({}/{})".format("*" * barra_depredador, " " * (TAMANIO_BARRA_VIDA - barra_depredador), vida_depredador, VIDA_INICIAL_DEPREDADOR))

    barra_alien = int(vida_alien * TAMANIO_BARRA_VIDA / VIDA_INICIAL_ALIEN)
    print("ALIEN:         [{}{}] ({}/{})".format("*" * barra_alien, " " * (TAMANIO_BARRA_VIDA - barra_alien), vida_alien, VIDA_INICIAL_ALIEN))

    if vida_alien <= 0 or vida_depredador <= 0:
        print("El combate ha finalizado")
        if vida_depredador <= 0:
            print("PERDISTE! GANA el ALIEN!")
        elif vida_alien <= 0:
            print("FELICITACIONES! GANA el DEPREDADOR")

    if vida_alien <= 0 or vida_depredador <= 0:
        exit()

    input("Enter para continuar...\n\n")
    os.system("cls")

    # Turno Depredador
    print("Es el turno del Depredador")
    print("Con que ataque deseas aniquilar al Alien?")


    ataque_depredador = None
    while ataque_depredador not in [1, 2, 3, 4]: #tiene que elegir si o si una opcion
        ataque_depredador = int(input("Ataque Laser (1), ataque Cuchillo Doble (2), ataque Patada Alta (3), No atacar(+5 de vida) y Teletransportación (4)"))
        print("Ese ataque no es valido")

    if ataque_depredador == 1:
        #Ataque Laser
        print("Depredador ataca con Laser")
        vida_alien -= 10

    elif ataque_depredador == 2:
        #Ataque Cuchillo Doble
        print("Depredador ataca con Cuchillo Doble")
        vida_alien -= 12

    elif ataque_depredador == 3:
        #Ataque Patada Alta
        print("Depredador ataca con Patada Alta")
        vida_alien -= 9

    elif ataque_depredador == 4:
        #Teletransportación
        print("Depredador se Teletransporta esta vez!")
        vida_depredador += 5

    else:
        #No elije opcion
        print("Ese ataque no existe!")

    if vida_alien < 0:
        vida_alien = 0

    if vida_depredador < 0:
        vida_depredador = 0

    barra_depredador = int(vida_depredador * TAMANIO_BARRA_VIDA / VIDA_INICIAL_DEPREDADOR)
    print("DEPREDADOR:    [{}{}] ({}/{})".format("*" * barra_depredador, " " * (TAMANIO_BARRA_VIDA - barra_depredador), vida_depredador, VIDA_INICIAL_DEPREDADOR))

    barra_alien = int(vida_alien * TAMANIO_BARRA_VIDA / VIDA_INICIAL_ALIEN)
    print("ALIEN:         [{}{}] ({}/{})\n".format("*" * barra_alien, " " * (TAMANIO_BARRA_VIDA - barra_alien), vida_alien, VIDA_INICIAL_ALIEN))

    if vida_alien <= 0 or vida_depredador <= 0:
        print("El combate ha finalizado")
        if vida_depredador <= 0:
            print("PERDISTE! GANA el ALIEN!")
        elif vida_alien <= 0:
            print("FELICITACIONES! GANA el DEPREDADOR")

    input("Enter para continuar...\n\n")
    os.system("cls")

    if vida_alien <= 0 or vida_depredador <= 0:
        exit()
