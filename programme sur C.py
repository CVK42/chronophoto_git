import numpy as np
import urllib.request
import requests
import os
import time
import re
import json
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



matches = re.findall(r'\[.*?\]', text)
L=[]

for i in range(len(matches)):
    urls_annee=matches[i].split(',')
    formatted_string = ','.join(urls_annee)
    nl = json.loads(formatted_string)
    L.append(nl)
    
    
ll=len(L)
n=1899
for annee in L:
    n=n+1
    numero_url=0
    for url in annee:
        numero_url=numero_url+1
        string_url = "http://" + str(url)
    #            print(string_url)
        chemin_fichier = r"C:\\Users\\chris\\OneDrive\\Documents\\Python Scripts\\chronophoto\\photos\\"+str(n)+"-"+str(numero_url)+".JPEG"
    
        telecharger_image(string_url, chemin_fichier)
        print(str(n)+'-'+str(numero_url))


temps_fin = time.time()
temps_execution = temps_fin - temps_debut
print("Le programme a mis", temps_execution, "secondes à s'exécuter.")
print("Nom du fichier Python :", os.path.basename(__file__))