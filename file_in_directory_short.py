import os
import shutil

# Répertoire de départ
repertoire_source = '/chemin/vers/votre/repertoire'

# Parcourir tous les fichiers dans le répertoire source
for fichier in os.listdir(repertoire_source):
    # Ignorer les répertoires
    if os.path.isfile(os.path.join(repertoire_source, fichier)):
        # Obtenir l'extension du fichier
        extension = os.path.splitext(fichier)[1].lower()

        # Définir le répertoire de destination en fonction de l'extension
        if extension:
            repertoire_destination = os.path.join(repertoire_source, extension[1:])
        else:
            repertoire_destination = os.path.join(repertoire_source, 'Autres')

        # Créer le répertoire de destination s'il n'existe pas encore
        os.makedirs(repertoire_destination, exist_ok=True)

        # Déplacer le fichier vers le répertoire de destination
        chemin_source = os.path.join(repertoire_source, fichier)
        chemin_destination = os.path.join(repertoire_destination, fichier)

        # Déplacer le fichier
        shutil.move(chemin_source, chemin_destination)

print("Tri des fichiers terminé.")