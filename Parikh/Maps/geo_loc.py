import re
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

def main(ipaddr):
    """Geo-locates an IP address passed in argv[1]."""

    geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
    html_page = urlopen(geody).read()
    soup = Soup(html_page)

    # Filter paragraph containing geolocation info.
    paragraph = soup('p')[3]

    # Remove html tags using regex.
    geo_txt = re.sub(r'<.*?>', '', str(paragraph))
    print(geo_txt[32:].strip() + '\n')

import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

ipaddr = ip_address


main(ipaddr)