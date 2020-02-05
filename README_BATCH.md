# AWS Batch Axpo

Integración de Airegas

## Comenzando 🚀

Esta versión contiene 4 integraciones a modo de Poc totalmente funcionales para los modos de actuación:

* Carga masiva.
 
  Consume directamente la API correspondiente a partir de los parámetros informados en el fichero excel. 
  En caso de que la colección no esté informada actuará en modo delta.
  Para cada colección se puede especificar los campos: from / to / fromMaxLastModified / toMaxLastModified / ListCodes
  así como un listado de clientes para la liquidación posterior
  
* Modo delta.

  Se consulta fromLastModified de cada colección, se consume el api con este dato en la query y se persisten en DocumentDB

### Pre-requisitos 📋

El proyecto está diseñado para ser dockerizado y posteriormente ser invocado a través de las definiciones de trabajo de AWS Batch.
Se adjunta un Dockerfile simple basado en la imagen oficial de python 3 que resuelve las dependencias del proyecto y copia todo su contenido a /usr/src/app 
```
docker build -t tagname .
```


### Instalación 🔧
En AWS se deberá crear :
* 1 Entorno informático
* 1 Cola de trabajo
* 5 definiciones de trabajos ( 4 para las colecciones y una de control )

```
En cada definición de trabajo (AWS), Container image deberá referenciar a la uri del repositorio.
Para un ecr de Amazon: 
ej. 012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>

En el command:
["python","entrypoint.py","coleccion_a_integrar"]

En este caso :

- Calendario
- Nominacion
- Prevision
- PrecioFormula

```



```
["python","entrypoint.py","Calendario"]
```



## Variables de entorno que deben ser informadas ⚙️

    BUCKET_NAME = os.getenv('BUCKET_NAME') --> Nombre del bucket en el que se van a depositar los excels
    FILE = os.getenv('KEY')  --> corresponde al prefix S3 (path y/o nombre del fichero)
    DOCUMENTDB_URL = os.getenv('DOCUMENTDB_URL') --> url de conexion para DocumentDB
    DATABASE = os.getenv('DATABASE') --> Nombre de la base de datos
    AIREGAS_ENDPOINT_URL = Ip base del endpoint de las Api de Airegas
    AWS_SECRET_ACCESS_KEY
    AWS_ACCESS_KEY_ID
