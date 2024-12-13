import os
from envoieEmail import envoieEmail
from programme2 import programme2
from programme3 import programme3

# Codes d'échappement ANSI pour les couleurs
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BLUE = "\033[34m"
RED = "\033[31m"

def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/macOS
        os.system('clear')

def menu():
    while True:  # Boucle pour réafficher le menu après chaque choix
        clear_terminal()
        print(GREEN + "███████    ████████    ██████████")
        print("██    ██   ██    ██        ██    ")
        print("██  ██     ██    ██        ██    ")
        print("██    ██   ██    ██        ██    ")
        print("███████    ████████        ██    ")

        print(RESET + "\nVeuillez choisir un programme à exécuter:\n")
        print(YELLOW + "1 - Programme 1 : Envoi d'e-mails")
        print(CYAN + "2 - Programme 2 : Exemple de programme 2")
        print(BLUE + "3 - Programme 3 : Exemple de programme 3")
        print(RED + "4 - Quitter")

        choice = input(RESET + "\nEntrez le numéro de votre choix: ").strip()

        if choice == '1':
            envoieEmail()  # Appel à la fonction d'envoi d'e-mails
        elif choice == '2':
            programme2()  # Appel au programme 2
        elif choice == '3':
            programme3()  # Appel au programme 3
        elif choice == '4':
            print("Au revoir!")  # Option pour quitter proprement
            break  # Quitte la boucle et donc le programme
        else:
            print("Choix invalide, essayez à nouveau.")  # Si l'utilisateur entre un choix invalide

if __name__ == "__main__":  # Assure-toi que ceci est bien dans ton script principal
    menu()
