# Sistema de Gestión de Turnos Hospitalarios

## Descripción del Proyecto

Este proyecto consiste en un sistema de gestión de turnos para pacientes de un centro médico desarrollado en Python. El programa permite registrar pacientes, organizarlos según su nivel de prioridad y gestionar su atención de manera eficiente.

El sistema utiliza estructuras de datos tipo cola para administrar el orden de atención de los pacientes, garantizando que aquellos con prioridad alta sean atendidos antes que los de prioridad media y baja.

---

## Objetivo

Implementar un sistema de turnos que permita:

* Registrar pacientes.
* Clasificar pacientes por nivel de prioridad.
* Consultar el siguiente paciente a atender.
* Atender pacientes respetando la prioridad.
* Mantener un historial de pacientes atendidos.

---

## Estructura del Programa

### Clase Cliente

La clase `Cliente` representa a cada paciente registrado en el sistema.

#### Atributos

| Atributo  | Descripción                             |
| --------- | --------------------------------------- |
| cedula    | Identificación del paciente             |
| nombre    | Nombre completo del paciente            |
| prioridad | Nivel de prioridad (Alta, Media o Baja) |
| fecha     | Fecha y hora de registro                |

#### Método especial

`__str__()`

Permite mostrar la información del paciente de forma legible cuando se imprime en pantalla.

---

## Estructuras de Datos

El sistema utiliza tres colas independientes:

```python
alta = []
media = []
baja = []
```

Cada lista almacena los pacientes según su prioridad.

Además, se utiliza una lista adicional:

```python
historial = []
```

para guardar los pacientes que ya fueron atendidos.

---

## Funcionamiento Paso a Paso

### 1. Registro de Pacientes

Función:

```python
registrar_paciente()
```

Proceso:

1. Solicita la cédula.
2. Solicita el nombre.
3. Solicita la prioridad.
4. Crea un objeto de tipo Cliente.
5. Almacena el paciente en la cola correspondiente.
6. Muestra un mensaje de confirmación.

Ejemplo:

```text
Ingrese la cedula: 123
Ingrese el nombre: Tatiana
Prioridad (Alta, Media, Baja): Alta
```

Resultado:

```text
Paciente registrado correctamente.
```

---

### 2. Mostrar Colas

Función:

```python
mostrar_colas()
```

Proceso:

1. Recorre la cola de prioridad alta.
2. Recorre la cola de prioridad media.
3. Recorre la cola de prioridad baja.
4. Muestra todos los pacientes registrados en cada una.

Ejemplo:

```text
===== COLA ALTA =====
Cedula: 123 | Nombre: Abelardo | Prioridad: Alta

===== COLA MEDIA =====

===== COLA BAJA =====
```

---

### 3. Ver Siguiente Paciente

Función:

```python
ver_siguiente()
```

Proceso:

1. Verifica si existen pacientes en la cola alta.
2. Si existe alguno, muestra el primero.
3. Si la cola alta está vacía, revisa la media.
4. Si la media está vacía, revisa la baja.
5. Si todas están vacías, informa que no hay pacientes en espera.

---

### 4. Atender Paciente

Función:

```python
atender_paciente()
```

Proceso:

1. Busca pacientes en la cola alta.
2. Si existe alguno, lo retira de la cola.
3. Si no hay pacientes de prioridad alta, busca en media.
4. Si tampoco hay, busca en baja.
5. El paciente atendido se agrega al historial.
6. Muestra los datos del paciente atendido.

Ejemplo:

```text
Paciente atendido:
Cedula: 123 | Nombre: Juan Pérez | Prioridad: Alta
```

---

### 5. Mostrar Historial

Función:

```python
mostrar_historial()
```

Proceso:

1. Verifica si existen pacientes atendidos.
2. Recorre la lista historial.
3. Muestra la información de cada paciente atendido.

Ejemplo:

```text
======= HISTORIAL =======
Cedula: 123 | Nombre: Juan Pérez | Prioridad: Alta
```

---

## Menú Principal

El sistema funciona mediante un menú interactivo:

```text
===== SISTEMA DE GESTION DE TURNOS =====

1. Registrar paciente
2. Mostrar colas
3. Ver siguiente paciente
4. Atender paciente
5. Mostrar historial
6. Salir
```

Cada opción ejecuta una función específica del sistema.

---

## Lógica de Prioridades

El sistema respeta el siguiente orden de atención:

1. Prioridad Alta.
2. Prioridad Media.
3. Prioridad Baja.

Esto significa que un paciente de prioridad alta siempre será atendido antes que uno de prioridad media o baja, independientemente del momento en que hayan sido registrados.

---

## Ejemplo de Ejecución

```text
Seleccione una opcion: 1

Ingrese la cedula: 1001
Ingrese el nombre: Maria Lopez
Prioridad (Alta, Media, Baja): Alta

Paciente registrado correctamente.

Seleccione una opcion: 3

Siguiente paciente:
Cedula: 1001 | Nombre: Maria Lopez | Prioridad: Alta

Seleccione una opcion: 4

Paciente atendido:
Cedula: 1001 | Nombre: Maria Lopez | Prioridad: Alta

Seleccione una opcion: 5

======= HISTORIAL =======
Cedula: 1001 | Nombre: Maria Lopez | Prioridad: Alta
```

---

## Conclusiones

El sistema desarrollado permite gestionar turnos hospitalarios de forma organizada utilizando colas de prioridad. La implementación demuestra el uso de clases, listas, funciones, estructuras condicionales y ciclos en Python, facilitando la administración eficiente de pacientes y garantizando una atención basada en niveles de urgencia.


#  ANEXO

LINK DE DESCARGA VIDEO 
https://drive.google.com/drive/folders/1L72w2rs_iDeuz9U9_3hMzq5gMPNXOQX9?usp=sharing
