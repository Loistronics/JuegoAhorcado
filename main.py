from random import  *
def palabra_azar():
    lista_palabras = ['FAMILIA','TROMPETA','TELEVISION','FUNERARIA','ESDRUJULA','NAVIDAD','ELECTRONICA','ASADO']
    palabra = choice(lista_palabras)
    longitud = len(palabra)
    return palabra,"_"*longitud
def pedir_letra(palabra,progreso,vidas):
    vidas = vidas
    letra = input("Ingrese una letra: ").upper()
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letra in abecedario and len(letra) == 1:
        validar_letra(letra,palabra,progreso,vidas)
    else:
        print("Por Favor ingrese una letra no otro tipo de caracter")
        pedir_letra(palabra,progreso,vidas)
def validar_letra(letra,palabra,progreso,vidas):
    progreso_anterior = list(progreso)
    progreso = ""
    if letra in palabra:
        for i in enumerate(palabra):
            if i[1] == letra:
                progreso = progreso + i[1]
            else:
                progreso = progreso + "_"
        progreso = list(progreso)

        for i in enumerate(progreso):
            if i[1] != "_":
                indice = i[0]
                progreso_anterior[indice] = i[1]
        print(progreso_anterior)
    else:
        vidas = vidas - 1
        print(f"Vidas: {vidas}")
        if vidas == 0:
            print("!!!!!PERDISTE!!!!!")
            print(f"La palabra era: {palabra}")
            return False
    if ("".join(progreso_anterior)).replace(" ","") == palabra:
        print("!!!!!GANASTE!!!!!")
    else:
        pedir_letra(palabra,progreso_anterior,vidas)

vidas = 6
palabra,guiones = palabra_azar()
print(guiones)
pedir_letra(palabra,guiones,vidas)
