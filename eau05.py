import sys

def est_nombre_premier(nombre):
    
    while nombre == nombre:
        if nombre <= 1:
            nombre = nombre + 1
        elif nombre == 2:
            return nombre
        elif nombre % 2 == 0:
            nombre = nombre + 1
        else:
            # Vérifier les diviseurs impairs jusqu'à la racine carrée du nombre
            for i in range(3, int(nombre**0.5) + 1, 2):
                if nombre % i == 0:
                    nombre = nombre + 1
            return nombre

def main():
    # Vérifier si un argument est fourni en ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_terms>")
        sys.exit(1)
    elif sys.argv[1] == '-':
        print("-1")
        sys.exit(1)
    # Récupérer le nombre de termes depuis la ligne de commande
    try:
        nombre = int(sys.argv[1])
    except ValueError:
        print("Veuillez fournir un nombre entier.")
        sys.exit(1)

# Afficher le premier nombre premier 
    result = est_nombre_premier(nombre)
    print(result)

if __name__ == "__main__":
    main()