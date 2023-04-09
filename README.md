
## Crud Basico usando Flask y Mongodb

una Practica de como se usan las operaciones basicas llamadas CRUD.

Navega hasta el directorio del proyecto: cd <directorio-NombreDelProyecto>

Crea un entorno virtual con el siguiente comando: python3 -m venv venv

Activa el entorno virtual con el siguiente comando: source venv/bin/activate (en Windows, utiliza venv\Scripts\activate)

Instala los paquetes necesarios con el siguiente comando: pip install -r requirements.txt

Ejecuta la aplicación Flask con el siguiente comando: flask run

Abre un navegador web y ve a la dirección http://localhost:5000 para ver la aplicación en funcionamiento.


# REST API

La API REST de la aplicación de ejemplo se describe a continuación.

## Obtener toda la lista de la BDD

### Request

`GET /api/Todo`

    curl -i -H 'Accept: application/json' http://localhost:5000/api/Todo

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    ```json
    {
    "Datos":[
        {
            "Email":"prueba@gmail.com",
            "Nombre":"Jhoney Testeando ",
            "Password":{
                "$binary":{
                "base64":"JDJiJDEyJFhsak8uSkY3Z0M2SkhPRzJiRWd4SS5PRHlYR3dIMnIvZEFROU82WksxWjk3SXQ5NWc0VzdP",
                "subType":"00"
                }
            },
            "_id":{
                "$oid":"64334079d17712bf3d059a6a"
            }
        },
        {
            "Email":"Carlos@gmail.com",
            "Nombre":"Jesus carlos",
            "Password":{
                "$binary":{
                "base64":"JDJiJDEyJHRrN0JVVlEwQ2liNVhuVmlMRVdQcnVoOUxLUmNWRDdJNUFUQ0JMM3NVNE93NEtRWjdzcWRt",
                "subType":"00"
                }
            },
            "_id":{
                "$oid":"6433424ed17712bf3d059a6b"
            }
        },
        {
            "Email":"PerezTest@gmail.com",
            "Nombre":"Andrea Perez",
            "Password":{
                "$binary":{
                "base64":"JDJiJDEyJEExMHM5cUVWOS9KLnlUU0lyMGZQL3VoL25TSWVsNkJqWkx4RmlMRVl5dU1vdzVjeHZqRHZt",
                "subType":"00"
                }
            },
            "_id":{
                "$oid":"64334269d17712bf3d059a6c"
            }
        }
    ]
    }
    ```


## Obtener solo una lista mediante el ID

### Request

`GET /api/Buscar/{id}`

    curl -i -H 'Accept: application/json' http://localhost:5000/api/Buscar/{id}
### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    ```json
        [
            {
                "Email":"PerezTest@gmail.com",
                "Nombre":"Andrea Perez",
                "Password":{
                    "$binary":{
                        "base64":"JDJiJDEyJEExMHM5cUVWOS9KLnlUU0lyMGZQL3VoL25TSWVsNkJqWkx4RmlMRVl5dU1vdzVjeHZqRHZt",
                        "subType":"00"
                    }
                },
                "_id":{
                    "$oid":"64334269d17712bf3d059a6c"
                }
            }
        ]
    ```

## Crear un documento en la base de datos

### Request

`POST /api/Agregar`

    curl -i -H 'Accept: application/json' http://localhost:5000/api/Agregar
### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

   ```json
    {
    "Nombre": "Jhoney Testeando ",
    "Password": "b'$2b$12$XljO.JF7gC6JHOG2bEgxI.ODyXGwH2r/dAQ9O6ZK1Z97It95g4W7O'",
    "_id": "64334079d17712bf3d059a6a"
    }
   ```


## Eliminar un documento ingresando el ID

### Request

`GET /api/Eliminar/{id}`

    curl -i -H 'Accept: application/json' http://localhost:5000/api/Eliminar/{id}

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    ```json
    {"mensaje": "Registro con: 643180f3552b4123e73a33df Fue eliminado"}
    ```
