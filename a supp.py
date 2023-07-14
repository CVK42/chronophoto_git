from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# Séparation des données d'entraînement et de test
train_data, test_data, train_labels, test_labels = train_test_split(ensemble_donnees, decennies, test_size=0.2, random_state=42)

decades=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]

# Séparation des caractéristiques et des étiquettes
train_features = [x[0] for x in train_data]
train_labels = [x[1] for x in train_data]
test_features = [x[0] for x in test_data]
test_labels = [x[1] for x in test_data]


# Initialisation du modèle Random Forest
model = RandomForestClassifier()
# Entraînement du modèle sur les données d'entraînement
model.fit(train_features, train_labels)
# Prédiction sur les données de test
predictions = model.predict(test_features)
# Calcul de la précision du modèle
accuracy = accuracy_score(test_labels, predictions)
print("Précision du modèle : {:.2f}%".format(accuracy * 100))
predictions = model.predict(test_features)


confusion = confusion_matrix(test_labels, predictions)
print("Matrice de confusion :")
print(confusion)


display = ConfusionMatrixDisplay(confusion_matrix=confusion, display_labels=decades)
# Plot the confusion matrix
display.plot()
plt.title("Confusion Matrix")
plt.show()

