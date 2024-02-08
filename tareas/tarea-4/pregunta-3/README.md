# Tarea 4 - Pregunta 3

Cliente para probar el proceso de inicializacion virtual de arreglos.

## Instrucciones de uso

### Ejecutar el cliente:

Compile el cliente con el comando `make` y luego ejecute el cliente con el comando `./cliente <n>`, donde `<n>` es el tamaño del arreglo virtual.

### Ejemplo de uso

```bash
Bienvenido al CLI para probar el proceso de inicializacion virtual de arreglos.

Comandos disponibles:
  - 'ASIGNAR POS VAL' para asignar el valor VAL en la posicion POS.
  - 'CONSULTAR POS' para cosultar POS.
  - 'LIMPIAR' para limpiar la tabla.
  - 'SALIR' para salir.

> Introduzca un comando: CONSULTAR 0
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 1
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 2
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 3
Error: Posicion invalida.

> Introduzca un comando: ASIGNAR 0 10
Asignando 10 en la posicion 0 ...

> Introduzca un comando: ASIGNAR 0 20
Asignando 20 en la posicion 0 ...

> Introduzca un comando: CONSULTAR 0
Posicion 0 inicializada, y contiene 20.

> Introduzca un comando: ASIGNAR 0 30
Asignando 30 en la posicion 0 ...

> Introduzca un comando: ASIGNAR 0 40
Asignando 40 en la posicion 0 ...

> Introduzca un comando: CONSULTAR 0
Posicion 0 inicializada, y contiene 40.

> Introduzca un comando: ASIGNAR 1 100
Asignando 100 en la posicion 1 ...

> Introduzca un comando: ASIGNAR 2 100
Asignando 100 en la posicion 2 ...

> Introduzca un comando: ASIGNAR 2 1000
Asignando 1000 en la posicion 2 ...

> Introduzca un comando: CONSULTAR 0
Posicion 0 inicializada, y contiene 40.

> Introduzca un comando: CONSULTAR 1
Posicion 1 inicializada, y contiene 100.

> Introduzca un comando: CONSULTAR 2
Posicion 2 inicializada, y contiene 1000.

> Introduzca un comando: CONSULTAR 3
Error: Posicion invalida.

> Introduzca un comando: LIMPIAR

> Introduzca un comando: CONSULTAR 0
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 1
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 2
Posicion no inicializada.

> Introduzca un comando: ASIGNAR 2 2000
Asignando 2000 en la posicion 2 ...

> Introduzca un comando: CONSULTAR 0
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 1
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 2
Posicion 2 inicializada, y contiene 2000.

> Introduzca un comando: ASIGNAR 0 2
Asignando 2 en la posicion 0 ...

> Introduzca un comando: ASIGNAR 1 20
Asignando 20 en la posicion 1 ...

> Introduzca un comando: CONSULTAR 0
Posicion 0 inicializada, y contiene 2.

> Introduzca un comando: CONSULTAR 1
Posicion 1 inicializada, y contiene 20.

> Introduzca un comando: CONSULTAR 2
Posicion 2 inicializada, y contiene 2000.

> Introduzca un comando: LIMPIAR

> Introduzca un comando: CONSULTAR 0
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 1
Posicion no inicializada.

> Introduzca un comando: CONSULTAR 2
Posicion no inicializada.

> Introduzca un comando: SALIR
```
