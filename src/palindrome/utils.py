import re
from unidecode import unidecode

PATRON_NORMALIZACION = re.compile(r'[^a-z0-9]')

def normalizar_cadena(cadena):
    if not isinstance(cadena, str):
        return ''  
    
    sin_tildes = unidecode(cadena).lower()
    return PATRON_NORMALIZACION.sub('', sin_tildes)