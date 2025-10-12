# Taller 1 — Exploración, Ingeniería de Características y PCA (HELOC)

## Objetivo
Familiarizarse con el dataset **HELOC** y aplicar **ingeniería de características** y **PCA** para comprender la estructura de los datos.

## Actividades
1. Cargar `./data/heloc.csv` y describir variables (tipos, nulos, estadísticas).
2. Ingeniería de características (ejemplos): ratios, escalado selectivo (StandardScaler/MinMaxScaler).
3. Aplicar **PCA** (estandarizar antes) y graficar los **dos primeros componentes** con colores por `RiskPerformance`.
4. Documentar **hallazgos** en markdown dentro del notebook.

## Entregables
- `taller1_exploracion_pca.ipynb` con celdas ordenadas y comentarios.
- 1–2 gráficos (correlaciones, PCA).

## Pista de inicio rápido (Python)
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv('data/heloc.csv')
num_cols = df.select_dtypes(include='number').columns
X = df[num_cols].dropna()  # ajuste responsable de NA segun tu criterio
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2).fit_transform(X_scaled)

plt.scatter(pca[:,0], pca[:,1], s=8)
plt.title('PCA HELOC (2D)')
plt.show()
```
