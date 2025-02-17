# Juego de Piedra, Papel o Tijeras
Este es un simple juego de Piedra, Papel o Tijeras que permite al jugador jugar de dos maneras:
- Contra la computadora.
- En modo multijugador entre dos personas.
## Descripción
El juego está basado en el famoso juego de mesa "Piedra, Papel o Tijeras". Cada jugador elige una de las tres opciones disponibles y se determina un ganador según las reglas clásicas:
- Piedra gana a Tijeras.
- Tijeras gana a Papel.
- Papel gana a Piedra.
- Si ambos jugadores eligen lo mismo, el resultado es un empate.
## Características
- Jugar contra la computadora: El jugador elige su opción y la computadora elige aleatoriamente.
- Modo multijugador: Dos jugadores eligen sus opciones en privado (utilizando getpass para ocultar las elecciones) y se compara el resultado.
- Ver estadísticas: Después de cada partida, puedes ver las estadísticas de la última partida jugada.
## Requisitos
Este juego está escrito en Python y necesita tener instalado Python 3.x. No requiere bibliotecas externas aparte de las estándar.

## Cómo ejecutar el juego
1. Asegúrate de tener Python 3 instalado. Si no lo tienes, puedes descargarlo desde https://www.python.org/downloads/.

2. Guarda el código en un archivo llamado piedra_papel_tijeras.py.

3. Abre una terminal o línea de comandos.

4. Navega hasta la carpeta donde guardaste el archivo.


## Uso del juego
El menú principal tiene las siguientes opciones:

1. Jugar contra la computadora: Te permitirá jugar una partida contra la computadora. La computadora elegirá una opción aleatoria y el juego determinará el ganador.

2. Jugar multijugador: Dos jugadores pueden elegir sus opciones. Se ocultan las elecciones para que los jugadores no puedan ver lo que el otro elige. El juego determinará el ganador entre los dos jugadores.

3. Ver estadísticas de la última partida: Después de cada juego, podrás ver un resumen con el modo de juego, las elecciones de cada jugador y el resultado.

4. Salir: Termina el juego.

## Entrada del jugador
Cuando se te pida que elijas una opción, debes seleccionar uno de los siguientes números:
1. Piedra
2. Papel
3. Tijeras
En el modo multijugador, las opciones de los jugadores están ocultas utilizando la función getpass para asegurar que las elecciones de cada jugador no se vean.

## Ejemplo de una partida
Elige el modo de juego. Ejemplo: Jugar contra la computadora.
El jugador elige su opción. Ejemplo: Piedra.
La computadora elige aleatoriamente. Ejemplo: Papel.
El juego muestra el resultado, por ejemplo: "Jugador 1 gana" si la computadora elige Tijeras, o "Computadora gana" si la computadora elige Papel.
## Estadísticas
Al finalizar una partida, puedes ver el siguiente resumen de la última partida:
- Modo de juego: Multijugador o Computadora.
- Elecciones de los jugadores.
- Resultado de la partida: Empate, Jugador 1 gana, o Jugador 2 gana.
## Estructura del Código
####  Funciones principales
- obtener_opcion(mensaje, ocultar): Permite al jugador elegir una opción, con la posibilidad de ocultar la entrada (usado en el modo multijugador).

- determinar_ganador(opcion1, opcion2): Determina el ganador de la partida según las reglas de Piedra, Papel o Tijeras.

- jugar_contra_computadora(): Función que permite al jugador jugar contra la computadora.

- jugar_multijugador(): Función que permite dos jugadores elegir sus opciones y determina el ganador.

- ver_estadisticas(): Muestra las estadísticas de la última partida.

- menu(): Muestra el menú principal y gestiona las opciones del juego.

## Posibles Mejoras
- Se podría agregar un sistema de puntuaciones para hacer un seguimiento del rendimiento de los jugadores en varias partidas.
- Agregar más modos de juego o diferentes reglas (por ejemplo, Piedra, Papel, Tijeras, Lagarto, Spock).
- Implementar un modo de torneo donde varios jugadores compiten entre sí en rondas consecutivas.
