from datetime import datetime

# -------------------------------
# CLASE CLIENTE
# -------------------------------
class Cliente:
    def __init__(self, cedula, nombre, tipo_atencion, prioridad, fecha):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_atencion = tipo_atencion
        self.prioridad = prioridad
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")

    def __str__(self):
        return f"{self.nombre} | {self.tipo_atencion} | {self.prioridad} | {self.fecha.date()}"

# -------------------------------
# PILA (para urgentes extracción)
# -------------------------------
class Pila:
    def __init__(self):
        self.items = []

    def push(self, cliente):
        self.items.append(cliente)

    def pop(self):
        if not self.vacia():
            return self.items.pop()
        return None

    def vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("\n--- PILA DE URGENCIAS (Extracción) ---")
        for cliente in reversed(self.items):
            print(cliente)

# -------------------------------
# COLA (atención diaria)
# -------------------------------
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, cliente):
        self.items.append(cliente)

    def dequeue(self):
        if not self.vacia():
            return self.items.pop(0)
        return None

    def vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("\n--- COLA DE ATENCIÓN DIARIA ---")
        for cliente in self.items:
            print(cliente)

# -------------------------------
# DATOS DE PRUEBA
# -------------------------------
clientes = [
    Cliente("1", "Ana", "Extraccion", "Urgente", "2026-04-27"),
    Cliente("2", "Luis", "Limpieza", "Normal", "2026-04-28"),
    Cliente("3", "Carlos", "Extraccion", "Urgente", "2026-04-26"),
    Cliente("4", "Maria", "Extraccion", "Normal", "2026-04-29"),
    Cliente("5", "Sofia", "Extraccion", "Urgente", "2026-04-25"),
]

# -------------------------------
# CREAR PILA (filtrar y ordenar)
# -------------------------------
pila = Pila()

# Filtrar
urgentes = [c for c in clientes if c.tipo_atencion == "Extraccion" and c.prioridad == "Urgente"]

# Ordenar por fecha (más cercana primero)
urgentes.sort(key=lambda x: x.fecha)

# Insertar en pila
for cliente in urgentes:
    pila.push(cliente)

# Mostrar pila
pila.mostrar()

# -------------------------------
# CREAR COLA (agenda diaria)
# -------------------------------
cola = Cola()

for cliente in clientes:
    cola.enqueue(cliente)

cola.mostrar()

# -------------------------------
# ATENDER CLIENTES (COLA)
# -------------------------------
print("\n--- ATENDIENDO CLIENTES ---")
while not cola.vacia():
    atendido = cola.dequeue()
    print(f"Atendiendo a: {atendido.nombre}")