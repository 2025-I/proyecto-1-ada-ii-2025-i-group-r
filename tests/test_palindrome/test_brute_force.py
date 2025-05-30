import unittest
import time
import random
import string
from src.palindrome.brute_force import resolver

class TestBruteForcePalindrome(unittest.TestCase):

    def setUp(self):
        def generar_cadena_aleatoria(longitud):
            caracteres = string.ascii_letters + string.digits
            return ''.join(random.choice(caracteres) for _ in range(longitud))

        self.test_cases = {
            "pequeño": generar_cadena_aleatoria(10), 
            "mediano": generar_cadena_aleatoria(50),
            "medianoxl": generar_cadena_aleatoria(100)
        }

    def run_test_with_repeats(self, label, input_str):
        print(f"\nTamaño: {label.upper()} (longitud = {len(input_str)})")
        tiempos = []

        for i in range(5):
            inicio = time.time()
            resultado = resolver(input_str)
            fin = time.time()
            duracion = fin - inicio
            tiempos.append(duracion)

            print(f"  Repetición {i+1}: {duracion:.4f} segundos")
            self.assertEqual(resultado, resultado[::-1])

        promedio = sum(tiempos) / len(tiempos)
        print(f"  Tiempo promedio: {promedio:.4f} segundos")

    def test_01_pequeno(self):
        self.run_test_with_repeats("pequeño", self.test_cases["pequeño"])

    def test_02_mediano(self):
        self.run_test_with_repeats("mediano", self.test_cases["mediano"])
        
    def test_03_medianoXL(self):
        self.run_test_with_repeats("medianoxl", self.test_cases["medianoxl"])
        

if __name__ == '__main__':
    unittest.main()
