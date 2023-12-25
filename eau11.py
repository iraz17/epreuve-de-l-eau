import sys

def absolute_difference_number(tableau):

    tableau_trie = sorted(tableau)
    diff_min_absolue = abs(tableau_trie[1] - tableau_trie[0])
    for i in range(1, len(tableau_trie) - 1):
        diff_actuelle = abs(tableau_trie[i + 1] - tableau_trie[i])
        if diff_actuelle < diff_min_absolue:
            diff_min_absolue = diff_actuelle

    return diff_min_absolue


 
def main():

    if len(sys.argv) < 3:
        print("Erreur : Le tableau doit contenir au moins deux éléments.")
        sys.exit(1)
     
    
    
    # Récupérer les nombres depuis les arguments en ligne de commande
    nombre = [int(arg) for arg in sys.argv[1:]]
    

    result = absolute_difference_number(nombre)
    print(result)

if __name__ == "__main__":
    main()


