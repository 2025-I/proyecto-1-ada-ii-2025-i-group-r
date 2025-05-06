from src.palindrome.utils import normalizar_cadena

def encontrar_palindromo_dinamica(s):
    n = len(s)
    if n == 0:
        return ""
    
    max_len = 1
    start = 0

    dp = [[False]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    
    return s[start:start+max_len]

def resolver(cadena):
    cadena_procesada = normalizar_cadena(cadena)
    return encontrar_palindromo_dinamica(cadena_procesada)