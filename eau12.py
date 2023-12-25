import sys

def my_bubble_sort(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

 


def main():
    if len(sys.argv) < 3:
        print("Erreur : Le tableau doit contenir au moins deux éléments.")
        sys.exit(1)
     # Récupérer les nombres depuis les arguments en ligne de commande
    tab = [int(arg) for arg in sys.argv[1:]]

    result = my_bubble_sort(tab)
    print(result)

if __name__ == "__main__":
    main()