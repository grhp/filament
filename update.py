#!/usr/bin/env python3

import urllib.request
import tarfile
import io

url = 'https://filament-build.storage.googleapis.com/badges/build_link_web.html'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
head = text.find('url=') + 4
tail = text.find('.tgz') + 4
url = text[head:tail]

response = urllib.request.urlopen(url)
data = response.read()

tar = tarfile.open(fileobj=io.BytesIO(data), mode="r:gz")
tar.extractall('public')
tar.close()
