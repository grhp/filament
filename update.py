#!/usr/bin/env python3

import urllib.request
import tarfile
import io

def fetch_demo():
    print('Fetching web release...')
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

def fetch_docs():
    print('Fetching docs...')
    url = 'https://raw.githubusercontent.com/google/filament/master/filament/docs/Vulkan.md.html'
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    html = html.replace('../../docs/', '')
    open('Vulkan.md.html', 'w').write(html)

fetch_demo()
fetch_docs()
