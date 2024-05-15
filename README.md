# Web Crawling con Python - Trabajo Práctico 
## TLP 3 - Python para Ciencia de datos


- **Objetivo**:
1. El objetivo de este trabajo práctico es implementar un web crawler en Python que pueda recorrer un sitio web, extraer todas las etiquetas `<a>` con sus respectivos enlaces y acceder a cada página enlazada. 
2. Por cada enlace encontrado, se deben obtener todas las etiquetas `<h1>` y `<p>` y almacenarlo en un array en un archivo JSON y si no se encuentran dichos elementos guardar el array como vacío. 

- Por ejemplo, si el crawler encuentra un enlace `https://example.com/pagina1` en una página y accede a ese enlace, debe obtener el contenido de la página `https://example.com/pagina1` y buscar todos los elementos `<h1></h1>` y
`<p></p>`, luego almacenarlo en un array en un archivo JSON bajo la clave
"https://example.com/pagina1" con el array de los elementos solicitados de la página como valor correspondiente y si no se encuentran dichos elementos guardar el array vacío.

### Resolución

- Para este proyecto se utilizó la url de un conocido diario de la ciudad de Formosa.
- Como resultado el programa guarda la información en un archivo `data.json`.

### Como probar el proyecto

1. Instalar dependencias

```bash
pip install -r requirements.txt
```

2. ejecutar
```bash
py __init__.py
```


