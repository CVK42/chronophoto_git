
import matplotlib.pyplot as plt
import random

# Générer des données aléatoires
x = range(10)  # Valeurs de l'axe x (de 0 à 9)
y = [random.randint(1, 10) for _ in x]  # Valeurs de l'axe y (valeurs aléatoires entre 1 et 10)
print(x,y)
# Créer le graphe
plt.rcParams["figure.figsize"] = (10,8)
plt.plot(x, y, 'b-o')  # 'b-o' spécifie le style de ligne et de points

# Ajouter des titres et des labels aux axes
plt.title('Exemple de graphe')
plt.xlabel('Axe x')
plt.ylabel('Axe y')

# Afficher le graphe
plt.show()
print('1+1')