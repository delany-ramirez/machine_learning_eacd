# Taller 4 — Clustering y Despliegue (HELOC)

## Objetivo
Aplicar **clustering** para segmentación y crear un **endpoint** de inferencia con **FastAPI**, registrando el modelo con **MLflow**.

## Actividades
1. Ejecutar **K-Means** y **DBSCAN** sobre variables numéricas estandarizadas (`StandardScaler`). Evaluar con **silhouette**.
2. Exportar el **mejor modelo** (`joblib.dump(model, 'models/model.joblib')`).
3. Implementar **FastAPI** que reciba un JSON de entrada y devuelva la predicción.
4. Registrar corridas con **MLflow** (parámetros, métricas, artefactos).

## Entregables
- `taller4_clustering_despliegue.ipynb`
- `deployment/fastapi_app.py` funcionando localmente
- Registro MLflow básico (carpeta `mlruns/`)

## Comandos útiles
```bash
uvicorn deployment.fastapi_app:app --reload
mlflow ui
```
