import requests
import os
import time
import re
import json
import matplotlib.pyplot as plt
temps_debut = time.time()

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




text = r"C:\\Users\\chris\\OneDrive\\Documents\\Python Scripts\\chronophoto\\url_chronophoto.txt"
with open(text, 'r') as fichier:
    text = fichier.read()
    
    
matches = re.findall(r'\[.*?\]', text)


L=[]
for i in range(len(matches)):
    urls_annee=matches[i].split(',')
    formatted_string = ','.join(urls_annee)
    nl = json.loads(formatted_string)
    L.append(nl)
    
"""
n=1899
for annee in L:
    n=n+1
    numero_url=0
    for url in annee:
        numero_url=numero_url+1
        string_url = "http://" + str(url)
        chemin_fichier = r"C:\\Users\\chris\\OneDrive\\Documents\\Python Scripts\\chronophoto\\photos\\"+str(n)+"-"+str(numero_url)+".JPEG"
        telecharger_image(string_url, chemin_fichier)
        print(str(n)+'-'+str(numero_url))

"""

# Liste des années
annees = [i for i in range(1900, 2023)]

# Compter le nombre de fichiers par année
nb_fichiers_par_annee = [len(annee) for annee in L]

# Créer le graphe
plt.scatter(annees, nb_fichiers_par_annee)
plt.xlabel('Année')
plt.ylabel('Nombre de fichiers')
plt.title('Nombre de fichiers par année')
plt.show()


'''
temps_fin = time.time()
temps_execution = temps_fin - temps_debut
print("Le programme a mis", temps_execution, "secondes à s'exécuter.")
print("Nom du fichier Python :", os.path.basename(__file__))'''