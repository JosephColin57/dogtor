uso: git tag [-a | -s | -u <key-id>] [-f] [-m <msg> | -F <file>] [-e]
             <tagname> [<commit> | <object>]
   o: git tag -d <nombre-de-tag>...
   o: git tag [-n[<num>]] -l [--contains <commit>] [--no-contains <commit>]
             [--points-at <object>] [--column[=<options>] | --no-column]
             [--create-reflog] [--sort=<key>] [--format=<format>]
             [--merged <commit>] [--no-merged <commit>] [<pattern>...]
   o: git tag -v [--format=<formato>] <nombre-de-tag>...

    -l, --list            listar nombres de tags
    -n[<n>]               imprimir <n> líneas de cada mensaje de tag
    -d, --delete          eliminar tags
    -v, --verify          verificar tags

Opciones de creación de tags
    -a, --[no-]annotate   tags anotadas necesitan un mensaje
    -m, --message <mensaje>
                          mensaje de tag
    -F, --[no-]file <archivo>
                          leer mensaje desde un archivo
    -e, --[no-]edit       forzar la edición del mensaje de tag
    -s, --[no-]sign       tag anotado y firmado con GPG
    --[no-]cleanup <modo> cómo quitar espacios y #comentarios de mensajes
    -u, --[no-]local-user <key-id>
                          usar otra clave para firmar el tag
    -f, --[no-]force      remplazar tag si existe
    --[no-]create-reflog  crear un reflog

Opciones de listado de tag
    --[no-]column[=<estilo>]
                          mostrar lista de tags en columnas
    --contains <confirmar>
                          mostrar solo tags que contengan el commit
    --no-contains <confirmar>
                          mostrar solo tags que no contengan el commit
    --merged <confirmar>  solo imprimir las tags que estén fusionadas
    --no-merged <confirmar>
                          solo imprimir las tags que no estén fusionadas
    --[no-]omit-empty     do not output a newline after empty formatted refs
    --[no-]sort <clave>   nombre del campo por el cuál ordenar
    --[no-]points-at <objeto>
                          solo imprimir tags del objeto
    --[no-]format <formato>
                          formato para usar para el output
    --[no-]color[=<cuando>]
                          respetar los colores de formato
    -i, --[no-]ignore-case
                          ordenamiento y filtración son case-insensitive

