import urllib.request
import re

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.request.urlopen(url)
html = response.read()
txt = html.decode()
data = re.findall(r'\(\d{3}\) \d{3}-\d{4}', txt)

for phone in data:
    print(phone)