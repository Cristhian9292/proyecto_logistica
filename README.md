# Proyecto de Logística

Este proyecto de logística está diseñado para gestionar el envío y seguimiento de paquetes. Utiliza Django como framework web para el backend y PostgreSQL como base de datos relacional.

## Instalación

### Requisitos previos

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Pasos de instalación

1. Clona este repositorio a tu máquina local:

    ```
    git clone https://github.com/Cristhian9292/proyecto_logistica
    ```

2. Navega al directorio del proyecto:

    ```
    cd proyecto_logistica
    ```

3. Instala las dependencias del proyecto:

    ```
    apt install python3-psycopg2
    apt install python3-djangorestframework
    ```

## Configuración de la base de datos

Este proyecto utiliza PostgreSQL como base de datos. Asegúrate de tener PostgreSQL instalado en tu sistema y crea una nueva base de datos para el proyecto.

1. Crea una nueva base de datos en PostgreSQL:

    ```sql
    CREATE DATABASE postgres;
    ```

2. Configura las credenciales de acceso a la base de datos en el archivo `settings.py` del proyecto Django. Busca la sección `DATABASES` y actualiza los valores de `USER`, `PASSWORD` y `HOST` según corresponda.

## Ejecución del proyecto

Una vez que hayas configurado la base de datos, puedes ejecutar el proyecto utilizando el servidor de desarrollo de Django.

1. Aplica las migraciones para crear las tablas en la base de datos:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

2. Inicia el servidor de desarrollo:

    ```
    python3 manage.py runserver
    ```

El proyecto estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Funcionamiento general

El proyecto permite gestionar clientes, paquetes y transportistas. Los clientes pueden enviar paquetes proporcionando detalles como peso, dimensiones, dirección de origen y destino, etc. Los paquetes pueden ser asignados a transportistas para su entrega. El estado de entrega de cada paquete se puede actualizar a medida que avanza el proceso de entrega.

## APIs

El proyecto proporciona las siguientes APIs para interactuar con los datos:

1. **Asignación de paquetes a transportistas**:
   
   Endpoint: `/asignar_paquete`
   
   Método: `POST`
   
   Descripción: Permite asignar un paquete a un transportista. Debes proporcionar el ID del paquete y el ID del transportista en el cuerpo de la solicitud.

2. **Actualización del estado de entrega de un paquete**:
   
   Endpoint: `/api/paquete/<int:paquete_id>/actualizar_estado`
   
   Método: `PUT`
   
   Descripción: Permite actualizar el estado de entrega de un paquete. Debes proporcionar el nuevo estado como query param.

## URLs

El proyecto contiene 3 urls con vistas para ver contenido de los paquetes

1. **Ver la lista de paquetes enviados por un cliente específico**:

    URL: `/paquetes/1/`

    Descripción: Permite ver la lista de paquetes por cliente por su ID (1 es el ID en la url ejemplo).

2. **Ver la lista de paquetes asignados a un transportista específico**:

    URL: `/paquetes_por_transportista/1/`

    Descripción: Permite ver la lista de paquetes por cliente por su ID (1 es el ID en la url ejemplo).

3. **Crear paquetes**:

    URL: `/paquetes/crear/`

    Descripción: Permite crear un paquete a través de su ID (1 es el ID en la url ejemplo).

4. **Editar paquetes**:

    URL: `/paquetes/1/editar/`

    Descripción: Permite editar la informacion de un paquete a traves de su ID (1 es el ID en la url ejemplo).

5. **Eliminar paquetes**:

    URL: `/paquetes/1/eliminar/`

    Descripción: Permite eliminar un paquete por su ID (1 es el ID en la url ejemplo).

## Colección Insomnia (Y Postman)

   Se encuentra el archivo JSON con la colección de los endpoints en la carpeta "insomnia_collection"

## Retos

1. **Lambda**
    ```python
    area_triangulo = lambda base, altura: (base * altura) / 2

    base = 5
    altura = 3
    print("El área del triángulo es:", area_triangulo(base, altura))
    ```

2. **LookUp Table**
    ```python
    lookup_table = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cherry',
    'D': 'Date'
    }


    print(lookup_table['A'])  # Output: Apple
    print(lookup_table['C'])  # Output: Cherry

    if 'B' in lookup_table:
        print("B exists in the lookup table") 
    else:
        print("B does not exist in the lookup table")

    lookup_table['E'] = 'Elderberry'

    print(lookup_table)
    ```

3. **Fibonacci**
    ```python
    def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

    n = 6
    resultado = fibonacci(n)
    print(f"El {n}-ésimo valor de la secuencia de Fibonacci es: {resultado}")
    ```

4. **QuickSort**
    ```python
    def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    print("Arreglo original:", arr)
    print("Arreglo ordenado:", sorted_arr)
    ```

Para más información, contactar:

- Name: [Cristhian Cotes]
- Email: [cristhian9292@gmail.com]
- Phone: [+57-300-6587228]