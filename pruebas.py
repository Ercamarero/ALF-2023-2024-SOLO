import re as re


vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
consonanteES = ["n", "s"]
duplas = ["ll", "Ll", "ch", "Ch","rr", "Rr"]
consonantes='bcdfghjklmnñpqrstvwxyz'
consonantes2=["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]

#R1 la primera la segunda sílaba empieza justo en la primera consonante v1 c v2 -- seg silaba --> c v2
pR1 = r"(?P<P1>[aeiouáéíóúü]([bcdfghjklmnñpqrstvwxyz]|ll|rr|ch)[aeiouáéíóúü])"
#R2 la segunda sílaba empieza justo en la primera consonante R2ab ->
pR2 = r"(?P<P2>[aeiouáéíóúü](([pcbgf][rl])|([dt]r))[aeiouáéíóúü])"
#R2c la segunda sílba empieza en la segunda consonante R2c -> v1 c1 c2 v2 -> c2 v2
pR2c = r"(?P<P2c>[aeiouáéíóúü][bcdhjklmnñpqrstvwxyz][bcdhjklmnñpqrstvwxyz][aeiouáéíóúü])"
#R3 si siguen la regla 2a y 2b entonces la segunda sílaba es c2 R3 -> v1 c1 c2 c3 v2 -> c2 c3 v2
pR3 = r"(?P<P3>[aeiouáéíóúü][bcdfghjklmnñpqrstvwxyz](([pcbgf][rl])|([dt]r))[aeiouáéíóúü])"
#R3bc si sigue la regla 3bc entonces la segunda sílaba empiezza por c3 -> c3 v2
pR3bc = r"(?P<P3bc>[aeiouáéíóúü](([bdnmlr]s)|(st))[bcdfghjklmnñpqrstvwxyz][aeiouáéíóúü])"
#R4 reglas C1 C2 -> 3b | 3c   C3 C4 -> 2a   la segunda sílaba es siempre c3 -> v1 c1 c2 c3 c4 v2 -> c3 c4 v2
pR4 = r"(?i)(?P<P4>[aeiouáéíóúü](([bdnmlr]s)|(st))[pcbgf][rl][aeiouáéíóúü])"

#R5 Diptongo v1 v2 -> no hay separación
pR5a = r"(?P<P5a>([aeoáéó]h?[iu])|([iuü]h?[aeoáéó])|(ih?[uúü]|íh?[uü]|[uü]h?[ií]|úh?i))"

#R5b
pR5bc= r"(?P<P5bc>[aeou]h?[íú]|[íú]h?[aeou]|[aá]h?[aá]|[eé]h?[eé]|[ií]h?[ií]|[oó]h?[oó]|[uú]h?[uú]|[aeoáéó][aeoáéó])"

#R6 Triptongo -> Después de v3
pR6 = r"(?P<P6>[iuy][aeoáéó][iuy])"

#EXPRESIÓN REGULAR GRANDE COMPILADA R
R= re.compile(pR4 + "|" + pR1 + "|" + pR2 + "|" + pR2c + "|" + pR3 + "|" + pR3bc + "|" + pR6 + "|" + pR5a + "|" + pR5bc )
def tonica(silabas):
    if len(silabas) == 1:
        mod = silabas[0]
    elif len(silabas) > 2 and any(k in 'áéíóúÁÉÍÓÚ' for k in silabas[-3]):
        mod = silabas[1]
    else:
        if any(k in 'áéíóúÁÉÍÓÚ' for k in silabas[-2]):
            mod = silabas[1]
        elif any(k in 'áéíóúÁÉÍÓÚ' for k in silabas[-1]):
            mod = silabas[len(silabas) - 1]
        else:
            if (silabas[-1][-1] in 'ns' or silabas[-1][-1] in 'aeiouAEIOU'):
                mod = silabas[1]
            else:
                mod = silabas[len(silabas) - 1]

    return mod

def entonacion(lista_silabas):
    print(len(lista_silabas))
    #Contador para saber dónde estamos de las sílabas
    iterador = len(lista_silabas)
    #Cuando nos hayamos quedado sin sílabas
    while(iterador <= 0):
        #Comprobamos sobreesdrújulas
        silaba= 
        if(iterador in 'áéí')
        iterador = iterador - 1





def silabear(cadena):
    cortes = []
    corteactual = 0
    corteanterior = 0
    while (len(cadena) != corteactual ):
        m = R.search(cadena,corteactual)
        #El objeto patrón m daría None salta una excepción en ejecución. Por eso la tratamos primero
        if m == None:
            #EN EL CASO DE QUE NO SE ENCUENTRE NADA EN LA CADENA
            if corteanterior != corteactual:
                cortes.append(cadena[corteanterior:len(cadena)])
            else:
                cortes.append(cadena[corteactual:len(cadena)])
            break
        if m.group("P1"):
            cortes.append(cadena[corteanterior:m.start()+1])
            corteactual = m.start()+1
            corteanterior = corteactual
            continue

        elif m.group("P2"):
            cortes.append(cadena[corteanterior:m.start()+1])
            corteactual = m.start()+1
            corteanterior = corteactual
            continue
        # R2c la segunda sílba empieza en la segunda consonante R2c -> v1 c1 c2 v2 -> c2 v2
        elif m.group("P2c"):
            cortes.append(cadena[corteanterior:m.start()+2])
            corteactual=m.start()+2
            corteanterior = corteactual
            continue
        # R3 si siguen la regla 2a y 2b entonces la segunda sílaba es c2 R3 -> v1 c1 c2 c3 v2 -> c2 c3 v2
        elif m.group("P3"):
            cortes.append(cadena[corteanterior:m.start()+2])
            corteactual=m.start()+2
            corteanterior = corteactual
            continue
        # R3bc si sigue la regla 3bc entonces la segunda sílaba empiezza por c3 -> c3 v2
        elif m.group("P3bc"):
            cortes.append(cadena[corteanterior:m.start()+2])
            corteactual=m.start()+2
            corteanterior = corteactual
            continue

        elif m.group("P4"):
            cortes.append(cadena[corteactual:m.start() + 3])
            corteactual = m.start() + 3
            corteanterior = corteactual
            continue

        elif m.group("P6"):
            #TAMBIÉN TENEMOS EL PROBLEMA AQUÍ EN P6 EL MISMO QUE EN 5A
            corteactual = m.end()
            continue

        #R5 Diptongos e hiatos
        #NO SEPARAMOS SÍLABAS EN 5A
        elif m.group("P5a"):
            #POR HACER PROBAR PALABRA FUNCIÓN -> aplauso es complicado
            #TENEMOS QUE: Coger desde el principio del anterior
            #Es decir desde la última regla aplicada coger el corteactual
            #Supongamos una palabra aplauso -> ahora mismo estamos cogiendo a plauso -> a so
            #Idea una variable anterior que almacene el último
            corteactual=m.end()-1
            continue

        # Si es hiato rompemos a partir de la primera vocal v1 v2 -> v2
        elif m.group("P5bc"):
            cortes.append(cadena[corteanterior:m.start()+1])
            corteactual=m.start()
            continue



    return cortes



intentos=0
while(intentos<100):
    cadena= input()
    resolv = silabear(cadena)
    print(resolv)
    print(tonica(resolv))
    print(entonacion(resolv))
    intentos=intentos+1