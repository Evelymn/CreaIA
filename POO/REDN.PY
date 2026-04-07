from sklearn.neural_network import MLPClassifier
# Datos de entrada: [edad, ingreso_mensual, visitas]
x = [
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
# Salida: 0 = no compra, 
# 1 = compra
y = [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
# Crear el modelo — Cree usted el modelo necesario
# (MLPClassifier con parámetros apropiados)
modelo = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000, random_state=42)
# Entrenar el modelo — Cree el código necesario para entrenar el modelo
modelo.fit (x, y)
prediccion = modelo.predict([[24, 3,500, 3]])
prediccion = modelo.predict([[42, 8,200, 10]])
prediccion = modelo.predict([[21, 2,600, 1]])
# Predicciones de prueba — Con estos datos:
# - 24 años, Q3,500 y 3 visitas al sitio web en la última semana
# - 42 años, Q8,200 y 10 visitas al sitio web en la última semana
# - 21 años, Q2,600 y 1 visita al sitio web en la última semana
print("Predicción para [29, 4800, 5]:", modelo.predict([[29, 4800, 5]]))