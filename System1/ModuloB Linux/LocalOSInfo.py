import platform
import os

output_file_path = "infoMaquina.txt"

# Redirigir la salida estándar a un archivo txt
with open(output_file_path, 'w') as f:
    # Información general de la máquina
    f.write("---------------------------------\n")
    f.write("INICIO DE LOS DATOS GENERALES DE LA MÁQUINA\n")
    f.write("Arquitectura de la máquina: " + platform.machine() + "\n")
    f.write("Nombre del host: " + platform.node() + "\n")
    f.write("Sistema Operativo: " + platform.platform() + "\n")
    f.write("Nombre del procesador: " + platform.processor() + "\n")
    f.write("Versión del sistema: " + platform.release() + "\n")
    f.write("Versión del kernel: ")
    f.write(os.popen("uname -v").read() + "\n")

    f.write("FIN DE LOS DATOS GENERALES DE LA MÁQUINA\n")
    f.write("---------------------------------\n")

    # Información del hardware
    f.write("INICIO DE LOS DATOS DE HARDWARE DE LA MÁQUINA\n")
    f.write(os.popen("lshw -short").read() + "\n")

    f.write("FIN DE LOS DATOS DE HARDWARE DE LA MÁQUINA\n")
    f.write("---------------------------------\n")

    # Información de la CPU
    f.write("INICIO DE LOS DATOS GENERALES DE LA CPU\n")
    f.write(os.popen("lscpu").read() + "\n")
    f.write("FIN DE LOS DATOS GENERALES DE LA CPU\n")
    f.write("---------------------------------\n")

    # Información de los dispositivos de bloque
    f.write("INICIO DE LOS DATOS GENERALES DE LOS DISPOSITIVOS DE BLOQUE\n")
    f.write(os.popen("lsblk -a").read() + "\n")
    f.write("FIN DE LOS DATOS GENERALES DE LOS DISPOSITIVOS DE BLOQUE\n")
    f.write("---------------------------------\n")

    # Información de la red estática
    f.write("INICIO DE LOS DATOS ESTÁTICOS DE RED\n")
    f.write("Configuración de la red: \n")
    f.write(os.popen("ifconfig").read() + "\n")
    f.write("Tabla ARP: \n")
    f.write(os.popen("arp -a").read() + "\n")
    f.write("Dirección MAC: \n")
    f.write(os.popen("ifconfig | grep ether").read() + "\n")
    f.write("FIN DE LOS DATOS ESTÁTICOS DE RED\n")
    f.write("---------------------------------\n")

    # Información de la red dinámica
    f.write("INICIO DE LOS DATOS DINÁMICOS DE RED\n")
    f.write("Tabla de rutas: \n")
    f.write(os.popen("ip route").read() + "\n")
    f.write("Estadísticas de red: \n")
    f.write(os.popen("netstat -rn").read() + "\n")
    f.write("Adaptadores de red: \n")
    f.write(os.popen("hwinfo").read() + "\n")
    f.write("FIN DE LOS DATOS DINÁMICOS DE RED\n")
    f.write("---------------------------------\n")

    # Información de los servicios internos
    f.write("INICIO DE LOS DATOS INTERNOS DE PROCESOS EN MEMORIA\n")
    f.write("Estado de los servicios: \n")
    f.write(os.popen("systemctl --type=service").read() + "\n")
    f.write("Servicios corriendo actualmente: \n")
    f.write(os.popen("top").read() + "\n")
    f.write("FIN DE LOS DATOS INTERNOS DE PROCESOS EN MEMORIA\n")
    f.write("---------------------------------\n")

print(f"Output written to {os.getcwd()}")
