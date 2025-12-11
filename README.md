# Hilos - Demostración de Threading en Python

## Descripción

Este repositorio contiene una demostración práctica de la diferencia entre **ejecución secuencial** y **ejecución con hilos (threads)** en Python, utilizando un ejemplo divertido de tareas de superhéroe.

## ¿Qué es Threading?

El **threading** (multihilo) es una técnica de programación que permite ejecutar múltiples tareas de forma concurrente dentro del mismo proceso. En lugar de esperar que una tarea termine para comenzar la siguiente, los hilos permiten que varias tareas se ejecuten "al mismo tiempo".

## Dinámica del Proyecto

### Escenario: Superhéroe al Rescate 🦸‍♂️

El proyecto simula tres tareas heroicas que un superhéroe debe realizar:

1. **Detener un auto** 🚗 - 7 segundos
2. **Congelar un incendio** 🔥 - 13 segundos  
3. **Sostener un balcón** 🏢 - 10 segundos

### Comparación de Métodos

#### 🐌 Ejecución Secuencial
- Las tareas se ejecutan una tras otra
- **Tiempo total**: ~30 segundos (7 + 13 + 10)
- El superhéroe debe completar una tarea antes de comenzar la siguiente

#### ⚡ Ejecución con Threads
- Las tareas se ejecutan en paralelo
- **Tiempo total**: ~13 segundos (tiempo de la tarea más larga)
- El superhéroe puede realizar las tres tareas simultáneamente

## Archivos del Proyecto

- `theadring.py` - Código principal con ambas implementaciones
- `not_theadring.py` - (archivo adicional en el repositorio)
- `README.md` - Este archivo de documentación

## Cómo Ejecutar

```bash
python theadring.py
```

## Salida Esperada

```
You have stopped a speeding car before it reaches a crowded crosswalk
You have freezed a fire to protect a family inside a house
You have held a collapsing balcony and everyone has escaped safely
------------------------------------------------------------
Execution time in sequence: 30.XX seconds
------------------------------------------------------------

[Tareas ejecutándose simultáneamente con threads]
All chores are complete. You are the best!
------------------------------------------------------------
Execution time using threads: 13.XX seconds
------------------------------------------------------------
```

## Conceptos Clave

### `threading.Thread()`
- Crea un nuevo hilo de ejecución
- `target` especifica la función a ejecutar
- `start()` inicia la ejecución del hilo

### `join()`
- Hace que el programa principal espere a que termine el hilo
- Garantiza que todas las tareas se completen antes de continuar

## Ventajas del Threading

✅ **Mejor rendimiento** para tareas I/O intensivas  
✅ **Mejor experiencia de usuario** (no bloquea la interfaz)  
✅ **Aprovechamiento de recursos** cuando hay esperas  

## Cuándo Usar Threading

- Operaciones de archivo
- Solicitudes de red
- Tareas con esperas (como `time.sleep()`)
- Interfaces de usuario que no deben bloquearse

## Nota Importante

Este ejemplo usa `time.sleep()` para simular tareas que toman tiempo. En aplicaciones reales, esto podría ser lectura de archivos, llamadas a APIs, consultas a bases de datos, etc.

---

**¡Conviértete en un superhéroe de la programación dominando los hilos!** 🚀