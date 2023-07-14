import numpy as np
import urllib.request
import requests
import os


def telecharger_image(url, chemin_fichier):
    try:
        response = requests.get(url)
        print(response)
        response.raise_for_status()
        print(response.raise_for_status())

        with open(chemin_fichier, 'wb') as fichier:
            fichier.write(response.content)

        print("Téléchargement terminé !")
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement :", e)
print(1+1)
# Exemple d'utilisation
    
url = "http://www.chronophoto.app/katylies/1910/49.JPEG"
chemin_fichier = r"C:\\Users\\chris\\OneDrive\\Documents\\Python Scripts\\chronophoto\\photos\\1910_42.JPEG"

telecharger_image(url, chemin_fichier)








