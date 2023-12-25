import sys

def afficher_valeurs(min_arg, max_arg):
    # Afficher les valeurs comprises entre minimum (inclus) et maximum (exclus)
    if min_arg < max_arg:
        for valeur in range(min_arg, max_arg):
            print(valeur, end=' ')
    else:
        print("Erreur : La valeur minimale doit être inférieure à la valeur maximale.")

def main():
    # Vérifier le nombre d'arguments en ligne de commande
    if len(sys.argv) != 3:
        print("error : Veuillez fournir exactement deux arguments.")
        sys.exit(1)
    # Récupérer les valeurs passées en ligne de commande
    # Vérifier si les arguments sont des entiers
    try:
        min_arg, max_arg = int(sys.argv[1]), int(sys.argv[2])
    except ValueError:
        print("Error : Les valeurs doivent être des entiers.")
        sys.exit(1)

    
    result = afficher_valeurs(min_arg, max_arg)
    print(result)
if __name__ == "__main__":
    main()

    