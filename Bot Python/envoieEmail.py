import smtplib

def envoieEmail():
    try:
        # Demander à l'utilisateur les informations nécessaires
        print("Entrez les informations nécessaires pour envoyer un e-mail :")
        toaddrs = input("Adresse e-mail de destination : ").strip()
        subject = input("Objet de l'e-mail : ").strip()
        message_body = input("Message : ").strip()

        # Construire le message complet avec l'objet
        message = f"Subject: {subject}\n\n{message_body}"

        fromaddrs = 'qmcoullery@gmail.com'

        with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('qmcoullery@gmail.com', 'pdjd wsaq ievw iwhc')

            # Demander combien de messages envoyer
            num_messages = int(input("Combien de messages souhaitez-vous envoyer ? "))

            for i in range(num_messages):
                smtpserver.sendmail(fromaddrs, toaddrs, message)
                print(f"Message {i + 1} envoyé à {toaddrs}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Lancer la fonction envoyer_email sans afficher de menu
if __name__ == "__main__":
    envoieEmail()
