# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 7. Ejercicio 3


# Basado en la implementacion del algoritmo KMP
# hallada en https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

def longest_prefix_suffix(s):
    # Inicializa la lista que almacenará la longitud del prefijo-sufijo más largo
    lps = [0]*len(s)
    length = 0
    i = 1 

    # Recorre la cadena de entrada
    while i < len(s):
        # Si el carácter actual coincide con el carácter en la posición 'length'
        # de la subcadena que es el prefijo-sufijo más largo, incrementa la longitud
        # del prefijo-sufijo y avanza al siguiente carácter
        if s[i] == s[length]:
            length += 1
            lps[i] = length  
            i += 1            
        # Si el caracter no coincide, intenta encontrar un prefijo-sufijo más corto
        else:
            # Si 'length' es distinto de cero, intenta encontrar un prefijo-sufijo más corto
            if length != 0:
                length = lps[length-1]
            # Si 'length' es cero, no se encontró un prefijo-sufijo, así que avanza al siguiente carácter
            else:
                lps[i] = 0
                i += 1
            

    # Devuelve la subcadena que es el prefijo-sufijo más largo
    return s[:lps[-1]]


if __name__ == "__main__":
    
    print(longest_prefix_suffix("ABRACADABRA"))
    print(longest_prefix_suffix("AREPERA"))
    print(longest_prefix_suffix("PROGRAMA"))
