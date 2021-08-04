Autor: Arturo Mata <arturo.mata@gmail.com>
Script: ping.py
Version: 1.0.0
Repositorio: https://github.com/matarturo/
Released under the GNU General Public License WITHOUT ANY WARRANTY.
See LICENSE.TXT for details.

# Script de mantenimiento de logs de dispositivos firewalls bajo plataforma GNU/Linux

Es importante el mantenimiento periódico de estos equipos ya que los archivos logs del entorno GNU/Linux DebianOS 
crecen rápidamente y se pueden llenar los discos duros generando problemas de almacenamiento de información.

# Instalación

Para correr este script se requiere ingresar al equipo con credenciales de usuario < root >

$ cd /var/log
$ sudo git clone https://github.com/matarturo/scan_subnet.git
$ cd scan_subnet
$ sudo cp ping.py /var/log
$ cd /var/log

# Para otorgar permisos de ejecución

$ sudo chmod 755 ping.py

Aun en el directorio < var/log > se escribe la siguiente línea de código < ls -l > y se despliega la 
lista de los diferentes archivos contenido en la referida ubicación, se selecciona el script: 
mantenimiento.sh, un archivo ejecutable creado para la limpieza de los logs elegidos previamente, 
garantizando un registro histórico mínimo para casos de auditorías. Para editar el archivo  <.sh >, 
se deberá utilizar el comando <nano> que corresponde al editor de código nativo 
de Linux.

$ sudo nano ping.py  

# Ejecución del script

La ejecución el script se debe utilizar la notación < ./ > (punto-diagonal-slash), para que efectúe 
la búsqueda del script en el directorio actual en vez de ir a buscar en todos los directorios que 
aparecen en $PATH, de la siguiente manera < ./mantenimiento.sh >, dependiendo de la versión de Linux, 
solicitara el uso el comando < sudo > para ejecutar programas con los privilegios de seguridad de super usuario.

$ sudo python3 ping.py 

Cuando a aparezca en pantalla < ...MANTENIMIENTO FINALIZADO > , ya estará listo el procedimiento de mantenimiento de
los archivos logs, el paso siguiente es detener el proceso.

$ exit
