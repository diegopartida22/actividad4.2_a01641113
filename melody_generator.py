import numpy as np
import sounddevice as sd
import time
from pathlib import Path

"""
Matriz de Transición para la Cadena de Markov:
- Cada fila representa la nota actual
- Cada columna representa la nota siguiente
- Los valores (0.143) representan la probabilidad de transición entre notas
- Ejemplo de interpretación:
  * P(DO → RE) = 0.143: Probabilidad de pasar de DO a RE
  * P(MI → LA) = 0.143: Probabilidad de pasar de MI a LA
  * Todas las transiciones tienen la misma probabilidad (1/7)

        DO     RE     MI     FA    SOL     LA     SI
DO   0.143  0.143  0.143  0.143  0.143  0.143  0.143 
RE   0.143  0.143  0.143  0.143  0.143  0.143  0.143 
MI   0.143  0.143  0.143  0.143  0.143  0.143  0.143 
FA   0.143  0.143  0.143  0.143  0.143  0.143  0.143 
SOL  0.143  0.143  0.143  0.143  0.143  0.143  0.143 
LA   0.143  0.143  0.143  0.143  0.143  0.143  0.143 
SI   0.143  0.143  0.143  0.143  0.143  0.143  0.143 


Para generar una melodía, se debe generar una cadena de Markov con la matriz de transición anterior.

Probar el programa.
python melody_generator.py
"""

# Diccionario de notas y sus frecuencias
NOTAS = {
    'DO': 261.63,  # C4
    'RE': 293.66,  # D4
    'MI': 329.63,  # E4
    'FA': 349.23,  # F4
    'SOL': 392.00, # G4
    'LA': 440.00,  # A4
    'SI': 493.88   # B4
}

# Crear matriz de transición con probabilidades iguales
num_notas = len(NOTAS)
matriz_transicion = np.full((num_notas, num_notas), 1/num_notas)

# Lista de notas para indexación fácil
lista_notas = list(NOTAS.keys())

def imprimir_matriz_transicion():
    """Imprime la matriz de transición en un formato legible"""
    print("\nMatriz de Transición:")
    print("    " + " ".join(f"{nota:>6}" for nota in lista_notas))
    for i, nota_actual in enumerate(lista_notas):
        print(f"{nota_actual:3}", end=" ")
        for prob in matriz_transicion[i]:
            print(f"{prob:6.3f}", end=" ")
        print()

def reproducir_nota(frecuencia, duracion=0.5):
    """Reproduce una nota con la frecuencia dada por una duración específica"""
    # Tasa de muestreo y tiempo
    tasa_muestreo = 44100
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
    
    # Generar nota con fade in/out para evitar clicks
    nota = np.sin(2 * np.pi * frecuencia * t)
    
    # Aplicar fade in/out
    duracion_fade = 0.05  # 50ms de fade
    longitud_fade = int(duracion_fade * tasa_muestreo)
    fade_in = np.linspace(0, 1, longitud_fade)
    fade_out = np.linspace(1, 0, longitud_fade)
    
    nota[:longitud_fade] *= fade_in
    nota[-longitud_fade:] *= fade_out
    
    # Reproducir la nota
    sd.play(nota, tasa_muestreo)
    sd.wait()  # Esperar hasta que termine el sonido

def generar_melodia(num_transiciones, duracion=0.5):
    """Genera y reproduce una melodía con el número especificado de transiciones"""
    # Comenzar con una nota aleatoria
    indice_nota_actual = np.random.randint(0, len(lista_notas))
    
    print("\nGenerando melodía:")
    for _ in range(num_transiciones):
        nota_actual = lista_notas[indice_nota_actual]
        print(f"Reproduciendo: {nota_actual}")
        
        # Reproducir la nota actual
        reproducir_nota(NOTAS[nota_actual], duracion)
        
        # Elegir la siguiente nota basada en las probabilidades de transición
        indice_nota_actual = np.random.choice(len(lista_notas), p=matriz_transicion[indice_nota_actual])

def main():
    print("Generador de Melodías usando Cadena de Markov")
    print("Todas las transiciones tienen probabilidad igual:", 1/num_notas)
    
    # Imprimir la matriz de transición
    imprimir_matriz_transicion()
    
    # Generar una melodía con 20 transiciones
    num_transiciones = 20
    print(f"\nGenerando una melodía con {num_transiciones} transiciones...")
    generar_melodia(num_transiciones)

if __name__ == "__main__":
    main() 