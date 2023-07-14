import os
from PIL import Image
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time

# Chemin du dossier contenant les photos
dossier_photos = r'C:\Users\chris\OneDrive\Documents\Python Scripts\chronophoto\photo_test'

# Création des listes pour stocker les résolutions et les années
resolutions = []
annees = []

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier_photos):
    # Vérification de l'extension du fichier
    if fichier.endswith('.jpg') or fichier.endswith('.JPG') or fichier.endswith('.JPEG') or fichier.endswith('.jpeg'):
        # Extraction de l'année à partir du nom du fichier
        annee = int(fichier.split('-')[0])
        # Construction du chemin complet du fichier
        chemin_fichier = os.path.join(dossier_photos, fichier)
        # Ouverture de l'image avec PIL
        image = Image.open(chemin_fichier)
        # Récupération de la résolution de l'image
        resolution = image.size
        # Calcul du produit des dimensions de la résolution
        resolution_valeur = resolution[0] * resolution[1]
        # Fermeture de l'image
        image.close()
        # Ajout de la résolution et de l'année aux listes correspondantes
        resolutions.append(resolution_valeur)
        annees.append(annee)
    else:
        print(f'Fichier ignoré : {fichier} (extension non valide)')

# Tracé du graphe de la résolution en fonction de l'année
plt.plot(annees, resolutions, 'o-')
plt.xlabel('Année')
plt.ylabel('Résolution')
plt.title('Évolution de la résolution des photos')

plt.show(block=False)  # Affichage du graphe sans bloquer

time.sleep(5)  # Pause de 5 secondes

plt.close()  # Fermeture manuelle de la fenêtre du graphe
