import socket
import ssl
import datetime
#from flask import Flask
from bs4 import BeautifulSoup


domains_url = [
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

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)



#def Web(Html):
#    soup = BeautifulSoup(Html, 'html.parser')
#    return str(soup)
    


if __name__ == "__main__":
    for value in domains_url:
        now = datetime.datetime.now()
        try:

            expire = ssl_expiry_datetime(value)
            diff = expire - now
            print ("Domain name: {} Expiry Date: {} Expiry Day: {}".format(value,expire.strftime("%Y-%m-%d"),diff.days))
#            #print(html)
        except Exception as e:
            print (e)