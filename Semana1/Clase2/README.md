# Configuración de Anaconda

La instalación y configuración puede ser un poco tediosa, pero, si se hace bien, servirá para siempre. Anaconda es una herramienta que permite manejar ambientes de manera flexible y modular. Python tiene dos versiones diferentes del lenguaje y muchas libreras tienen diferencias. Esto puede hace difícil que tu código funcione en otras computadoras. Anaconda hace fácil esto creando un ambiente en tu computadora y usando versiones especficas de estos paquetes. Lo único que se necesita saber para lograr esto es utilizar la terminal de tu sistema operativo (sólo vamos a correr unos cuántos comandos, nada complicado).

En el siguiente [link](https://www.continuum.io/downloads) se explica como instalar Anaconda para cualquier sistema operativo. No es necesario tener nada más instalado. Elige Python 3.6 (desde Anaconda podrás instalar otras versiones más adelante).

Una vez que hayas instalado Anaconda, sólo es necesario crear el ambiente

```
conda create -n curso-dl python=3.5
``` 

Finalmente, activamos el ambiente e instalamos libreras necesarias.

Mac o Linux: 

```source activate curso-dl```

Windows: 

```activate curso-dl```

Instalamos las librerías que vamos a estar utilizando
```
conda install numpy pandas jupyter notebook matplotlib
```


En este momento podemos correr el comando ```jupyter notebook``` en el directorio del archivo .ipynb, y este dará un enlace para abrir el cuaderno en cualquier navegador (se debe navegar a la carpeta donde está el cuaderno). Arriba a la derecha puedes descargar el cuaderno como zip.
