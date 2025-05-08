from src.palindrome.utils import normalizar_cadena

def encontrar_palindromo_voraz(s):
    n = len(s)
    if n == 0:
        return ""
    
    def expandir_desde_centro(left, rigth):
        while left >= 0 and rigth < n and s[left] == s[rigth]:     
            left -=1
            rigth +=1
            
        return s[left+1:rigth]
            
    max_palindrome = s[0]
    
    for i in range(n):
        pal1 = expandir_desde_centro(i, i)
        pal2 = expandir_desde_centro(i, i+1)
        
        mas_largo = pal1 if len(pal1) > len(pal2) else pal2
        
        if len(mas_largo) > len(max_palindrome):
            max_palindrome = mas_largo
    
    return max_palindrome

def resolver(cadena):
    cadena_procesada = normalizar_cadena(cadena)
    return encontrar_palindromo_voraz(cadena_procesada)