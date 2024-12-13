import smtplib

def envoieEmail():
    try:
        # Vérifier si le fichier contenant les adresses e-mail existe
        file_name = "destinataires.txt"
        try:
            with open(file_name, "r") as file:
                destinataires = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Le fichier {file_name} est introuvable. Assurez-vous qu'il existe dans le dossier.")
            return

        if not destinataires:
            print(f"Le fichier {file_name} est vide. Ajoutez des adresses e-mails pour continuer.")
            return

        print(f"Adresses e-mail trouvées dans {file_name} :")
        for i, email in enumerate(destinataires, start=1):
            print(f"{i}. {email}")

        # Sélectionner un destinataire par son index ou envoyer à tous
        print("\nEntrez un numéro pour sélectionner une adresse e-mail, ou tapez 'all' pour envoyer à toutes :")
        choice = input("Votre choix : ").strip()

        if choice.lower() == "all":
            selected_addresses = destinataires
        else:
            try:
                index = int(choice) - 1
                if index < 0 or index >= len(destinataires):
                    print("Numéro invalide.")
                    return
                selected_addresses = [destinataires[index]]
            except ValueError:
                print("Choix invalide.")
                return

        subject = input("Entrez l'objet de l'e-mail : ").strip()
        message_body = input("Entrez le message : ").strip()

        # Construire le message complet avec l'objet
        message = f"Subject: {subject}\n\n{message_body}"

        fromaddrs = 'lebotquispam@gmail.com'

        with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('lebotquispam@gmail.com', 'pdjd wsaq ievw iwhc')

            for email in selected_addresses:
                smtpserver.sendmail(fromaddrs, email, message)
                print(f"E-mail envoyé à : {email}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Lancer la fonction envoyer_email sans afficher de menu
if __name__ == "__main__":
    envoieEmail()
