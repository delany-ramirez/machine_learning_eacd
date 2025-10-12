# Taller 3 — Clasificación y Optimización de Modelos (HELOC)

## Objetivo
Predecir si un cliente será **Good** (1) o **Bad** (0) y **optimizar** el mejor modelo.

## Actividades
1. Construir `y` binaria a partir de `RiskPerformance` (Good=1, Bad=0).
2. Entrenar: **LogisticRegression**, **KNN**, **SVM**, **DecisionTree**.
3. Evaluar: **accuracy**, **recall**, **F1**, **AUC-ROC**, **matriz de confusión**.
4. Elegir el mejor y aplicar **GridSearchCV**/**RandomizedSearchCV**.
5. Reportar los **mejores hiperparámetros** y su desempeño.

## Entregables
- `taller3_clasificacion_tuning.ipynb` con comparación de modelos y tuning.

## Pista de inicio rápido
```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test)))
print('AUC:', roc_auc_score(y_test, clf.predict_proba(X_test)[:,1]))
```
