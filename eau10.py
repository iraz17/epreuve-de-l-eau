import sys

def trouver_index(element, tableau):
    # Rechercher l'index de l'élément dans le tableau
    try:
        index = tableau.index(element)
        return index
    except ValueError:
        return -1  # Retourner -1 si l'élément n'est pas trouvé
def main():
    # Vérifier s'il y a au moins deux arguments (un pour le script, un pour l'élément recherché)
    if len(sys.argv) < 3:
        print("Erreur : Veuillez fournir au moins deux arguments.")
        sys.exit(1)
    # Récupérer le tableau (tous les arguments sauf le dernier) et l'élément recherché (dernier argument)
    tableau = sys.argv[1:-1]
    element_recherche = sys.argv[-1]
    
    # Appeler la fonction pour trouver l'index de l'élément
    resultat = trouver_index(element_recherche, tableau)
    
    # Afficher le résultat
    print(resultat)
if __name__ == "__main__":
    main()