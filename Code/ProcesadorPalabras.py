import re as re

vocales = ["a", "e", "i", "o", "u", "y"]
cerradas = ["i", "u"]
abiertas = ["a", "e", "o"]

# R1 la primera la segunda sílaba empieza justo en la primera consonante
# v1 c v2 -- seg silaba --> c v2
pR1 = r"(?P<P1>[aeiouáéíóúü]([bcdfgjklmnñpqrstvwxyz]|ll|rr)[aeiouáéíóúü])"
# R2 la segunda sílaba empieza justo en la primera consonante R2ab ->
pR2 = r"(?P<P2>[aeiouáéíóúü](([pcbgf][rl])|([dt]r))[aeiouáéíóúü])"
# R2c la segunda sílba empieza en la segunda consonante R2c ->
# v1 c1 c2 v2 -> c2 v2
pR2c = r"(?P<P2c>[aeiouáéíóúü][bcdghfjklmnñpqrstvwxyz][bcdhfgjklmnñpqrstvwxyz][aeiouáéíóúü])"
# R3 si siguen la regla 2a y 2b entonces la segunda sílaba es c2 R3 ->
# v1 c1 c2 c3 v2 -> c2 c3 v2
pR3 = r"(?P<P3>[aeiouáéíóúü][bcdfghjklmnñpqrstvwxyz](([pcbgf][rl])|([dt]r))[aeiouáéíóúü])"
# R3bc si sigue la regla 3bc entonces la segunda sílaba empiezza por c3 ->
# c3 v2
pR3bc = r"(?P<P3bc>[aeiouáéíóúü](([bdnmlr]s)|(st))[bcdfghjklmnñpqrstvwxyz][aeiouáéíóúü])"
# R4 reglas C1 C2 -> 3b | 3c   C3 C4 -> 2a   la segunda sílaba es siempre c3 ->
# v1 c1 c2 c3 c4 v2 -> c3 c4 v2
pR4 = r"(?P<P4>([aeiouáéíóúü](([bdnmlr]s)|(st))[pcbgf][rl][aeiouáéíóúü]))"
# R5 Diptongo v1 v2 -> no hay separación
pR5a = r"(?P<P5a>(([aeoáéó]h?[iuü])|([iuü]h?[aeoáéó])|(ih?[uúü]|íh?[uü]|[uü]h?[ií]|úh?i)))"
# R5b Hiato v1 v2 -> separadas
pR5bc = r"(?P<P5bc>[aeou]h?[íú]|[íú]h?[aeou]|[aá]h?[aá]|[eé]h?[eé]|[ií]h?[ií]|[oó]h?[oó]|[uú]h?[uú]|[aeoáéó][aeoáéó])"
# R6 Triptongo -> Después de v3
pR6 = r"(?i)(?P<P6>[iu][aeoáéó][iuy])"
# Regla de tildes.
tilde = re.compile(r"(?i)(?P<Tilde>([a-z]+)?[áéíóú]([a-z]+)?)")
# Regla agudas
agudas = re.compile(r"(?P<Ag>([a-z]*[aeiou][ns]|[a-z]*[aeiouy]\b))")
aRe = r"(?i)(?P<A>[á])"
eRe = r"(?P<E>[é])"
iRe = r"(?P<I>[í])"
oRe = r"(?P<O>[ó])"
uRe = r"(?P<U>[úü])"
# EXPRESIÓN REGULAR GRANDE COMPILADA R
R = re.compile(pR6 + "|" + pR5a + "|" + pR5bc + "|" + pR1 + "|" + pR2 + "|" + pR2c + "|" + pR3 + "|" + pR3bc + "|" + pR4)
E = re.compile(pR6 + "|" + pR5a)
C = re.compile(aRe + "|" + eRe + "|" + iRe + "|" + oRe + "|" + uRe)


def tonica(silabas):
    t = E.search(silabas)
    mod = ''
    pos = 0
    if t:
        #comenzamos por los diptongos
        if t.group("P5a"):
            for i in silabas:
                if i in abiertas:
                    mod += i.upper()
                elif i in cerradas and  pos == 1:
                    mod += i.upper()
                elif i in cerradas and pos ==0:
                    mod += i
                    pos += 1
                else:
                    mod += i
            return mod
        else:
            for i in silabas:
                if i in vocales and pos == 0:
                    mod += i
                    pos += 1
                elif i in vocales and pos == 1:
                    mod += i.upper()
                    pos += 1
                else:
                    mod += i

            return mod
    else:
        for i in silabas:
            if i in vocales:
                mod += i.upper()
            else:
                mod += i
        return mod
    

def entonartonicas(silabeo):
    mod = ''
    for i in silabeo:
        m = C.match(i)
        if m:
            if m.group("A"):
                mod += "A"
                continue
            elif m.group("E"):
                mod += "E"
                continue
            elif m.group("I"):
                mod += "I"
                continue
            elif m.group("O"):
                mod += "O"
                continue
            elif m.group("U"):
                mod += "U"
                continue
        else:
            mod += i
            continue
    return mod

def entonar(cadena):
    aux = silabear(cadena)
    m = tilde.match(cadena)
    if len(aux) == 1 and m:
        aux = entonartonicas(aux[0])
        return aux
    elif len(aux) == 1:
        aux = tonica(aux[0])
        return aux
    if m:
        for i,silaba in enumerate(aux):
            if tilde.match(silaba):
                aux[i] = entonartonicas(silaba)
                continue
            else:
                continue
        return aux
    else:
        r = agudas.match(aux[-1])
        if r:
            aux[-1] = tonica(aux[-1])
            return  aux
        else:
            aux[-2] = tonica(aux[-2])
            return aux

def silabear(cadena):
    cortes = []
    corteactual = 0
    corteanterior = 0
    while (len(cadena) != corteactual):
        m = R.search(cadena, corteactual)
        # El objeto patrón m daría None salta una excepción en ejecución. Por eso la tratamos primero
        if m == None:
            # EN EL CASO DE QUE NO SE ENCUENTRE NADA EN LA CADENA
            if corteanterior != corteactual:
                cortes.append(cadena[corteanterior:len(cadena)])
            else:
                cortes.append(cadena[corteactual:len(cadena)])
            break

        elif m.group("P1"):
            cortes.append(cadena[corteanterior:m.start() + 1])
            corteactual = m.start() + 1
            corteanterior = corteactual
            continue

        if m.group("P2"):
            cortes.append(cadena[corteanterior:m.start() + 1])
            corteactual = m.start() + 1
            corteanterior = corteactual
            continue

        # R2c la segunda sílba empieza en la segunda consonante R2c ->
        # v1 c1 c2 v2 -> c2 v2
        elif m.group("P2c"):
            cortes.append(cadena[corteanterior:m.start() + 2])
            corteactual = m.start() + 2
            corteanterior = corteactual
            continue
        # R3 si siguen la regla 2a y 2b entonces la segunda sílaba es c2 R3 ->
        # v1 c1 c2 c3 v2 -> c2 c3 v2
        elif m.group("P3"):
            cortes.append(cadena[corteanterior:m.start() + 2])
            corteactual = m.start() + 2
            corteanterior = corteactual
            continue
        # R3bc si sigue la regla 3bc entonces
        # la segunda sílaba empieza por c3 -> c3 v2
        elif m.group("P3bc"):
            cortes.append(cadena[corteanterior:m.start() + 3])
            corteactual = m.start() + 3
            corteanterior = corteactual
            continue

        elif m.group("P4"):
            cortes.append(cadena[corteactual:m.start() + 3])
            corteactual = m.start() + 3
            corteanterior = corteactual
            continue
        # R5 Diptongos e hiatos
        # NO SEPARAMOS SÍLABAS EN 5A
        elif m.group("P5a"):
            # POR HACER PROBAR PALABRA FUNCIÓN -> aplauso es complicado
            # TENEMOS QUE: Coger desde el principio del anterior
            # Es decir desde la última regla aplicada coger el corteactual
            # Supongamos una palabra aplauso -> ahora mismo estamos cogiendo
            # aplauso -> a so
            # Idea una variable anterior que almacene el último
            if m.end() + 1 != len(cadena):
                cortes.append(cadena[corteanterior:m.end()])
                corteactual = m.end()
                corteanterior = corteactual
                continue
            else:
                cortes.append(cadena[corteanterior:m.end() + 1])
                corteactual = m.end() + 1
                corteanterior = corteactual
                continue

        # Si es hiato rompemos a partir de la primera vocal v1 v2 -> v2
        elif m.group("P5bc"):
            if m.end() + 1 != len(cadena):
                cortes.append(cadena[corteanterior:m.start() + 1])
                corteactual = m.start() + 1
                corteanterior = corteactual
                continue

        elif m.group("P6"):
            # TAMBIÉN TENEMOS EL PROBLEMA AQUÍ EN P6 EL MISMO QUE EN 5A

            if cadena[m.end() - 1] == "y" and m.end() < len(cadena):
                if cadena[m.end()] in vocales:
                    cortes.append(cadena[corteanterior:m.end() - 1])
                    corteactual = m.end() - 1
                    corteanterior = corteactual
                    continue
                else:
                    if m.end() + 1 != len(cadena):
                        cortes.append(cadena[corteanterior:m.end()])
                        corteactual = m.end()
                        corteanterior = corteactual
                        continue
                    else:
                        cortes.append(cadena[corteanterior:m.end() + 1])
                        corteactual = m.end() + 1
                        corteanterior = corteactual
                        continue
            else:
                if m.end() + 1 != len(cadena):
                    cortes.append(cadena[corteanterior:m.end()])
                    corteactual = m.end()
                    corteanterior = corteactual
                    continue
                else:
                    cortes.append(cadena[corteanterior:m.end() + 1])
                    corteactual = m.end() + 1
                    corteanterior = corteactual
                    continue

    return cortes

