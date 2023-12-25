import sys

def capitalizer(result):
    
    capitalized_words = [arg.capitalize() for arg in sys.argv[1:] ]  # Mettre en majuscule la première lettre de chaque mot
    result = ' '.join(capitalized_words)  # Joindre les mots pour former la chaîne de sortie
    return result


def main():
    if len(sys.argv) < 2:
        print("error")
        sys.exit(1)
    # Vérifier si un argument est fourni en ligne de commande
    try:
        input_string = str(sys.argv[1:])
    except ValueError:
        print("error")
        sys.exit(1)


    # Appliquer la transformation et afficher le résultat
    result = capitalizer(input_string)
    print(result)
    

if __name__ == "__main__":
    main()
