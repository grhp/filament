#!/usr/bin/env python3

import glob
import io
import os
import tarfile
import urllib.request

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

def process_demo():
    print('Renaming KTX to BMP...')
    paths = glob.glob('public/*.html')
    for path in paths:
        print(path)
        html = open(path).read()
        html = html.replace('.ktx', '_ktx.bmp')
        open(path, 'w').write(html)
    paths = glob.glob('public/*.ktx')
    for path in paths:
        print(path)
        basename = path.split('.ktx')[0]
        os.rename(path, f'public/{basename}_ktx.bmp')

def fetch_docs():
    print('Fetching docs...')
    url = 'https://raw.githubusercontent.com/google/filament/master/filament/docs/Vulkan.md.html'
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    html = html.replace('../../docs/', '')
    open('Vulkan.md.html', 'w').write(html)

# fetch_demo()
process_demo()
# fetch_docs()
