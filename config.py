# Configuración de la página
PAGE_CONFIG = {
    'page_title': 'Predicción de riesgo de seguros',
    'page_icon': '🚗',
    'layout': 'centered',
    'initial_sidebar_state': 'auto'
}

# Configuración de la imagen
IMAGE_CONFIG = {
    'logo_path': "Logo_seguro_carro.jpg",
    'width': 800
}

# Configuración del modelo
MODEL_CONFIG = {
    'model_path': "modelo-clas-tree-RL-Knn-SVM-RF.pkl"
}

# Opciones de vehículos
VEHICLE_TYPES = ["combi", "minivan", "sport", "family"]

# Opciones de modelos
MODEL_TYPES = ["DT", "RL", "Knn", "SVM", "RF"]

# Configuración de edad
AGE_CONFIG = {
    'min_value': 18,
    'max_value': 50,
    'default_value': 25,
    'step': 1
} 