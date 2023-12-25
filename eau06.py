import sys

def string_in_string(sub_str, main_str):
    sub_len = len(sub_str)
    for i in range(len(main_str) - sub_len + 1):
        if main_str[i:i+sub_len] == sub_str:
            return True
    return False
    

def main():
    if len(sys.argv) != 3:
        print("error")
        sys.exit(1)
    # Vérifier si un argument est fourni en ligne de commande
    try:
        sub_str = str(sys.argv[1])
        main_str = str(sys.argv[1])
    except ValueError:
        print("error")
        sys.exit(1)


    result = string_in_string(sub_str, main_str)
    print(result)

if __name__ == "__main__":
    main()