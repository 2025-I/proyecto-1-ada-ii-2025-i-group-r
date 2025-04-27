from src.palindrome.utils import normalizar_cadena

def es_palindromo(s):
    return s == s[::-1]

def encontrar_palindromo_fuerza_bruta(s):
    n = len(s)
    if n == 0:
        return ""
    
    max_palindromo = s[0] 

    for i in range(n):
        for j in range(i + 1, n + 1):
            subcadena = s[i:j]
            if es_palindromo(subcadena) and len(subcadena) > len(max_palindromo):
                max_palindromo = subcadena
    
    return max_palindromo

def resolver(cadena):
    cadena_procesada = normalizar_cadena(cadena)
    return encontrar_palindromo_fuerza_bruta(cadena_procesada)
