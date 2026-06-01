from datetime import datetime

# -------------------------------
# CLASE CLIENTE
# -------------------------------
class Cliente:
    def __init__(self, cedula, nombre, prioridad):
        self.cedula = cedula
        self.nombre = nombre
        self.prioridad = prioridad
        self.fecha = datetime.now()

    def __str__(self):
        return f"Cedula: {self.cedula} | Nombre: {self.nombre} | Prioridad: {self.prioridad} | {self.fecha.date()}"

# ------------------------------- 
# COLAS DE PRIORIDAD
# -------------------------------
alta=[]
media=[]
baja=[]

#===============
# HISTORIAL
#================
historial = []

#================
# REGISTRAR PACIENTE
#================
def registrar_paciente():
    cedula = input("Ingrese la cedula:")
    nombre = input("Ingrese el nombre:")
    prioridad = input("Prioridad (Alta, Media, Baja):").capitalize()
    
    paciente = Cliente(cedula, nombre, prioridad)
    
    if prioridad == "Alta":
        alta.append(paciente)
    elif prioridad == "Media":
        media.append(paciente)
    elif prioridad == "Baja":
        baja.append(paciente)
    else:
        print("Prioridad no valida.")
        return
    
    print("Paciente registrado correctamente.")
    print("Pacientes alta:",
    len(alta))
    print("Paciente media:",
    len(media))
    print("Paciente baja:",
    len(baja))
    
    
    
#========================
#MOSTRAR COLAS
#========================
def mostrar_colas():
    print("\n===== COLA ALTA =====")
    for paciente in alta:
        print(paciente)
            
    print("\n===== COLA MEDIA  =====")
    for paciente in media:
        print(paciente)
            
    print("\n===== COLA BAJA =====")
    for paciente in baja:
        print(paciente)
            
#======================
# VER SIGUIENTE PACIENTE
#======================

def ver_siguiente():
    if alta:
        print("Siguiente paciente:")
        print(alta[0])
        
    elif media:
        print("Siguiente paciente:")
        print(media[0])
        
    elif baja:
        print("siguiente paciente:")
        print((baja[0]))
            
    else:
        print("No hay paciente en espera.")
        
        
#================
# ATENDER PAIENTE
#================
def atender_paciente():
    
    if alta:
        paciente = alta.pop(0)
        
    elif media:
        paciente = media.pop(0)
        
    elif baja:
        paciente = baja.pop(0)
        
    else:
        print("No hay pacientes para atender.")
        return
    
    historial.append(paciente)
    
    print("Paciente atendido:")
    print(paciente)
    
#=====================
# MOSTRAR HISTORIAL
#=====================
def mostrar_historial():
    
    if not historial:
        print("No hay pacientes atendidos.")
        return
    
    print("\n======= HISTORIAL========")
    
    for paciente in historial:
        print(paciente)
        
#================
# MENU
#================
def menu():
    print("\n")
    print("=====SISTEMA DE GESTION DE TURNOS=====")
    print("1. Registrar paciente")
    print("2. Mostrar colas")
    print("3. Ver siguiente paciente")
    print("4. Atender paciente")
    print("5. Mostrar historial")
    print("6. Salir")
    
#======================
# PROGRAMA PRINCIPAL
#======================
while True:
    
    menu()
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        registrar_paciente()
    
    elif opcion == "2":
        print("OPCION 2 DETECTADA")
        mostrar_colas()
        
    elif opcion == "3":
        ver_siguiente()
        
    elif opcion == "4":
        atender_paciente()
        
    elif opcion == "5":
        mostrar_historial()
        
    elif opcion == "6":
        print("Programa finalizado.")
        break
    
    else:
        print("Opcion invalida.")  