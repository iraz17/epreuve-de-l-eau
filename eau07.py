import sys

def capital_on_two(charac): 
    resultat = ""
    make_uppercase = True

    for caractere in charac:
        if caractere.isalpha():  # Vérifier si le caractère est une lettre
            if make_uppercase:
                resultat += caractere.upper()
            else:
                resultat += caractere.lower()
            make_uppercase = not make_uppercase
        else:
            resultat += caractere

    return resultat

        

def main():
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)
    # Vérifier si un argument est fourni en ligne de commande
    try:
        charac = str(sys.argv[1])
    except ValueError:
        print("error")
        sys.exit(1)


    result = capital_on_two(charac)
    print(result)

if __name__ == "__main__":
    main()