import re as re

patron_R1 = re.compile(r"(?i)[aeiouáéíóúü]([bcdfghjklmnñpqrstvwxyz]|ll|rr|ch)[aeiouáéíóúü]")  # 4
patron_R2 = re.compile(r"(?i)[aeiouáéíóúü]?([pcbgf][rl][aeiouáéíóú]|[dt]r[áéíóúaeiouü]|([hjklmnñqrsvwxyz][bcdfghjklmnñpqrstvwxyz]|[bcdfghjklmnñpqrstvwxyz][bcdfghjkmnñpqstvwxyz])[aeiouáéíóúü])")  # 3
patron_R2c = re.compile(r"(?i)[qwrtypsdfghjklñzxcvbnm|ll|rr|ch]?[aeiouáéíóúü]([hjklmnñqrsvwxyz][bcdfghjklmnñpqrstvwxyz]|[bcdfghjklmnñpqrstvwxyz][bcdfghjkmnñpqstvwxyz])[aeiouáéíóúü]")
patron_R3 = re.compile(r"(?i)[aeiou][bdnmlr]s|[aeiou]st")  # 2
patron_R5a = re.compile(r"(?i)[aeoáéó]h?[iu]|[iuü]h?[aeoáéó]|[uiúíü]h?[uiúíü]")  # 5
patron_R5b = re.compile(r"(?i)[aeou]h?[íú]|[íú]h?[aeou]|[aá]h?[aá]|[eé]h?[eé]|[ií]h?[ií]|[oó]h?[oó]|[uú]h?[uú]|[aeoáéó][aeoáéó]")
patron_R6 = re.compile(r"(?i)[qwrtypsdfghjklñzxcvbnm|ll|rr|ch]?[iuy][aeoáéó][iuy]")  # Menos general 1
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
consonanteES = ["n"]
duplas = ["ll", "Ll", "ch", "Ch", "rr", "Rr"]
global corteactual  # VARIALBLE GLOBAL PARA LA GESTION DEL SILABEO

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


cadena = input()


def silabeoaux(iniciobase, finbase, cadena, cortes):
    global corteactual
    aux = patron_R5a.search(cadena, finbase)
    aux1 = patron_R5b.search(cadena, finbase)
    aux2 = patron_R6.search(cadena, finbase)
    if aux:
        if aux.end()+1 >= len(cadena):
            cortes.append(cadena[iniciobase:len(cadena)])
            corteactual = len(cadena)
            return cortes
        else:
            cortes.append(cadena[iniciobase:aux.end()])
            corteactual = aux.end()
            return cortes
    elif aux1:
        if aux1.end()+1 >= len(cadena):
            cortes.append(cadena[iniciobase:aux1.start()])
            cortes.append(cadena[aux1.start()+1: len(cadena)])
            corteactual = len(cadena)
            return cortes
        else:
            cortes.append(cadena[iniciobase:aux1.start()+1])
            cortes.append(cadena[aux1.start()+1:aux1.end()])
            corteactual = aux1.end()
            return cortes
    elif aux2:
        if aux2.end()+1 >= len(cadena) and aux2.end()-1 != "y":
            cortes.append(cadena[iniciobase:len(cadena)])
            corteactual = len(cadena)
        elif aux2.end()-1 == "y" and aux2.end() == len(cadena):
            cortes.append(cadena[iniciobase:aux2.end()-1])
            corteactual = aux2.end()-1
            return cortes
        else:
            cortes.append(cadena[iniciobase:aux2.end()])
            return cortes
        return cortes
    else:
        return cortes


def silabear(cadena):
    cortes = []
    global corteactual
    corteactual = 0
    while corteactual <= (len(cadena) - 1):
        cortecercano = 99999
        m = patron_R6.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual):
                x = cadena[m.end() - 1]
                if x == "y" and not m.end() == len(cadena):
                    cortes.append(cadena[m.start(): m.end() - 1])
                    corteactual = m.end() - 1
                    continue
                else:
                    cortes.append(cadena[m.start(): m.end()])
                    corteactual = m.end()
                    continue
            else:
                if m.start() < cortecercano:
                    cortecercano = m.start()
                    pass
                else:
                    pass

        # m = patron_R3.search(cadena,corteactual)
        # if m:
        m = patron_R5a.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual + 1):
                if (m.end() + 1) >= len(cadena):
                    cortes.append(cadena[corteactual:len(cadena)])
                    corteactual = len(cadena)
                    continue
                else:
                    s0 = cadena[m.end()]
                    if s0 in consonanteES:
                        cortes.append(cadena[corteactual:m.end() + 1])
                        corteactual = m.end() + 1
                        continue
                    else:
                        cortes.append(cadena[corteactual:m.end()])
                        corteactual = m.end()
                        continue
            else:
                if m.start() < cortecercano:
                    cortecercano = m.start()
                    pass
                else:
                    pass

        m = patron_R2.search(cadena,corteactual)
        if m:
            if m.start() <= (corteactual):
                if patron_R2c.match(m.group(0)):
                    if m.end()+1 >= len(cadena):
                        cortes.append(cadena[corteactual:m.start()+2])
                        cortes.append(cadena[m.end()-2 : len(cadena)])
                        corteactual = len(cadena)
                    else:
                        cortes.append(cadena[corteactual:m.start()+2])
                        cortesaux = silabeoaux(m.start()+2,m.end()-1,cadena,cortes)
                        if cortesaux == cortes:
                            cortes.append(cadena[m.end()-2:m.end()])
                            corteactual = m.end()
                            continue
                        else:
                            cortes = cortesaux
                            continue
                    continue
                else:
                    if m.start() in vocales:
                        cortes.append(cadena[corteactual:m.start()])
                        if m.end()+1 >= len(cadena):
                            cortes.append(cadena[m.start()+1:len(cadena)])
                            corteactual = len(cadena)
                            continue
                        else:
                            cortesaux = silabeoaux(m.start()+1,m.end()-1,cadena,cortes)
                            if cortesaux != cortes:
                                cortes.append(cadena[m.start()+1:m.end()])
                                corteactual = m.end()
                                continue
                            else:
                                cortes = cortesaux
                                continue
                    else:
                        if m.end()+1 >= len(cadena):
                            cortes.append(cadena[corteactual:len(cadena)])
                            corteactual = len(cadena)
                            continue
                        else:
                            cortesaux = silabeoaux(m.start(),m.end()-1,cadena,cortes)
                            if cortes != cortesaux:
                                cortes.append(cadena[m.start():m.end()])
                                corteactual = m.end()
                                continue
                            else:
                                cortes = cortesaux
                                continue
            else:
                if m.start() < cortecercano:
                    cortecercano = m.start()
                    pass
                else:
                    pass

        m = patron_R1.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual + 1):
                if m.end() + 1 >= len(cadena):
                    if cadena[m.start() + 1: m.start() + 2] in duplas:
                        cortes.append(cadena[m.start()])
                        cortes.append(cadena[m.start() + 1: m.end()])
                        corteactual = m.end()
                        continue
                    else:
                        s1 = cadena[corteactual:(m.start() + 1)]
                        s2 = cadena[(m.start() + 1):m.end() + 1]
                        cortes.append(s1)
                        cortes.append(s2)
                        corteactual = m.end() + 1
                        continue
                else:
                    s1 = cadena[m.start()]
                    cortes.append(s1)
                    aux = patron_R5a.search(cadena, (m.end() - 1))  # diptongo
                    aux1 = patron_R5b.search(cadena, (m.end() - 1))  # hiato
                    aux2 = patron_R6.search(cadena, (m.end() - 1))  # triptongo (muy improbable pero posible)
                    if aux:
                        if aux and aux.start() <= m.end():
                            if aux.end() + 1 >= len(cadena):
                                cortes.append(cadena[m.start() + 1: len(cadena)])
                                corteactual = len(cadena)
                                continue
                            else:
                                cortes.append(cadena[m.start() + 1: aux.end()])
                                corteactual = aux.end()
                                continue
                    elif aux1 and aux1.start() <= m.end():
                        if aux1.end() + 1 >= len(cadena):
                            cortes.append(cadena[m.start() + 1:aux.start()])
                            cortes.append(cadena[aux.start() + 1:len(cadena)])
                            corteactual = len(cadena)
                            continue
                        else:
                            cortes.append(cadena[m.start() + 1:aux1.start()])
                            cortes.append(cadena[aux1.start() + 1:aux1.end()])
                            corteactual = aux1.end()
                            continue
                    elif aux2 and aux2.start() <= m.end():
                        if aux2.end() + 1 <= len(cadena) and aux2.end() - 1 == "y":
                            cortes.append(cadena[m.start() + 1:aux2.end() - 1])
                            corteactual = aux2.end() - 1
                            continue
                        else:
                            cortes.append(cadena[m.start() + 1:aux2.end()])
                            corteactual = aux2.end()
                            continue

                    else:
                        s2 = cadena[(m.start() + 1):m.end()]
                        cortes.append(s2)
                        corteactual = m.end()
                        continue
            else:
                if m.start() < cortecercano:
                    cortecercano = m.start()
                    pass
                else:
                    pass

        if cortecercano == 99999:
            s1 = cadena[corteactual:len(cadena)]
            cortes.append(s1)
            break
        else:
            if cadena[cortecercano] in vocales:
                s1 = cadena[corteactual:cortecercano + 1]
                cortes.append(s1)
                corteactual = cortecercano + 1
                continue
            else:
                s1 = cadena[corteactual:cortecercano]
                cortes.append(s1)
                corteactual = cortecercano
                continue

    return cortes


resolv = silabear(cadena)

print(resolv)
