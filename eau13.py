import sys 

def select(tab, indice_start=0):
    if len(tab) - 1 > indice_start:
        value_min = indice_start
        for j in range(indice_start+1, len(tab)):
            if tab[j] < tab[value_min]:
                value_min = j
            tab[value_min], tab[indice_start] = tab[indice_start], tab[value_min]
        select(tab, indice_start+1) 




def main():
    if len(sys.argv) < 3:
        print("Erreur : Le tableau doit contenir au moins deux éléments.")
        sys.exit(1)

    tab  = [int(arg) for arg in sys.argv[1:]]

    result = select(tab)
    print(result)

if __name__ == "__main__":
    main()