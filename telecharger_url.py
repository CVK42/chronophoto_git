def telecharger_image(url, chemin_fichier):
    try:
        response = requests.get(url)
#        print(response)
        response.raise_for_status()
#        print(response.raise_for_status())

        with open(chemin_fichier, 'wb') as fichier:
            fichier.write(response.content)

#        print("Téléchargement terminé !")
    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement :", e)