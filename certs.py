import ssl
import socket
import datetime
from bs4 import BeautifulSoup

def get_certificate_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                cert_info = {
                    "subject": dict(x[0] for x in cert["subject"]),
                    "issuer": dict(x[0] for x in cert["issuer"]),
                    "notBefore": cert["notBefore"],
                    "notAfter": cert["notAfter"],
                }
                return cert_info
    except Exception as e:
        print(f"Error fetching certificate for {domain}: {e}")
        return None

def generate_html(certificates):
    html = "<html><head><title>SSL Certificate Info</title></head><body><table>"
    html += "<tr><th>Domain</th><th>Not Before</th><th>Not After</th><th>Issuer</th><th>Days Left</th></tr>"
    for domain, cert_info in certificates.items():
        not_before = datetime.datetime.strptime(cert_info["notBefore"], "%b %d %H:%M:%S %Y %Z")
        not_after = datetime.datetime.strptime(cert_info["notAfter"], "%b %d %H:%M:%S %Y %Z")
        days_left = (not_after - datetime.datetime.now()).days
        Issuer = cert_info["issuer"]
        html += f"<tr><td>{domain}</td><td>{not_before}</td><td>{not_after}</td><td>{Issuer}</td><td>{days_left}</td></tr>"
    html += "</table></body></html>"
    return html

# Lista de dominios
dominios = [
"www.dermaglos.us",
"nfsssrs.andromaco.com.ar",
"www.prevencionparasitosisintestinal.com.ar",
"sedacc.andromaco.com.ar",
"logino365.andromaco.com.ar",
"qs01.labandromaco.com.ar",
"empresas.andromaco.com.ar",
"bloginnovacion.andromaco.com.ar",
"androma.co",
"pedidos.andromaco.com",
"www.dermaglos.com",
"dermaglos.com",
"www.dermaglos.com.uy",
"www.hipoglos.com",
"www.aveno.com.ar",
"www.bushi.com.ar",
"www.prurisedan.com.ar",
"www.materna.com.ar",
"www.andromaco.com",
"adserver.proximitas.com.ar",
"www.cedlabs.com",
"internacional.andromaco.com",
"www.andromaco.com.py",
"www.andromaco.com.bo",
"www.andromaco.com.gt",
"www.andromaco.co.cr",
"www.andromaco.com.pa",
"www.andromaco.com.pe",
"www.andromaco.com.uy",
"mf.andromaco.com.ar",
"tienda.andromaco.com",
"nfs.andromaco.com.ar",
"pedidos.andromaco.com"
]

# Obtener información del certificado para cada dominio
certificados = {}
for dominio in dominios:
    cert_info = get_certificate_info(dominio)
    if cert_info:
        certificados[dominio] = cert_info

# Generar HTML
contenido_html = generate_html(certificados)

# Guardar HTML en un archivo
with open("informacion_certificados_ssl.html", "w") as f:
    f.write(contenido_html)

print("La información de los certificados SSL se ha guardado en informacion_certificados_ssl.html")