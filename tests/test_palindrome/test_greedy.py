import unittest
import time
import random
import string
from src.palindrome.greedy import resolver

class TestGreedyPalindrome(unittest.TestCase):

    def setUp(self):
        self.test_cases = {
            "pequeño": self.generar_cadena_aleatoria(100),     
            "mediano": self.generar_cadena_aleatoria(1000),     
            "grande": self.generar_cadena_aleatoria(10000),     
            "extra_grande": self.generar_cadena_aleatoria(50000)
        }

    def generar_cadena_aleatoria(self, longitud):
        caracteres = string.ascii_letters + string.digits  
        return ''.join(random.choice(caracteres) for _ in range(longitud))

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

    def test_03_grande(self):
        self.run_test_with_repeats("grande", self.test_cases["grande"])

    def test_04_extra_grande(self):
        self.run_test_with_repeats("extra_grande", self.test_cases["extra_grande"])

if __name__ == '__main__':
    unittest.main()