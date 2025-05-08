import re
from unidecode import unidecode

patron_normalizacion = re.compile(r'[^a-z0-9]')

def normalizar_cadena(cadena):
    
    if not isinstance(cadena, str):
        return ''
    
    sin_tildes = unidecode(cadena).lower()
    return patron_normalizacion.sub('', sin_tildes)