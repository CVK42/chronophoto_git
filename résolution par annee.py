import os
from PIL import Image
import matplotlib.pyplot as plt

# Chemin du dossier contenant les photos
dossier_photos = r'C:\Users\chris\OneDrive\Documents\Python Scripts\chronophoto\photo_test'

# Création des listes pour stocker les résolutions et les années
resolutions = []
annees = []

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier_photos):
    print(fichier)
    # Vérification de l'extension du fichier
    if fichier.endswith('.jpg') or fichier.endswith('.JPG') or fichier.endswith('.JPEG') or fichier.endswith('.jpeg'):
        print('bonne extension')
        # Extraction de l'année à partir du nom du fichier
        annee = int(fichier.split('-')[0])
        print(annee)
        # Construction du chemin complet du fichier
        chemin_fichier = os.path.join(dossier_photos, fichier)
        print(chemin_fichier)
        # Ouverture de l'image avec PIL
        image = Image.open(chemin_fichier)
        print(image)
        # Récupération de la résolution de l'image
        resolution = image.size
        print(resolution)
        # Fermeture de l'image
        image.close()
        # Ajout de la résolution et de l'année aux listes correspondantes
        resolutions.append(resolution)
        annees.append(annee)
    else :
        print('pas la bonne extension')

# Tracé du graphe de la résolution en fonction de l'année
plt.plot(annees, resolutions, 'o-')
plt.xlabel('Année')
plt.ylabel('Résolution')
plt.title('Évolution de la résolution des photos')
plt.show()