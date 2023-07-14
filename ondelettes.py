# Méthode 2 : Transformée en ondelettes
def calculer_niveau_bruit_ondelettes(image):
    # Conversion de l'image en niveaux de gris
    image_gris = image.convert('L')
    
    # Conversion de l'image en un tableau NumPy
    pixels = np.array(image_gris)
    
    # Calcul de la transformée en ondelettes
    coeffs = pywt.dwt2(pixels, 'haar')
    
    # Extraction du coefficient de détail (high frequency)
    coeffs_details = coeffs[1][0]
    
    # Calcul de l'écart-type du coefficient de détail
    ecart_type = np.std(coeffs_details)
    
    return ecart_type