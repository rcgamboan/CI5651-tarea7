# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 7. Ejercicio 2

# Basado en la implementacion del algoritmo Graham Scan
# hallada en https://www.geeksforgeeks.org/convex-hull-using-graham-scan/


from functools import cmp_to_key

# Clase para almacenar las coordenadas de cada punto
class Point:
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y
	
	def __str__(self) -> str:
		return f"({self.x}, {self.y})"

# Funcion para hallar la distancia al cuadrado entre dos puntos
def distSq(p1, p2):
	return ((p1.x - p2.x) * (p1.x - p2.x) +
			(p1.y - p2.y) * (p1.y - p2.y))

# Funcion para calcular la orientacion de un conjunto de tres puntos
# Se calcula el producto cruz entre p1-p2 y p2-p3
# Si el resultado es 0, los puntos son colineales
# Si el resultado es positivo, los puntos se encuentran en sentido horario
# Si el resultado es negativo, los puntos se encuentran en sentido antihorario
def orientation(p1, p2, p3):
	val = ((p2.y - p1.y) * (p3.x - p2.x) -
		(p2.x - p1.x) * (p3.y - p2.y))
	if val == 0:
		return 0
	elif val > 0:
		return 1
	else:
		return 2

# Funcion para ordenar los puntos segun su orientacion
def compare(p1, p2):
	p0 = Point(0, 0)
	orientacion = orientation(p0, p1, p2)
	if orientacion == 0:
		if distSq(p0, p2) >= distSq(p0, p1):
			return -1
		else:
			return 1
	else:
		if orientacion == 2:
			return -1
		else:
			return 1

# Funcion para hallar la capa convexa de un conjunto de puntos
# Incialmente se halla el punto con la coordenada y mas baja,
# ya que este punto siempre pertenecera a la capa convexa
# Luego se ordenan los puntos segun su orientacion respecto al punto inicial hallado previamente,
# Al ordenar los puntos, se puede obtener un camino cerrado entre ellos,
# Luego se recorre el conjunto de puntos, y se van agregando a la capa convexa
# aquellos que tengan orientacion antihoraria respecto a los dos ultimos puntos agregados
def convexHull(points, n):

	# Punto con la coordenada y menor
	# recorriendo el conjunto de puntos
	# en caso de empate, se escoge el punto con la coordenada x menor
	ymin = points[0].y
	min = 0
	for i in range(1, n):
		y = points[i].y

		if ((y < ymin) or
			(ymin == y and points[i].x < points[min].x)):
			ymin = points[i].y
			min = i

	# Se coloca el punto con la coordenada y mas baja en la primera posicion
	# en el arreglo de puntos
	points[0], points[min] = points[min], points[0]


	# Se ordenan los puntos segun su orientacion respecto al punto inicial
	# un punto p1 viene antes que un punto p2 en la salida ordenada si p2
	# tiene un angulo polar mayor que p1 (en sentido antihorario).
	p0 = points[0]
	points = sorted(points, key=cmp_to_key(compare))

	# Si varios puntos tienen el mismo angulo respecto a p0,
	# se eliminan todos menos el que este mas lejos de p0

	# Contador para la cantidad de puntos que pueden ser parte
	# de la capa convexa
	m = 1
	for i in range(1, n):
	
		# Se recorren los puntos y se eliminan aquellos que sean colineales
		while ((i < n - 1) and (orientation(p0, points[i], points[i + 1]) == 0)):
			i += 1

		points[m] = points[i]
		m += 1

	# Si la cantidad de puntos que pueden ser parte de la capa convexa
	# es menor a 3, no se puede formar una capa convexa
	if m < 3:
		return

	# Se agregan los primeros tres puntos a la capa convexa
	S = []
	S.append(points[0])
	S.append(points[1])
	S.append(points[2])

	# Se procesan los puntos restantes
	for i in range(3, m):
		
		# Se elimina el tope de la pila mientras el angulo
		# formado por los puntos no forme un giro a la izquierda
		while ((len(S) > 1) and
		(orientation(S[-2], S[-1], points[i]) != 2)):
			S.pop()
		S.append(points[i])

	# Los puntos restantes en el arreglo S forman la capa convexa
	return S

if __name__ == "__main__":
	input_points = [(0, 3), (1, 1), (2, 2), (4, 4),
					(0, 0), (1, 2), (3, 1), (3, 3)]
	points = set()
	for point in input_points:
		points.add(Point(point[0], point[1]))

	for i in range(len(input_points)):
		
		print(f"\nConjunto de puntos P{i}:")
		for p in points:
			print(p)

		print(f"\nCapa {i} formada por los puntos en P{i}:")
		capa = convexHull(list(points), len(points))
		# No se pudo formar una capa convexa
		if not capa:
			break
		
		for p in capa:
			print(p)
		
		# Remover del conjunto de puntos los puntos que forman la capa
		points.difference_update(set(capa))
		# Si la cantidad de puntos restantes es menor o igual a 3, no se puede formar una capa convexa
		if len(points) <= 3:
			break
