#importar librerias.

import time
from collections import deque

# Clase Proceso

class Proceso:
    def __init__(self, id, tiempo_irrupcion, prioridad_alerta, tamaño_datos):
        self.id = id
        self.tiempo_irrupcion = tiempo_irrupcion
        self.tiempo_restante = tiempo_irrupcion
        self.prioridad_alerta = prioridad_alerta
        self.tamaño_datos = tamaño_datos
        self.estado = "Nuevo"

    def __str__(self):
        return f"Proceso {self.id} | Estado: {self.estado} | Restante: {self.tiempo_restante}"


# Algoritmo Round Robin, distribuir equitativamente la CPU

def round_robin(procesos, quantum):
    print("\n--- Simulación Round Robin ---\n")
    cola = deque(procesos)
    for p in cola:
        p.estado = "Listo"
    while cola:
        proceso = cola.popleft()
        proceso.estado = "En ejecución"
        print(proceso)
        tiempo_ejecucion = min(quantum, proceso.tiempo_restante)
        proceso.tiempo_restante -= tiempo_ejecucion
        time.sleep(0.5)
        if proceso.tiempo_restante > 0:
            proceso.estado = "Listo"
            cola.append(proceso)
        else:
            proceso.estado = "Terminado"
            print(f"Proceso {proceso.id} terminado.\n")


# Algoritmo que prioriza los procesos por prioridad

def prioridad(procesos):
    print("\n--- Simulación por Prioridad ---\n")
    procesos_ordenados = sorted(procesos, key=lambda x: x.prioridad_alerta)

    for proceso in procesos_ordenados:
        proceso.estado = "Listo"
        print(proceso)

        proceso.estado = "En ejecución"
        while proceso.tiempo_restante > 0:
            proceso.tiempo_restante -= 1
            print(proceso)
            time.sleep(0.3)

        proceso.estado = "Terminado"
        print(f"Proceso {proceso.id} terminado.\n")


# Creación de procesos SIGET

p1 = Proceso("Rutinario", 5, 2, 345)  # Datos rutinarios
p2 = Proceso("Alerta Incidente", 3, 1, 150)  # Emergencia
p3 = Proceso("alto Trafico", 7, 3, 660)  # Alto trafico

procesos = [p1, p2, p3]

# Ejecutar el primer algoritmo
round_robin(procesos, quantum=2)

# Reiniciar tiempos para el segundo algoritmo, en este caso, ejecutar el algoritmo de prioridad
p1.tiempo_restante = p1.tiempo_irrupcion
p2.tiempo_restante = p2.tiempo_irrupcion
p3.tiempo_restante = p3.tiempo_irrupcion

prioridad(procesos)