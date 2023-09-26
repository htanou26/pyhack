import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fonction pour générer le rapport HTML
def generer_rapport():
    # Remplacez ceci par la logique pour générer votre rapport
    rapport = "<html><body><h1>Rapport Automatisé</h1><p>Contenu du rapport ici.</p></body></html>"
    return rapport

# Paramètres du serveur SMTP (utilisez les informations de votre fournisseur de messagerie)
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'votre_email@example.com'
smtp_password = 'votre_mot_de_passe'

# Destinataires de l'e-mail
destinataires = ['destinataire1@example.com', 'destinataire2@example.com']

# Génération du rapport
rapport_html = generer_rapport()

# Création de l'e-mail
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = ', '.join(destinataires)
msg['Subject'] = 'Rapport Automatisé'

# Corps du message au format HTML
msg.attach(MIMEText(rapport_html, 'html'))

# Connexion au serveur SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Envoi de l'e-mail
    server.sendmail(smtp_username, destinataires, msg.as_string())
    server.quit()

    print("E-mail envoyé avec succès !")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'e-mail : {str(e)}")
