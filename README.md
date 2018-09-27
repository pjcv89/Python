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

A continuación descargaremos el sistema de gestión de paquetes [pip](https://pypi.org/) con la siguiente instrucción 

```bash
conda install pip
```

para posteriormente descargar dos librerías adicionales que necesitaremos para nuestros propósitos, a saber: 

1. [pyserial](https://github.com/pyserial/pyserial): Nos permitirá emplear de forma sencilla el [puerto serie](https://es.wikipedia.org/wiki/Puerto_serie) para enviar información de nuestros programas (_software_) hacia nuestra tarjeta (_hardware_).

2. [pyFirmata](https://github.com/tino/pyFirmata): Es una interfaz en Python para el protocolo Firmata, el cual es un protocolo genérico para la comunicación con microcontroladores desde software instalado en un ordenador. Este protocolo se puede implementar en cualquier arquitectura de microcontroladores, así como en cualquier paquete de software. En nuestro caso, nuestro objetivo principal es permitir controlar completamente Arduino desde software instalado en nuestra computadora, sin escribir una sola línea de código de Arduino.

Descargamos estas dos librerías ejecutando la siguientes instrucción:


```bash
pip install pyserial msgpack pyfirmata
```

Cuando vayamos a dejar de utilizar el entorno, deberemos desactivarlo mediante la siguiente instrucción:

```bash
source deactivate games
```

## Jupyter Notebooks

### ¿Qué es Jupyter?

Jupyter Notebook, o simplemente Jupyter, es un entorno de trabajo interactivo que permite desarrollar código en Python (y algunos otros lenguajes) de manera dinámica, a la vez que integrar en un mismo documento tanto bloques de código como texto, gráficas o imágenes. 

La forma tradicional de correr un programa en Python es con el comando `python nombre.py`, donde **nombre.py** es un archivo con código de Python. Adicional a eso, para este curso utilizaremos un servidor de Jupyter Notebook con cuadernos de código. Estos cuadernos (_notebooks_) nos permiten combinar texto y código, organizados en celdas, lo cual es más cómodo para probar cosas nuevas y documentar lo que hacemos. El servidor de cuadernos se inicia ejecutando:

```bash
jupyter notebook
```

