from sklearn.neural_network import MLPClassifier

# Datos de entrada: [edad, ingreso_mensual, visitas]
X = [
    [18, 2500, 2],
    [22, 3000, 3],
    [25, 4000, 5],
    [28, 4500, 6],
    [35, 7000, 8],
    [40, 8000, 9],
    [45, 8500, 10],
    [50, 9000, 12],
    [23, 2800, 1],
    [30, 5000, 4],
    [38, 7500, 7],
    [27, 4200, 2]
]

# Salida: 0 = no compra, 1 = compra
y = [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]

# Crear modelo
modelo = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000, random_state=1)

# Entrenar modelo
modelo.fit(X, y)

# Predicciones de prueba (las del ejercicio)
print("Predicción [24, 3500, 3]:", modelo.predict([[24, 3500, 3]]))
print("Predicción [42, 8200, 10]:", modelo.predict([[42, 8200, 10]]))
print("Predicción [21, 2600, 1]:", modelo.predict([[21, 2600, 1]]))

# 🔹 3 nuevas predicciones (las que te piden)
print("Predicción [29, 4800, 5]:", modelo.predict([[29, 4800, 5]]))
print("Predicción [33, 6000, 6]:", modelo.predict([[33, 6000, 6]]))
print("Predicción [19, 2200, 1]:", modelo.predict([[19, 2200, 1]]))

# 🔹 Nueva variable: tiempo promedio en el sitio
X_nuevo = [
    [20, 3000, 2, 5],
    [26, 4200, 4, 7],
    [31, 5500, 6, 10],
    [45, 8000, 9, 12],
    [23, 2800, 1, 3],
    [37, 7200, 7, 11]
]

y_nuevo = [0, 1, 1, 1, 0, 1]

# Entrenar modelo con nueva variable
modelo.fit(X_nuevo, y_nuevo)

# Predicción con nueva variable
print("Predicción con nueva variable [30, 5000, 5, 8]:", modelo.predict([[30, 5000, 5, 8]]))