import re as re

patron_R1 = re.compile(r"(?i)[aeiouáéíóú]([[bcdfghjklmnñpqrstvwxyz]|ll|rr|ch)[aeiouáéíóú]")  # 4
patron_R2 = re.compile(r"(?i)[aeiouáéíóú]?([pcbgf][rl][aeiouáéíóú]|[dt]r[aeiou]|[bcdfghjklmnñpqrstvwxyz][bcdfghjklmnñpqrstvwxyz][aeiouáéíóú])")  # 3

patron_R3 = re.compile(r"(?i)[aeiou][bdnmlr]s|[aeiou]st")  # 2
patron_R5a = re.compile(r"(?i)[qwrtypsdfghjklñzxcvbnm|ll|rr|ch]?([aeoáéó]h?[iu]|[iuü]h?[aeoáéó]|[uiúíü]h?[uiúíü])")  # 5
patron_R5b = re.compile(r"(?i) [qwrtypsdfghjklñzxcvbnm|ll|rr|ch]? ([aeou]h?[íú]|[íú]h?[aeou]|[aá]h?[aá]|[eé]h?[eé]|[ií]h?[ií]|[oó]h?[oó]|[uú]h?[uú]|[aeoáéó][aeoáéó])")
# patron_R5c = re.compile(r"(?i) ([aeiouáéíó]h[aeiouáéíóú])")
patron_R6 = re.compile(r"(?i)[qwrtypsdfghjklñzxcvbnm|ll|rr|ch]?[iuy][aeoáéó][iuy]")  # Menos general 1
patron_Ge = re.compile(r"[qwrtypsdfghjklñzxcvbnm|ll|rr|ch]?[aeiouáéíóú]")


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


def silabear(cadena):
    cortes = []
    corteactual = 0
    while corteactual <= (len(cadena) - 1):
        cortecercano = 99999
        m = patron_R6.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual + 1):
                if m.end() + 1 == len(cadena):
                    cortes.append(cadena[corteactual:m.end() + 1])
                    corteactual = m.end() + 1
                    continue
                else:
                    cortes.append(cadena[corteactual:m.end()])
                    corteactual = m.end()
                    continue
            else:
                cortecercano = m.start()
                pass

        m = patron_R2.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual):
                if cadena[m.start()] in ['a''e''i''o''u''á''é''í''ó''ú']:
                    cortes.append(cadena(m.start()))
                    cortes.append(cadena[m.start() + 1:m.end()])
                    corteactual = m.end()
                    continue
                else:
                    cortes.append(cadena[m.start():m.end()])
                    corteactual = m.end()
                    continue
            else:
                cortecercano = m.start()
                pass

        m = patron_R1.search(cadena, corteactual)
        if m:
            if m.start() <= (corteactual + 1):
                if m.end() + 1 == len(cadena):
                    s1 = cadena[corteactual:(m.start() + 1)]
                    s2 = cadena[(m.start() + 1):m.end() + 1]
                    cortes.append(s1)
                    cortes.append(s2)
                    corteactual = m.end() + 1
                    continue
                else:
                    s1 = cadena[corteactual:(m.start() + 1)]
                    s2 = cadena[(m.start() + 1):m.end()]
                    cortes.append(s1)
                    cortes.append(s2)
                    corteactual = m.end()
                    continue
            else:
                cortecercano = m.start()
                pass

        if cortecercano == 99999:
            s1 = cadena[corteactual:len(cadena)]
            cortes.append(s1)
            break
        else:
            s1 = cadena[corteactual:cortecercano + 1]
            cortes.append(s1)
            corteactual = cortecercano + 1
            continue

    return cortes


resolv = silabear(cadena)
print(resolv)