API Consulta DGII RNC / CEDULA
==============================

Consulta en tiempo real los datos oficiales de RNC/Cédula en la DGII República Dominicana.

Esta api esta corriendo en linea 24/7 atravez del dominio https://rnc.megaplus.com.do.

# URL BASE:

```bash
https://rnc.megaplus.com.do
```

### OPCIONAL: 
Si deseas mantener y ejecutar la API localmente o en tu propio Servidor / VPS, puedes seguir las instrucciones de instalacion en [INSTALL.md](https://github.com/nsmdeveloper/api_consulta_rnc_cedula_dgii/blob/master/INSTALL.md)

Uso de la API
-------------

Tipos de Consultas
-------------------

    * Consulta por RNC / Cedula
    * Consulta por Nombre (Exacto)
    * Consulta por Nombres

# Consulta por RNC / Cedula:

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
  "error": false,
  "codigo_http": 200,
  "mensaje": "Consulta Exitosa",
  "cedula_rnc": "131-99603-5",
  "nombre_razon_social": "AGROPECUARIA DELIA & MILO AGRODEMI SRL",
  "nombre_comercial": "AGROPECUARIA DELIA & MILO AGRODEMI",
  "categoria": "",
  "regimen_de_pagos": "NORMAL",
  "estado": "ACTIVO",
  "actividad_economica": "CRÍA DE ANIMALES Y OBTENCIÓN DE PRODUCTOS DE ORIGEN ANIMAL, N.C.P. (INCL. CIERVO, CONEJO EXCEPTO PARA PELO, GATO, LOMBRIZ PÁJARO,",
  "administracion_local": "ADM LOCAL LA VEGA",
  "facturador_electronico": "SI",
  "licencias_de_comercializacion_de_vhm": "N/A",
  "rnc_consultado": "131996035"
}
```

# Consulta por Nombre (Exacto):

Existen dos métodos para consultar:

### GET

```bash
GET https://rnc.megaplus.com.do/api/consulta/nombre?buscar=lugo & de oleo
```

### POST

```bash
POST https://rnc.megaplus.com.do/api/consulta/nombre
{
    "buscar": "lugo & de oleo"
}
```

### Ejemplos con cURL

### GET:

```bash
curl -X GET "https://rnc.megaplus.com.do/api/consulta/nombre?buscar=lugo"
```

### POST:

```bash
curl -X POST "https://rnc.megaplus.com.do/api/consulta/nombre" -H "Content-Type: application/json" -d '{"buscar": "lugo & de oleo"}'
```

### Ejemplo de respuesta (Éxito)
```bash
{
    "error": false,
    "codigo_http": 200,
    "mensaje": "Consulta  Exitosa",
    "cedula_rnc": "130-00229-2",
    "nombre_razon_social": "LUGO & DE OLEO EIRL",
    "nombre_comercial": "LUGO & DE OLEO",
    "categoria": "",
    "regimen_de_pagos": "NORMAL",
    "estado": "ACTIVO",
    "actividad_economica": "SERVICIOS INMOBILIARIOS REALIZADOS A CAMBIO DE UNA RETRIB. O POR CONTRATA (INCL. COMPRA, VENTA, ALQUILER, REMATE, TASACIÓN, ADM DE",
    "administracion_local": "ADM LOCAL LA FERIA",
    "facturador_electronico": "NO",
    "licencias_de_comercializacion_de_vhm": "N/A",
    "rnc_consultado": "130002292"
}
```

# Consulta por Nombres:

Existen dos métodos para consultar:

### GET

```bash
GET https://rnc.megaplus.com.do/api/consulta/nombres?buscar=lugo
```

### POST

```bash
POST https://rnc.megaplus.com.do/api/consulta/nombres
{
    "buscar": "lugo"
}
```

### Ejemplos con cURL

### GET:

```bash
curl -X GET "https://rnc.megaplus.com.do/api/consulta/nombres?buscar=lugo"
```

### POST:

```bash
curl -X POST "https://rnc.megaplus.com.do/api/consulta/nombres" -H "Content-Type: application/json" -d '{"buscar": "lugo"}'
```

### Ejemplo de respuesta (Éxito)
```bash
{
    "codigo_http": 200,
    "error": false,
    "info_paginacion": {
        "pagina_actual": 1,
        "paginas_totales": 5,
        "total_en_esta_pagina": 7
    },
    "mensaje": "Consulta Exitosa",
    "resultados": [
        {
            "categoria": "",
            "cedula_rnc": "130-00229-2",
            "estado": "ACTIVO",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "LUGO & DE OLEO",
            "nombre_razon_social": "LUGO & DE OLEO EIRL",
            "regimen_de_pagos": "NORMAL"
        },
        {
            "categoria": "",
            "cedula_rnc": "101-82861-7",
            "estado": "SUSPENDIDO",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "",
            "nombre_razon_social": "LUGO & DIAZ COBROS REALES C POR A",
            "regimen_de_pagos": "N/D"
        },
        {
            "categoria": "",
            "cedula_rnc": "131-98667-6",
            "estado": "ACTIVO",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "LUGO & MORA INVESTMENT GROUP",
            "nombre_razon_social": "LUGO & MORA INVESTMENT GROUP SRL",
            "regimen_de_pagos": "NORMAL"
        },
        {
            "categoria": "",
            "cedula_rnc": "118-01153-2",
            "estado": "SUSPENDIDO",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "",
            "nombre_razon_social": "LUGO ALCIBIADES SUCS",
            "regimen_de_pagos": "N/D"
        },
        {
            "categoria": "",
            "cedula_rnc": "123-01489-9",
            "estado": "DADO DE BAJA",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "",
            "nombre_razon_social": "LUGO AUTO IMPORT C POR A",
            "regimen_de_pagos": "N/D"
        },
        {
            "categoria": "",
            "cedula_rnc": "111-00167-6",
            "estado": "SUSPENDIDO",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "",
            "nombre_razon_social": "LUGO C POR A",
            "regimen_de_pagos": "NORMAL"
        },
        {
            "categoria": "",
            "cedula_rnc": "101-69475-2",
            "estado": "DADO DE BAJA",
            "facturador_electronico": "NO",
            "licencias_de_comercializacion_de_vhm": "N/A",
            "nombre_comercial": "",
            "nombre_razon_social": "LUGO COMERCIAL S A",
            "regimen_de_pagos": "NORMAL"
        }
    ]
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

---


### 📘 Documentación Interactiva

Explora y prueba los endpoints de la API directamente desde Swagger UI:

[![Abrir en Swagger UI](https://img.shields.io/badge/Swagger%20UI-Open%20Docs-brightgreen?logo=swagger&style=for-the-badge)](https://rnc.megaplus.com.do/apidocs/)


### 🚀 Probar la API en Postman

Haz clic en el siguiente botón para importar la colección directamente en Postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/26024289-a99cec98-c460-42f2-8535-dd40b625d465?action=collection%2Ffork&collection-url=entityId%3D26024289-a99cec98-c460-42f2-8535-dd40b625d465%26entityType%3Dcollection%26workspaceId%3D713a5e06-8546-4ea6-a9e6-5cc6a6832c66)

---

### 👥 Comunidad / Soporte

Únete a nuestro Discord para soporte y novedades:

[![Unite Discord Channel](https://img.shields.io/badge/Discord-Join%20Channel-5865F2?logo=discord&logoColor=white&style=for-the-badge)](https://discord.gg/dfXXM42yM3)

### 🌍 Página Web Oficial

Visita la plataforma en línea:

[**https://rnc.megaplus.com.do**](https://rnc.megaplus.com.do)

---

© 2026 **[nsmdeveloper](https://www.natiumsofts.nimo.com.do/)** — Todos los derechos reservados.

