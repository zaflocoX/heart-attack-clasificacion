# Diccionario de Datos - Heart Attack Dataset

**Fuente:** https://www.kaggle.com/datasets/fatemehmohammadinia/heart-attack-dataset-tarik-a-rashid
**Extraido de: ** https://data.mendeley.com/datasets/wmhctcrt5v/1/files/959a4949-b1c2-4858-b361-2602bb60a07a
**Especificidad** una fila = un paciente
**total de filas:** 1309

---
## Descripcion de variables
En la exploracion del dataset `Medicaldataset.csv` se encontraron las siguientes columnas.

### Variables 
| Columna | Tipo | Descripción |
|---|---|---|
|Age|int64|La edad del paciente|
|Gender|int64|Sexo biológico del paciente (el masculino se establece en 1 y el femenino en 0)|
|Heart rate|int64|el número de latidos por minuto|
|Systolic blood pressure|int64| la presión en las arterias cuando el corazón se contrae|
|Diastolic blood pressure|int64| la presión en las arterias entre los latidos del corazón|
|Blood sugar|float64|el nivel de glucosa en sangre del paciente|
|CK-MB|float64|una enzima cardíaca liberada durante el daño del músculo cardíaco|
|Troponin|float64|un biomarcador proteico altamente específico para la lesión del músculo cardíaco|
|Result|int64|La etiqueta de resultado que indica si el paciente sufrió o no un ataque cardíaco|

---

## Resumen de analisis exploratorio

1. **Datos faltantes**
    - El conjunto de datos no posee datos faltantes, no contiene datos `NULL` o `NaN`
2. **Estandarizacion nombre de las variables**
    -Se realizo una estandarización en el nombre de las diferentes variables ejemplo `Heart rate` = `heart_rate` ó `Diastolic blood pressure` = `diastolic_bp`
3. **Duplicados** el conjunto de datos no posee filas dúplicadas

### Variable Objetivo

**`result`**: Esta es la variable que se desea predecir en el modelo de clasificación.

- Valores posibles: `"negative"` (negativo) o `"positive"` (positivo)
- Tipo: Categórica binaria
- Importancia: Variable objetivo del modelo de Machine Learning