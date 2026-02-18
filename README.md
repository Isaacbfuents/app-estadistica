# App Estadística - Backend

Este proyecto consiste en el desarrollo de un scraper orientado a la obtención y procesamiento de datos deportivos.

En lugar de realizar scraping sobre HTML, se identificaron y consumieron directamente las APIs utilizadas por aplicaciones de estadísticas deportivas. A partir de esas respuestas JSON, se construyó una capa de parsing y normalización para estructurar la información de manera consistente y almacenarla en una base de datos propia.

## Objetivos

- Consumir datos estadísticos desde APIs externas.
- Procesar y transformar la información recibida.
- Normalizar las entidades (equipos, jugadores, estadísticas, temporadas, etc.).
- Generar identificadores internos.
- Persistir los datos en una base de datos relacional.

## Flujo

1. Consumo de API externa.
2. Parseo y transformación de datos.
3. Creación de modelos internos.
4. Inserción en base de datos.