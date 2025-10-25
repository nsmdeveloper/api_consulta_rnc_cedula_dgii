#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API Flask para consultar RNC/Cédula en la DGII y devolver resultados estructurados en JSON.
Incluye documentación interactiva con Swagger UI (Flasgger) para GET y POST con JSON real.
Compatible con Python 3.8+.
"""

import os
import re
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flasgger import Swagger

app = Flask(__name__)

# ---- Documentación global Flasgger ----
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API Consulta DGII RNC",
        "description": (
            "Esta API permite consultar en tiempo real los datos de RNC/Cédula "
            "registrados en la DGII República Dominicana.\n\n"
            "Se puede acceder vía GET o POST y devolverá un JSON con la información "
            "oficial del contribuyente.\n\n"
        ),
        "version": "1.0.0",
        "contact": {
            "name": "nsmdeveloper",
            "url": "https://discord.gg/dfXXM42yM3",
            "email": "nsmprogramador@gmail.com"
        },
        "license": {
            "name": "Licencia MIT",
            "url": "https://opensource.org/licenses/MIT"
        }
    },
    "host": "rnc.megaplus.com.do",
    "basePath": "/",
    "schemes": ["https"],
    "tags": [
        {
            "name": "Consulta RNC / Cedula",
            "description": "Endpoints para consultar RNC / Cédula en la DGII"
        }
    ],
}

swagger = Swagger(app, template=swagger_template)

DGII_RNC_URL = "https://dgii.gov.do/app/WebApps/ConsultasWeb2/ConsultasWeb/consultas/rnc.aspx"
DEFAULT_TIMEOUT = 20

# ---- Funciones auxiliares ----
def parse_hidden_inputs(html):
    """Extrae los inputs ocultos ASP.NET (__VIEWSTATE, etc.)."""
    soup = BeautifulSoup(html, "lxml")
    hidden = {}
    for inp in soup.select("input[type=hidden]"):
        name = inp.get("name")
        if name:
            hidden[name] = inp.get("value", "")
    return hidden

def parse_result_table(html):
    """Convierte la tabla de resultados DGII a dict."""
    soup = BeautifulSoup(html, "lxml")

   # 1. BÚSQUEDA DE ERRORES HTTP GENÉRICOS (Ej: 415, 400, 404, etc.)
    # Estos errores a menudo tienen el mensaje en la etiqueta <title> y/o <h1>
    
    title_tag = soup.find("title")
    
    # Verificamos si el título contiene un código de error de 3 dígitos o una palabra clave de error
    if title_tag and any(keyword in title_tag.get_text(strip=True).lower() for keyword in ["error", "bad request", "not found"]):
        
        error_title = title_tag.get_text(strip=True)
        h1_tag = soup.find("h1")
        p_tag = soup.find("p")

        # Construimos un mensaje de error detallado
        error_message = f"{error_title}"
        if h1_tag:
            error_message += f": {h1_tag.get_text(strip=True)}"
        if p_tag:
             error_message += f" - {p_tag.get_text(strip=True)}"
        
        # Aplicar limpieza y minúsculas al mensaje de error completo
        error_message = (
            error_message.replace("é", "e")
            .replace("ó", "o")
            .replace("í", "i")
            .replace("á", "a")
            .replace("ú", "u")
            .replace("ñ", "n")
        ).lower()
        
        return {
            "error": True,
            "mensaje": error_message
        }

    # 2. BÚSQUEDA DEL SPAN DE ERROR DE NEGOCIO (DGII)
    error_span = soup.find("span", id="cphMain_lblInformacion")
    
    # Si encuentra el SPAN, construye y devuelve el objeto de error.
    if error_span:
        error_text = error_span.get_text(strip=True)
        
        # Aplicar limpieza de texto
        error_text = (
            error_text.replace("é", "e")
            .replace("ó", "o")
            .replace("í", "i")
            .replace("á", "a")
            .replace("ú", "u")
            .replace("ñ", "n")
        ).lower()
        
        # Devolver el objeto de error solicitado
        return {
            "error": True,
            "mensaje": error_text
        }
    
    # 3. BÚSQUEDA DE LA TABLA DE RESULTADOS
    table = soup.find("table", id=re.compile("dvDatosContribuyentes", re.I))
    data = {}

    if table:
        rows = table.find_all("tr")
        for tr in rows:
            cols = tr.find_all("td")
            if len(cols) == 2:
                key = cols[0].get_text(strip=True)
                val = cols[1].get_text(strip=True)
                key = (
                    key.replace(":", "")
                    .replace("/", "_")
                    .replace(" ", "_")
                    .replace("é", "e")
                    .replace("ó", "o")
                    .replace("í", "i")
                    .replace("á", "a")
                    .replace("ú", "u")
                    .replace("ñ", "n")
                ).lower()
                data[key] = val
    return data

def consulta_rnc(rnc_value):
    """Realiza la consulta HTTP simulando el formulario ASP.NET."""
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ConsultaRNC/1.0)",
        "Accept-Language": "es-ES,es;q=0.9",
    }

    r = session.get(DGII_RNC_URL, headers=headers, timeout=DEFAULT_TIMEOUT)
    if r.status_code != 200:
        return {"error": "No se pudo acceder a la página DGII", "status": r.status_code}
    hidden = parse_hidden_inputs(r.text)

    payload = hidden.copy()
    payload["ctl00$cphMain$txtRNCCedula"] = rnc_value
    payload["ctl00$cphMain$btnBuscarPorRNC"] = "BUSCAR"
    payload.setdefault("__EVENTTARGET", "")
    payload.setdefault("__EVENTARGUMENT", "")

    r2 = session.post(DGII_RNC_URL, data=payload, headers=headers, timeout=DEFAULT_TIMEOUT)
    if r2.status_code != 200:
        return {"error": "Error al enviar el formulario", "status": r2.status_code}

    data = parse_result_table(r2.text)
    data["rnc_consultado"] = rnc_value
    return data

# ---- Rutas Flask ----
@app.route("/")
def index():
    return """
 <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>API Consulta DGII RNC</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 0;
            /* Agregamos padding al body igual o mayor a la altura del header para evitar que el contenido se oculte debajo del header fijo */
            padding-top: 8rem; /* Estimar la altura del header para compensar */
        }
        header {
            background-color: #4a90e2;
            color: white;
            padding: 2rem;
            text-align: center;
            /* INICIO DE LA MODIFICACIÓN CLAVE */
            position: fixed; /* Fija la posición del header */
            top: 0;          /* Lo ancla a la parte superior de la ventana */
            left: 0;         /* Lo ancla a la izquierda */
            width: 100%;     /* Asegura que ocupe todo el ancho */
            z-index: 1000;   /* Asegura que esté por encima de otros elementos */
            box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* Opcional: añade sombra para destacarlo */
            /* FIN DE LA MODIFICACIÓN CLAVE */
        }
        header h1 {
            margin: 0;
            font-size: 2.2rem;
        }
        header p {
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        main {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        h2, h3 {
            color: #4a90e2;
            margin-top: 1.5rem;
        }
        .error-code {
            color: #d9534f;
            font-weight: bold;
        }
        pre {
            background-color: #f4f4f4;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
        }
        a.button {
            display: inline-block;
            margin-top: 1rem;
            padding: 0.6rem 1.2rem;
            background-color: #4a90e2;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: background-color 0.3s ease;
        }
        a.button:hover {
            background-color: #357ab8;
        }
        footer {
            text-align: center;
            margin: 3rem 0 1rem 0;
            color: #666;
        }
        footer a {
            color: #4a90e2;
            text-decoration: none;
        }
        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>API Consulta DGII RNC / CEDULA</h1>
        <p>Consulta en tiempo real los datos oficiales de RNC/Cédula en la DGII República Dominicana</p>
    </header>
    <main>
        <h2>Uso de la API</h2>
        <p>Existen dos métodos para consultar:</p>

        <h3>GET</h3>
        <pre>GET https://rnc.megaplus.com.do/api/consulta?rnc=131996035</pre>

        <h3>POST</h3>
        <pre>POST https://rnc.megaplus.com.do/api/consulta
{
    "rnc": "131996035"
}</pre>

        <h3>Ejemplos con cURL</h3>
        <p>GET:</p>
        <pre>curl -X GET "https://rnc.megaplus.com.do/api/consulta?rnc=131996035"</pre>

        <p>POST:</p>
        <pre>curl -X POST "https://rnc.megaplus.com.do/api/consulta" \
-H "Content-Type: application/json" \
-d '{"rnc": "131996035"}'</pre>

        <h3>Ejemplo de respuesta (Éxito)</h3>
        <pre>{
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
}</pre>

        <h2>Respuestas de Error (Formato JSON)</h2>
        <p>Todos los errores, incluidos los de cliente (4xx) y servidor (5xx), se devuelven en formato JSON consistente.</p>
        
        <h3>Error de Negocio (404 Not Found)</h3>
        <p class="error-code">Código HTTP: 404</p>
        <p>Devuelto cuando el RNC/Cédula es válido pero no se encuentra inscrito como contribuyente.</p>
        <pre>{
  "error": true,
  "codigo_http": 404,
  "mensaje": "el rnc/cedula consultado no se encuentra inscrito como contribuyente.",
  "rnc_consultado": "1305035590"
}</pre>

        <h3>Error de Cliente (400 Bad Request)</h3>
        <p class="error-code">Código HTTP: 400</p>
        <p>Devuelto cuando el cuerpo de la solicitud (JSON) o los parámetros son inválidos o faltan.</p>
        <pre>{
  "error": true,
  "codigo_http": 400,
  "mensaje": "solicitud incorrecta: el campo 'rnc' es obligatorio y debe tener 9 o 11 dígitos.",
  "rnc_consultado": null
}</pre>

        <h3>Error de Servidor (500 Internal Server Error)</h3>
        <p class="error-code">Código HTTP: 500</p>
        <p>Devuelto cuando hay un error inesperado en el servidor o al consultar la DGII.</p>
        <pre>{
  "error": true,
  "codigo_http": 500,
  "mensaje": "error interno del servidor. ha ocurrido un fallo inesperado.",
  "rnc_consultado": "1305035590"
}</pre>

        <h3>Documentación Interactiva</h3>
        <p>Accede a <a href="https://rnc.megaplus.com.do/apidocs/" class="button" target="_blank">Swagger UI</a> para probar la API directamente.</p>

        <h3>Comunidad / Soporte</h3>
        <p>Únete a nuestro Discord para soporte y novedades:</p>
        <p><a href="https://discord.gg/dfXXM42yM3" class="button" target="_blank">Discord</a></p>
    </main>
    <footer>
        &copy; 2025 <a href="https://discord.gg/dfXXM42yM3" target="_blank">nsmdeveloper</a>. Todos los derechos reservados.
    </footer>
</body>
</html>
    """

# ----- GET -----
@app.route("/api/consulta", methods=["GET"])
def api_consulta_get():
    """
    Consulta RNC / Cedula DGII por GET
    ---
    tags:
      - Consulta RNC / Cedula
    parameters:
      - name: rnc
        in: query
        type: string
        required: true
        description: Número de RNC / Cedula a consultar
        example: "130718296"
    responses:
      200:
        description: Respuesta correcta con datos del RNC / Cedula
      400:
        description: RNC / Cedula no proporcionado
      404:
        description: RNC / Cedula no econtrado
      500:
        description: Falla interna en servicio / API
    """
    rnc = request.args.get("rnc")
    if not rnc:
        return jsonify({"error": True,"codigo_http": 400,"mensaje": "Debe especificar el parámetro 'rnc'"}), 400
    try:
        result = consulta_rnc(rnc.strip())
        if "error" in result and result["error"] is True:
            result['codigo_http'] = 404
            return jsonify(result), 404
            
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": True,"codigo_http": 500, "mensaje": str(e)}), 500


@app.route("/api/consulta", methods=["POST"])
def api_consulta_post():
    """
    Consulta RNC / Cedula DGII por POST con JSON
    ---
    tags:
      - Consulta RNC / Cedula
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - rnc / cedula
          properties:
            rnc:
              type: string
              description: Número de RNC / Cedula a consultar
              example: "130718296"
    responses:
      200:
        description: Respuesta correcta con datos del RNC / Cedula
      400:
        description: RNC / Cedula no proporcionado
      404:
        description: RNC / Cedula no econtrado
      500:
        description: Falla interna en servicio / API
    """
    data = request.get_json(force=True)
    rnc = data.get("rnc")
    if not rnc:
        return jsonify({"error": True,"codigo_http": 400,"mensaje": "Debe especificar el parámetro 'rnc'"}), 400
    try:
        result = consulta_rnc(rnc.strip())
        if "error" in result and result["error"] is True:
            result['codigo_http'] = 404
            return jsonify(result), 404
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": True, "codigo_http": 500, "mensaje": str(e)}), 500


# ---- Ejecutar Flask ----
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
