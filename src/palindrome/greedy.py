import re
from src.palindrome.utils import normalizar_cadena

def encontrar_palindromo_voraz(s):
    n = len(s)
    if n == 0:
        return ""
    
    def expandir_desde_centro(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    max_palindromo = s[0]  
    
    for i in range(n):
        pal1 = expandir_desde_centro(i, i)
        pal2 = expandir_desde_centro(i, i+1)

        longer = pal1 if len(pal1) > len(pal2) else pal2
        
        if len(longer) > len(max_palindromo):
            max_palindromo = longer
    
    return max_palindromo

def resolver(cadena):
    cadena_procesada = normalizar_cadena(cadena)
    return encontrar_palindromo_voraz(cadena_procesada)