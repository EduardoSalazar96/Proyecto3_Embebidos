# Sistema de detección del distanciamiento social

Este repositorio cuenta con dos directorios principales. Uno de ellos es el meta-distancia, el cual tiene adentro las
receta del código fuente de detención del distanciamiento social, el archivo de ejecución, asi como los modelos de entrenamiento y pesos. Además cuenta con layer 
de configuración de la receta.

El segundo directorio es la carpeta de construcción o build llamada pro3. Esta tiene adentro los archivos de configuración
necesarios, así como las dependecias que se necesitan para la generación de una imagen personalizada utilizando el flujo 
del Yocto Project para un "target" de raspberrypi2.

Este repositorio también cuenta con dos archivos de python, uno es la interfaz de usuario para el control de la aplicación en python3.
Así como la aplicación de mensajesaria para el bot telegram.

Se necesitan seguir los siguientes pasos si se desea hacer uso de este repositorio:

	1. Clonar poky-warrior: git clone -b warrior git://git.yoctoproject.org/poky.git
	2. Clonar el repositorio de meta-raspberry dentro de la carpeta poky-warrior: git clole -b warrior git://git.yoctoproject.org/meta-raspberrypi
	3. Clonar el master de este repositorio dentro de la carpeta poky-warrior y al mismo nivel de meta-raspberrypi: git clone https://github.com/kendallguido/Proyecto2_Embebidos.git
	4. Abrir una terminal dentro de carpeta poky-warrior y ejecutar el siguiente comando: source oe-init-build-env pro3/
	5. Correr el siguiente comando devtool add https://files.pythonhosted.org/packages/b5/94/46dcae8c061e28be31bcaa55c560cb30ee9403c9a4bb2659768ec1b9eb7d/imutils-0.5.3.tar.gz
	   Esto es para agregar la biblioteca de imutils a la receta de imagen en Yocto Project 	
	6. Ejecutar el comando: bitbake core-image-sato

Nota: Se deben hacer los cambios pertinentes al archivo bblayers dentro de la carpeta conf con las direcciones absolutas de las carpetas de los layers.
