import sys

def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(1, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    number_table = fib_sequence[-1]

    return number_table

def main():
    # Vérifier si un argument est fourni en ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_terms>")
        sys.exit(1)

    # Récupérer le nombre de termes depuis la ligne de commande
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Veuillez fournir un nombre entier.")
        sys.exit(1)

    # Générer et afficher la suite de Fibonacci
    result = fibonacci(n)
    print(result)

if __name__ == "__main__":
    main()