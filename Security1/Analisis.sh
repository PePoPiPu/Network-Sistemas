#!/bin/bash

# Definir las variables
MACHINE_IDENTIFIER="identificador_de_la_maquina"
OUTPUT_FILE="reporte_${MACHINE_IDENTIFIER}_$(date +'%Y%m%d_%H%M%S').txt"
PERIOD="5 mins"

# Ejecuta Snort, captura tráfico en tiempo real y guarda la salida en un archivo
snort -c /etc/snort/snort.conf -q -l /home/alexsugimoto/Documentos/DAM/Sistemas_Informáticos/2EV/ASAlex_Actividad_Evaluable2EV/Security1 -v -i eno1 -K none -N -l /home/alexsugimoto/Documentos/DAM/Sistemas_Informáticos/2EV/ASAlex_Actividad_Evaluable2EV/Security1 -b -B 512 &

# Espera el tiempo especificado para capturar el tráfico
sleep 300

# Detiene la ejecución de Snort
killall -SIGINT snort
# Escribir el resultado en el archivo de salida
echo "Reporte de incidencias - $MACHINE_IDENTIFIER - $(date +'%Y-%m-%d %H:%M:%S')" > $OUTPUT_FILE
echo "Periodo de análisis: $PERIOD" >> $OUTPUT_FILE
echo "----------------------------------------------" >> $OUTPUT_FILE
# Genera el archivo del reporte:
grep "Alerta" /home/alexsugimoto/Documentos/DAM/Sistemas_Informáticos/2EV/ASAlex_Actividad_Evaluable2EV/Security1/snortAlertas.txt >> $OUTPUT_FILE
grep "Alarma" /home/alexsugimoto/Documentos/DAM/Sistemas_Informáticos/2EV/ASAlex_Actividad_Evaluable2EV/Security1/snortAlarmas.txt >> $OUTPUT_FILE

echo "Proceso completado. El reporte se ha guardado en: $OUTPUT_FILE"

