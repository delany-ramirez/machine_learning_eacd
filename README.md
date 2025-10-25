# Curso de Machine Learning (40h)
# Especialización en Analítica y Ciencia de Datos Aplicada


Repositorio del curso intensivo de **Machine Learning para Modelos de Predicción**.
Incluye el **programa**, **talleres semanales** y **recursos** para que los estudiantes trabajen un proyecto integral
de predicción de riesgo crediticio.

> Modalidad: 4 semanas (10h/semana) — **Viernes (4h) + Sábado (6h)**.  
> Cada sábado incluye aproximadamente **2h 30m** de taller práctico.

## Estructura del repositorio
```
curso-ml-heloc/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ data/   
   ├─ heloc.csv
├─ notebooks/          
├─ talleres/
│  ├─ semana1/
│  ├─ semana2/
│  ├─ semana3/
│  └─ semana4/
└─ deployment/
   ├─ fastapi_app.py
   └─ sample_request.json
```

## Programa del curso (resumen)
- **Semana 1**: Intro ML, ciclo de vida, fundamentos (álgebra, cálculo, probabilidad), *ingeniería de características*, **PCA** y **T-Sne**.  
   -	Introducción al Aprendizaje Automático y ciclo de vida de un proyecto de ML
   -	Tipos de aprendizaje: supervisado, no supervisado y reforzado
   -	Herramientas del ecosistema Python para ML
   -	Fundamentos matemáticos aplicados al ML (álgebra lineal, cálculo y probabilidad)
   -	Ingeniería de características y reducción de dimensionalidad (PCA, t-SNE)

- **Semana 2**: **Regresión** (lineal, Ridge, Lasso), **validación cruzada** y métricas.  
   - Modelos de regresión lineal y regularizada (Ridge, Lasso)
   - Modelos de clasificación: Regresión Logística, K-Nearest Neighbors, Support Vector Machines, Árboles de Decisión
   - Validación cruzada y selección de modelos
   - Evaluación de desempeño en regresión y clasificación (MAE, MSE, R², Accuracy, Recall, F1, AUC-ROC)


- **Semana 3**: **Clasificación** (Logística, KNN, SVM, Árboles), **Ensembles** (Random Fores, Gradient Boosting), **búsqueda de hiperparámetros**.  
   - Ensemble Learning: Bagging, Random Forest y Gradient Boosting
   - Optimización de hiperparámetros (GridSearchCV, RandomizedSearchCV)
   - Comparación y selección de modelos óptimos
   - Interpretación y comunicación de resultados

- **Semana 4**: **Clustering** (K-Means, DBSCAN, Agrupamiento jerárquico), **despliegue** (FastAPI), **MLflow**, **proyecto final**.
   - Algoritmos de clustering: K-Means, DBSCAN y Jerárquico
   - Evaluación y visualización de clusters (Silhouette Score, Inertia)
   - Despliegue de modelos mediante API (Flask o FastAPI)
   - Tracking y versionamiento de modelos con MLflow
   - Proyecto final: desarrollo de un pipeline completo sobre el dataset HELOC

> Nota: se asume competencia previa en **limpieza de datos** (curso anterior de minería de datos).

## Dataset de caso de estudio
- **HELOC — FICO Data Science Challenge**. (https://huggingface.co/datasets/mstz/heloc) 
- Objetivo: `RiskPerformance` (Good/Bad). Úsalo como **binaria** (clasificación) o derivando un **score** (regresión).

## Instalación (local)
```bash
# 1) Clonar / crear el repo y entrar
# git clone https://github.com/delany-ramirez/machine_learning_eacd.git
cd curso-ml-heloc
```
A continuación se muestra un ejemplo de crear e instalar las librerías necesarias en un nuevo ambiente, sin embargo, puede utilizar otros gestores de ambientes si lo desea.

```bash
# 2) Crear entorno e instalar dependencias
python -m venv .venv
source .venv/bin/activate  # (Windows) .venv\Scripts\activate
pip install -r requirements.txt
```

## Flujo sugerido de trabajo
1. Descargar/ubicar **HELOC** en `./data/`  
2. Seguir los **talleres** por semana en `./talleres/semanaX/README.md`  
3. Guardar los notebooks en cada carpeta de taller  
4. Semana 4: exportar el modelo (`joblib`), exponer **FastAPI** y registrar con **MLflow**

## Licencia
MIT
