from gtts import gTTS
# -*- coding: utf-8 -*-

# Creacion de variable
_1_presentacion = 'Hola, sere tu narradora llamame anonymus, fui programada en python por  Rafael Moreno, utilizando el api de google, sin mas preambulos vamos con la carnita '
# configuracion el archivo
tts_es = gTTS(_1_presentacion, lang='es', tld='com.mx')
# impresion en el drectorio y formto deseado
tts_es.save('mp3/_1_presentacion.mp3')

_2_raiz = 'raiz,  aqui es donde se monta el sistema, aqui estan todos los directorios, de los cuales daremos detalles despues, por lo mientras usaremos el comando ls -l para mostrar  los permisos de los directorios'
tts_es_raiz = gTTS(_2_raiz, lang='es', tld='com.mx')
tts_es_raiz.save('mp3/_2_raiz.mp3')

_2_1_bin ='bin,  Binarios de los comandos esenciales (cp, rm, ls, etc.), usados por todos los usuarios'
tts_es_bin = gTTS(_2_1_bin, lang='es', tld='com.mx')
tts_es_bin.save('mp3/_2_1_bin.mp3')

_3_permisos = 'permisos, Como podemos apreciar lod directorios tienen grupo y usuario en este caso la mayoria grupo root usuario root, osea que solo pueden ser modificados con permisos de super usuario, los que empiezan con d significa que son directorios, la x significa que tienen permiso de de ejecucion, la w de escritura y la r de lectura, estos valores sepueden modificar con el uso de chmod, y el dueño del fichicher chow '
tts_es_permisos = gTTS(_3_permisos, lang='es', tld='com.mx')
tts_es_permisos.save('mp3/_3_permisos.mp3')

_4_boot = 'boot, Ficheros de configuración del arranque, núcleos y otros ficheros necesarios para el arranque (boot) del equipo.'
tts_es_boot = gTTS(_4_boot, lang='es', tld='com.mx')
tts_es_boot.save('mp3/_4_boot.mp3')

_5_dev = 'dev, los ficheros de dispositivo'
tts_es_dev = gTTS(_5_dev, lang='es', tld='com.mx')
tts_es_dev.save('mp3/_5_dev.mp3')

_6_etc = 'etc, ficheros de configuración, scripts de arranque, etc.'
tts_es_etc = gTTS(_6_etc, lang='es', tld='com.mx')
tts_es_etc .save('mp3/_6_etc.mp3')

_7_home = 'home, directorios personales (home) para los diferentes usuarios.'
tts_es_home = gTTS(_7_home, lang='es', tld='com.mx')
tts_es_home .save('mp3/_7_home.mp3')

_8_initrd = 'initrd, usado cuando se crea un proceso de arranque initrd personalizado.'
tts_es_initrd = gTTS(_8_initrd, lang='es', tld='com.mx')
tts_es_initrd.save('mp3/_8_initrd.mp3')

_9_lib = 'lib, librerías del sistema (libraries)'
tts_es_lib = gTTS(_9_lib, lang='es', tld='com.mx')
tts_es_lib.save('mp3/_9_lib.mp3')

_10_lost_found = 'lost+found, proporciona un sistema de "perdido+encontrado" (lost+found) para los ficheros que existen debajo del directorio raíz (/)'
tts_es_lost_found = gTTS(_10_lost_found, lang='es', tld='com.mx')
tts_es_lost_found.save('mp3/_10_lost_found.mp3')

_11_media = 'media, particiones montadas (cargadas) automáticamente en el disco duro y medios (media) extraíbles como CDs, cámaras digitales, etc.'
tts_es_media = gTTS(_11_media, lang='es', tld='com.mx')
tts_es_media .save('mp3/_11_media.mp3')


_12_mnt = 'mnt, sistemas de archivos montados manualmente en el disco duro.'
tts_es_mnt = gTTS(_12_mnt, lang='es', tld='com.mx')
tts_es_mnt .save('mp3/_12_mnt.mp3')

_13_opt = 'opt  proporciona una ubicación donde instalar aplicaciones opcionales (de terceros)'
tts_es_opt = gTTS(_13_opt, lang='es', tld='com.mx')
tts_es_opt.save('mp3/_13_opt.mp3')

_14_proc = 'proc,  directorio dinámico especial que mantiene información sobre el estado del sistema, incluyendo los procesos actualmente en ejecución'
tts_es_proc = gTTS(_14_proc, lang='es', tld='com.mx')
tts_es_proc .save('mp3/_14_proc.mp3')

_15_root = 'root, directorio personal del usuario root (superusuario); también llamado "barra-root".'
tts_es_root = gTTS(_15_root, lang='es', tld='com.mx')
tts_es_root .save('mp3/_15_rootc.mp3')

_16_sbin = 'sbin, binarios importantes del sistema'
tts_es_sbin = gTTS(_16_sbin, lang='es', tld='com.mx')
tts_es_sbin .save('mp3/_16_sbin.mp3')

_17_srv = 'srv, puede contener archivos que se sirven a otros sistemas'
tts_es_srv = gTTS(_17_srv, lang='es', tld='com.mx')
tts_es_srv .save('mp3/_17_srv.mp3')

_18_sys = 'sys, archivos del sistema (system)'
tts_es_sys = gTTS(_18_sys, lang='es', tld='com.mx')
tts_es_sys .save('mp3/_18_sys.mp3')

_19_tmp = 'tmp, temporary files'
tts_es_tmp = gTTS(_19_tmp, lang='es', tld='com.mx')
tts_es_tmp .save('mp3/_19_tmp.mp3')

_20_usr = 'usr, aplicaciones y archivos a los que puede acceder la mayoría de los usuarios'
tts_es_usr = gTTS(_20_usr, lang='es', tld='com.mx')
tts_es_usr .save('mp3/_20_usr.mp3')

_21_var = 'var, archivos variables como archivos de registros y bases de datos'
tts_es_var = gTTS(_21_var, lang='es', tld='com.mx')
tts_es_var .save('mp3/_20_usr.mp3')
