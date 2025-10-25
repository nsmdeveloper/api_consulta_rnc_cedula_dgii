API Consulta DGII RNC / CEDULA
==============================

Consulta en tiempo real los datos oficiales de RNC/Cédula en la DGII República Dominicana

Uso de la API
-------------

Existen dos métodos para consultar:

### GET

```bash
GET https://rnc.megaplus.com.do/api/consulta?rnc=131996035
```

### POST

```bash
POST https://rnc.megaplus.com.do/api/consulta
{
    "rnc": "131996035"
}
```

### Ejemplos con cURL

### GET:

```bash
curl -X GET "https://rnc.megaplus.com.do/api/consulta?rnc=131996035"
```

### POST:

```bash
curl -X POST "https://rnc.megaplus.com.do/api/consulta" -H "Content-Type: application/json" -d '{"rnc": "131996035"}'
```

### Ejemplo de respuesta (Éxito)
```bash
{
  "actividad_economica": "CRÍA DE ANIMALES Y OBTENCIÓN DE PRODUCTOS DE ORIGEN ANIMAL, N.C.P. (INCL. CIERVO, CONEJO EXCEPTO PARA PELO, GATO, LOMBRIZ PÁJARO,",
  "administracion_local": "ADM LOCAL LA VEGA",
  "categoria": "",
  "cedula_rnc": "131-99603-5",
  "estado": "ACTIVO",
  "facturador_electronico": "SI",
  "licencias_de_comercializacion_de_vhm": "N/A",
  "nombre_comercial": "AGROPECUARIA DELIA & MILO AGRODEMI",
  "nombre_razon_social": "AGROPECUARIA DELIA & MILO AGRODEMI SRL",
  "regimen_de_pagos": "NORMAL",
  "rnc_consultado": "131996035"
}
```
Respuestas de Error (Formato JSON)
----------------------------------

Todos los errores, incluidos los de cliente (4xx) y servidor (5xx), se devuelven en formato JSON consistente.


### Error de Cliente (400 Bad Request)

### Código HTTP: 400

Devuelto cuando el cuerpo de la solicitud (JSON) o los parámetros son inválidos o faltan.

```bash
{
  "error": true,
  "codigo_http": 400,
  "mensaje": "solicitud incorrecta: el campo 'rnc' es obligatorio y debe tener 9 o 11 dígitos.",
  "rnc_consultado": null
}
```

### Error de Negocio (404 Not Found)

### Código HTTP: 404

Devuelto cuando el RNC/Cédula es válido pero no se encuentra inscrito como contribuyente.

```bash
{
  "error": true,
  "codigo_http": 404,
  "mensaje": "el rnc/cedula consultado no se encuentra inscrito como contribuyente.",
  "rnc_consultado": "1305035590"
}
```

### Error de Servidor (500 Internal Server Error)

### Código HTTP: 500

Devuelto cuando hay un error inesperado en el servidor o al consultar la DGII.

```bash
{
  "error": true,
  "codigo_http": 500,
  "mensaje": "error interno del servidor. ha ocurrido un fallo inesperado.",
  "rnc_consultado": "1305035590"
}
```

### Documentación Interactiva

Accede a [Swagger UI](https://rnc.megaplus.com.do/apidocs/) para probar la API directamente.

### Comunidad / Soporte

Únete a nuestro Discord para soporte y novedades:

[Discord](https://discord.gg/dfXXM42yM3)

### Pagina Web Oficial

Accede a (https://rnc.megaplus.com.do/).

© 2025 [nsmdeveloper](https://discord.gg/dfXXM42yM3). Todos los derechos reservados.
