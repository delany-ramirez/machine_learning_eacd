# Curso de Machine Learning (40h)
# Especialización en Analítica y Ciencia de Datos Aplicada


Repositorio del curso intensivo de **Machine Learning** basado en el dataset **HELOC (Home Equity Line of Credit)**.
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
- **Semana 2**: **Regresión** (lineal, Ridge, Lasso), **validación cruzada** y métricas.  
- **Semana 3**: **Clasificación** (Logística, KNN, SVM, Árboles), **Ensembles** (Random Fores, Gradient Boosting), **búsqueda de hiperparámetros**.  
- **Semana 4**: **Clustering** (K-Means, DBSCAN, Agrupamiento jerárquico), **despliegue** (FastAPI), **MLflow**, **proyecto final**.

> Nota: se asume competencia previa en **limpieza de datos** (curso anterior de minería de datos).

## Dataset de caso de estudio
- **HELOC — FICO Data Science Challenge**.  
- Objetivo: `RiskPerformance` (Good/Bad). Úsalo como **binaria** (clasificación) o derivando un **score** (regresión).

## Instalación (local)
```bash
# 1) Clonar / crear el repo y entrar
# git clone https://github.com/<tu-usuario>/curso-ml-heloc.git
cd curso-ml-heloc

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
