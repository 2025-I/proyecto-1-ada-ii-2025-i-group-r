
import re
from unidecode import unidecode

def normalizar_cadena(cadena):
    sin_tildes = unidecode(cadena).lower()
    return re.sub(r'[^a-z0-9]', '', sin_tildes)