import re
from src.palindrome.utils import normalizar_cadena
from itertools import combinations


def es_palindromo(s):
    return s == s[::-1]

def encontrar_palindromo_fuerza_bruta(s):
    n = len(s)
    if n == 0:
        return ""
    
    max_palindromo = ""

    for length in range(n, 0, -1):
        for indices in combinations(range(n), length):
            subseq = ''.join(s[i] for i in sorted(indices))
            if es_palindromo(subseq):
                if len(subseq) > len(max_palindromo):
                    max_palindromo = subseq
        if max_palindromo:
            break
    
    return max_palindromo if max_palindromo else s[0]

def resolver(cadena):
    cadena_procesada = normalizar_cadena(cadena)
    return encontrar_palindromo_fuerza_bruta(cadena_procesada)