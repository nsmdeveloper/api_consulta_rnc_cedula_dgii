API Consulta DGII RNC / CEDULA
==============================

Consulta en tiempo real los datos oficiales de RNC/Cédula en la DGII República Dominicana

Uso de la API
-------------

Existen dos métodos para consultar:

### GET

GET https://rnc.megaplus.com.do/api/consulta?rnc=131996035

### POST

POST https://rnc.megaplus.com.do/api/consulta
{
    "rnc": "131996035"
}

### Ejemplos con cURL

GET:

curl -X GET "https://rnc.megaplus.com.do/api/consulta?rnc=131996035"

POST:

curl -X POST "https://rnc.megaplus.com.do/api/consulta" -H "Content-Type: application/json" -d '{"rnc": "131996035"}'

### Ejemplo de respuesta (Éxito)

{
  "actividad\_economica": "CRÍA DE ANIMALES Y OBTENCIÓN DE PRODUCTOS DE ORIGEN ANIMAL, N.C.P. (INCL. CIERVO, CONEJO EXCEPTO PARA PELO, GATO, LOMBRIZ PÁJARO,",
  "administracion\_local": "ADM LOCAL LA VEGA",
  "categoria": "",
  "cedula\_rnc": "131-99603-5",
  "estado": "ACTIVO",
  "facturador\_electronico": "SI",
  "licencias\_de\_comercializacion\_de\_vhm": "N/A",
  "nombre\_comercial": "AGROPECUARIA DELIA & MILO AGRODEMI",
  "nombre\_razon\_social": "AGROPECUARIA DELIA & MILO AGRODEMI SRL",
  "regimen\_de\_pagos": "NORMAL",
  "rnc\_consultado": "131996035"
}

Respuestas de Error (Formato JSON)
----------------------------------

Todos los errores, incluidos los de cliente (4xx) y servidor (5xx), se devuelven en formato JSON consistente.

### Error de Negocio (404 Not Found)

Código HTTP: 404

Devuelto cuando el RNC/Cédula es válido pero no se encuentra inscrito como contribuyente.

{
  "error": true,
  "codigo\_http": 404,
  "mensaje": "el rnc/cedula consultado no se encuentra inscrito como contribuyente.",
  "rnc\_consultado": "1305035590"
}

### Error de Cliente (400 Bad Request)

Código HTTP: 400

Devuelto cuando el cuerpo de la solicitud (JSON) o los parámetros son inválidos o faltan.

{
  "error": true,
  "codigo\_http": 400,
  "mensaje": "solicitud incorrecta: el campo 'rnc' es obligatorio y debe tener 9 o 11 dígitos.",
  "rnc\_consultado": null
}

### Error de Servidor (500 Internal Server Error)

Código HTTP: 500

Devuelto cuando hay un error inesperado en el servidor o al consultar la DGII.

{
  "error": true,
  "codigo\_http": 500,
  "mensaje": "error interno del servidor. ha ocurrido un fallo inesperado.",
  "rnc\_consultado": "1305035590"
}

### Documentación Interactiva

Accede a [Swagger UI](https://rnc.megaplus.com.do/apidocs/) para probar la API directamente.

### Comunidad / Soporte

Únete a nuestro Discord para soporte y novedades:

[Discord](https://discord.gg/dfXXM42yM3)

© 2025 [nsmdeveloper](https://discord.gg/dfXXM42yM3). Todos los derechos reservados.
