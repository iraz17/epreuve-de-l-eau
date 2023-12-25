import sys

def order_ASCII(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
        
def afficher_elements(elements):
    for element in elements:
        print(element, end=' ')

def main():
    if len(sys.argv) < 1:
        print("Erreur : Le tableau doit contenir au moins deux éléments.")
        sys.exit(1)

    elements = [str(arg) for arg in sys.argv[1:]]

    result = order_ASCII(elements)
    print(result)

if __name__ == "__main__":
    main()