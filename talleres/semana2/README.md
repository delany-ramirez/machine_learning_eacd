# Taller 2 — Regresión y Validación Cruzada (HELOC)

## Objetivo
Construir y evaluar **modelos de regresión** para estimar un **score** de riesgo crediticio.

## Actividades
1. Derivar una **variable continua** de riesgo (p. ej., `RiskPerformance` → {Bad:1, Good:0} y suavizar con probabilidad o media por grupo).
2. Entrenar **Regresión Lineal**, **Ridge** y **Lasso** con **validación cruzada**.
3. Comparar **MAE**, **MSE**, **R²** y escoger el modelo más estable.
4. Visualizar **residuos** y discutir sesgo–varianza.

## Entregables
- `taller2_regresion_cv.ipynb` con resultados y gráficos comparativos.

## Pista de inicio rápido
```python
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

# X, y preparados...
cv = KFold(n_splits=5, shuffle=True, random_state=42)
for model in [LinearRegression(), Ridge(alpha=1.0), Lasso(alpha=0.1)]:
    scores = cross_val_score(model, X, y, cv=cv, scoring='neg_mean_absolute_error')
    print(model.__class__.__name__, -scores.mean(), '+/-', scores.std())
```
