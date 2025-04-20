from tkinter import Tk, Button, filedialog

#from src.palindrome.dynamic import resolver
from src.palindrome.greedy import resolver
#from src.palindrome.brute_force import resolver


def procesar_lineas(lines):
    try:
        n = int(lines[0].strip())
        cadenas = [line.strip() for line in lines[1:n+1] if line.strip()]
        return cadenas
    except (ValueError, IndexError) as e:
        print(f"Error: Formato de archivo incorrecto. {str(e)}")
        return []

def open_file():
    filepath = filedialog.askopenfilename(
        initialdir=".",
        title="Selecciona el archivo de entrada",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            cadenas = procesar_lineas(lines)
            for cadena in cadenas:
                resultado = resolver(cadena)
                print(resultado.lower()) 

def run_gui():
    window = Tk()
    window.title("Seleccionar archivo")
    window.geometry("300x150")
    Button(window, text="Abrir archivo (DP)", 
           command=open_file).pack(pady=10)
    window.mainloop()

if __name__ == "__main__":
    run_gui()