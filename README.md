API Consulta DGII RNC / CEDULA
==============================

Consulta en tiempo real los datos oficiales de RNC/Cédula en la DGII República Dominicana.

Esta api esta corriendo en linea 24/7 atravez del dominio https://rnc.megaplus.com.do.

# URL BASE:

```bash
https://rnc.megaplus.com.do
```

### OPCIONAL: 
Si deseas mantener y ejecutar la API localmente o en tu propio Servidor / VPS, puedes seguir las instrucciones de inslacion en [INSTALL.md](https://github.com/nsmdeveloper/api_consulta_rnc_cedula_dgii/blob/master/INSTALL.md)

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

© 2025 **[nsmdeveloper](https://www.natiumsofts.nimo.com.do/)** — Todos los derechos reservados.

