# Python

## Anaconda

### ¿Qué es Anaconda?
Anaconda es una suite de código abierto que abarca una serie de aplicaciones, librerías y conceptos diseñados para el desarrollo de [ciencia de datos](https://es.wikipedia.org/wiki/Ciencia_de_datos) con Python. A grandes rasgos, Anaconda es una distribucción de Python que funciona como un gestor de entorno, un gestor de paquetes y que posee una colección de más de 720 paquetes de código abierto.

### Descargar Anaconda
La liga para su descarga se encuentra [aquí](https://www.anaconda.com/download/)

A continuación veremos la siguiente pantalla, en donde podemos elegir la versión para nuestro sistema operativo y la versión de Python a instalar. 

![alt text](https://github.com/pjcv89/Python/blob/master/imagenes/anaconda_instructions.png "Logo Title Text 1")

En nuestro caso, instalaremos **Python 3.6** y elegiremos la versión de sistema operativo que estemos utilizando. En el caso de Windows, elegimos **32-Bit Graphical Installer** mientras que para macOS elegimos **64-Bit Graphical Installer**.

### Instalar Anaconda

En este paso instalaremos la app en nuestro sistema. Ejecutamos el archivo que descargamos haciendo doble click, de la manera usual. Se abrirá un asistente típico de instalación. Seguiremos los pasos, podemos seleccionar instalación sólo para nuestro usuario, seleccionar la ruta en disco donde instalaremos y listo.

### Creando y gestionando ambientes virtuales

A grandes rasgos, un entorno virtual o ‘virtual environment’  es una carpeta en la que se encuentran los ejecutables de Python y las distintas versiones de las librerías que vayamos a usar. De este modo, podremos estar desarrollando varias aplicaciones con distintas versiones de las librerías, incluso del propio interprete de Python, gracias a los entornos virtuales.

Una explicación más detallada sobre este tema puede ser hallada en [este excelente blog](https://devnull.wordpress.com/2016/04/18/crear-entorno-virtual-bajo-condapython/).

En nuestro caso, crearemos un ambiente virtual que llamaremos **games**.
Para esto, ejecutaremos la siguiente instrucción en nuestra línea de comandos (**Terminal** si usamos macOS, o en **CMD** si usamos Windows).

```bash
conda create -n games python=3.6 anaconda
```

Una vez creado nuestro ambiente, el siguiente paso es activarlo para poder usarlo mediante la siguiente instrucción:

```bash
source activate games
```

A continuación utilizaremos el sistema de gestión de paquetes [pip](https://pypi.org/) para descargar dos librerías adicionales que necesitaremos para nuestros propósitos, a saber, [pyserial](https://github.com/pyserial/pyserial) y [pyFirmata](https://github.com/tino/pyFirmata) ejecutando la siguiente instrucción:

```bash
pip install pyserial msgpack pyfirmata
```

Cuando vayamos a dejar de utilizar el entorno, deberemos desactivarlo mediante la siguiente instrucción:

```bash
source deactivate games
```

