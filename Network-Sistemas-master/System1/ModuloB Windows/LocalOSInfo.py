import os
import platform
import subprocess

output_file_path = "machine_info.txt"

# Redirect the standard output to a file
with open(output_file_path, 'w') as f:
    # Write general machine information
    f.write("---------------------------------\n")
    f.write("INICIO DE LOS DATOS GENERALES DE LA MÁQUINA\n")
    f.write("Arquitectura de la máquina: " + platform.machine() + "\n")
    f.write("Nombre del host: " + platform.node() + "\n")
    f.write("Sistema Operativo: " + platform.platform() + "\n")
    f.write("Nombre del procesador: " + platform.processor() + "\n")
    f.write("Versión del sistema: " + platform.release() + "\n")

    # Use 'ver' command for Windows instead of 'uname -v'
    process = subprocess.Popen("ver", stdout=subprocess.PIPE, shell=True)
    f.write("Versión del kernel: " + process.stdout.read().decode() + "\n")

    f.write("FIN DE LOS DATOS GENERALES DE LA MÁQUINA\n")
    f.write("---------------------------------\n")

    # Write hardware information
    f.write("INICIO DE LOS DATOS DE HARDWARE DE LA MÁQUINA\n")
    process = subprocess.Popen("systeminfo", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")

    f.write("FIN DE LOS DATOS DE HARDWARE DE LA MÁQUINA\n")
    f.write("---------------------------------\n")

    # Write CPU information
    f.write("INICIO DE LOS DATOS GENERALES DE LA CPU\n")
    process = subprocess.Popen("wmic cpu get caption, deviceid, maxclockspeed, name, status", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")
    f.write("FIN DE LOS DATOS GENERALES DE LA CPU\n")
    f.write("---------------------------------\n")

    # Write block device information
    f.write("INICIO DE LOS DATOS GENERALES DE LOS DISPOSITIVOS DE BLOQUE\n")
    process = subprocess.Popen("wmic diskdrive list brief", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")
    f.write("FIN DE LOS DATOS GENERALES DE LOS DISPOSITIVOS DE BLOQUE\n")
    f.write("---------------------------------\n")

    # Write static network information
    f.write("INICIO DE LOS DATOS ESTÁTICOS DE RED\n")
    process = subprocess.Popen("ipconfig /all", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")
    f.write("FIN DE LOS DATOS ESTÁTICOS DE RED\n")
    f.write("---------------------------------\n")

    # Write dynamic network information
    f.write("INICIO DE LOS DATOS DINÁMICOS DE RED\n")
    process = subprocess.Popen("route print", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")
    f.write("FIN DE LOS DATOS DINÁMICOS DE RED\n")
    f.write("---------------------------------\n")

    # Write list of running processes
    f.write("INICIO DE LA LISTA DE PROCESOS EN EJECUCIÓN\n")
    process = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    f.write(process.stdout.read().decode() + "\n")
    f.write("FIN DE LA LISTA DE PROCESOS EN EJECUCIÓN\n")
    f.write("---------------------------------\n")

    # Write internal process information
    f.write("INICIO DE LOS DATOS INTERNOS DE PROCESOS EN MEMORIA\n")
    # Unfortunately, Windows doesn't have a direct equivalent for 'systemctl --type=service' or 'top'
    f.write("Información de servicios no disponible en Windows\n")
    f.write("FIN DE LOS DATOS INTERNOS DE PROCESOS EN MEMORIA\n")
    f.write("---------------------------------\n")

print(f"Output written to {os.getcwd()}")

