# Predicción de Riesgo de Seguros de Vehículos

Esta aplicación web permite predecir el riesgo de seguros de vehículos utilizando diferentes modelos de machine learning.

## Características

- Interfaz web interactiva usando Streamlit
- Múltiples modelos de predicción:
  - Árbol de Decisión (DT)
  - Regresión Logística (RL)
  - K-Nearest Neighbors (Knn)
  - Support Vector Machine (SVM)
  - Random Forest (RF)
- Predicción basada en:
  - Edad del conductor
  - Tipo de vehículo

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación:

```bash
streamlit run main.py
```

La aplicación se abrirá en tu navegador web predeterminado.

## Estructura del Proyecto

- `main.py`: Aplicación principal
- `config.py`: Configuración y constantes
- `requirements.txt`: Dependencias del proyecto
- `modelo-clas-tree-RL-Knn-SVM-RF.pkl`: Modelos entrenados
- `Logo_seguro_carro.jpg`: Logo de la aplicación 
