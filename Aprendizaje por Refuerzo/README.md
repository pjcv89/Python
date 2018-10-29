# APRENDIZAJE POR REFUERZO

## Introducción

Imaginemos la siguiente situación. Un robot da un gran paso adelante, luego cae. La próxima vez, da un paso más pequeño y es capaz de mantener su equilibrio. El robot intenta diversas variaciones como esta muchas veces; finalmente, aprende el tamaño correcto de los pasos a seguir y camina de manera constante. Después de varios ensayos de prueba y error, ha tenido éxito.

La situación anterior es un ejemplo del llamado aprendizaje por refuerzo. En este marco, la acción del robot y el resultado que obtiene de dicha acción están directamente contectados. El robot aprende a caminar basándose en recompensas positivas y recompensas negativas (o castigos). En nuestro ejemplo del robot, la recompensa positiva se obtiene al mantener el equilibrio y el castigo se obtiene al caerse. Esta retroalimentación se considera "refuerzo" por hacer o no hacer una acción.

Ahora pongamos otro ejemplo, pero ahora uno basado más en seres vivos. ¿Cómo aprende un perro trucos nuevos como sentarse o tumbarse? Cada vez que lo hace bien, se le da un **premio**. Esa *premio* simplemente es un refuerzo positivo. A la larga, nuestra mascota aprenderá que hacer el truco bien tiene una recompensa. La idea se puede extender a los algoritmos que aprenden de forma automática. Tenemos que dar a nuestros algoritmos *premios* digitales.

<p align="center">
  <img width="460" height="300" src="https://misanimales.com/wp-content/uploads/2015/06/galleta-perro.jpg">
</p>

Exploremos esta idea con un juego: el 3 en línea o juego del gato . Si tenemos un algoritmo que aprende por refuerzo, podríamos ofrecer un refuerzo positivo cada vez que el algoritmo gana. La idea básica del aprendizaje por refuerzo es probar a realizar movimientos y observar el refuerzo que proporcionan.

No es difícil para un algoritmo aprender qué movimientos concretos ganan la partida. Por ejemplo, supongamos que el tablero tiene dos X en línea y la siguiente casilla en la misma línea está vacía. El algoritmo se enfrentará a esta situación múltiples veces, y si prueba diferentes movimientos cada vez, después de algunas pruebas el algoritmo descubrirá que poner una X en la casilla que forma una línea garantiza un refuerzo positivo. Vemos que el refuerzo no sólo depende de la acción que se realiza, sino también del estado en que se encuentra el tablero antes de realizar esa acción, porque poner la X en esa casilla en otros momentos de la partida no gana la partida.

<p align="center">
  <img width="700" height="300" src="https://rubenlopezg.files.wordpress.com/2015/05/reinforcement1.png">
</p>


<p align="center">
  <img width="700" height="700" src="https://rubenlopezg.files.wordpress.com/2015/05/direct_reward1.png">
</p>


<p align="center">
  <img width="400" height="200" src="https://rubenlopezg.files.wordpress.com/2015/05/direct_reward_win.png">
</p>

<p align="center">
  <img width="400" height="200" src="https://rubenlopezg.files.wordpress.com/2015/05/direct_reward_int.png">
</p>

<p align="center">
  <img width="400" height="200" src="https://rubenlopezg.files.wordpress.com/2015/05/experience1.png">
</p>
