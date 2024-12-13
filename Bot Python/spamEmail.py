import os
import smtplib
from email.message import EmailMessage
import sys

os.system('cls' if os.name == 'nt' else 'clear')

# Bannière
banner = f"""
\033[34m
    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝
    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗
    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝
    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝
\033[0m
"""
print(banner)

# Fonction pour obtenir l'entrée utilisateur
def get_input(prompt_text):
    print(prompt_text, end="")
    user_input = input("\033[32m")
    print("\033[0m", end="")
    if user_input.lower() == "exit":
        print("Exiting...")
        sys.exit()
    return user_input

# Paramètres prédéfinis
expediteur = "qmcoullery@gmail.com"
mot_de_passe = "Qc271107"
destinataire = "qcoullery@gmail.com"

# Récupérer les informations du message
nombre = int(get_input("Nombre de fois à envoyer l'email : "))
sujet = get_input("Sujet : ")
corps = get_input("Message à envoyer : ")

# Envoi des emails
for i in range(nombre):
    try:
        # Connexion au serveur SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(expediteur, mot_de_passe)

        # Création de l'email
        msg = EmailMessage()
        msg['From'] = expediteur
        msg['To'] = destinataire
        msg['Subject'] = sujet
        msg.set_content(corps)

        # Envoi de l'email
        server.send_message(msg)
        print(f"{i + 1}: Message envoyé depuis {expediteur} à {destinataire}.")

    except Exception as e:
        print(f"Une erreur est survenue lors de l'envoi : {e}")
    finally:
        server.quit()

print("Tous les emails ont été envoyés.")
