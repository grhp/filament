#!/usr/bin/env python3

import http.server
import os
import socketserver
import sys

if len(sys.argv) == 1:
    quit("Usage: serve [debug|release|docs|filaweb]")

PORT = 8000
HOME = os.environ.get('HOME')
FILAMENT = f'{HOME}/github/filament'
FILAWEB = f'{HOME}/github/filaweb'
CONFIG = sys.argv[1]

if CONFIG == 'filaweb':
    SERVEDIR = f'{FILAWEB}'
elif CONFIG == 'docs':
    SERVEDIR = f'{FILAMENT}/docs/'
else:
    SERVEDIR = f'{FILAMENT}/out/cmake-webgl-{CONFIG}/samples/web/public'

os.system(f"ls -l {SERVEDIR}")
os.system(f"lsof -nP -i4TCP:{PORT}")

# Crucially, associate wasm files with the correct MIME type.
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.wasm': 'application/wasm',
})

# Serve all files in the script folder.
Handler.directory = SERVEDIR
os.chdir(SERVEDIR)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print("serving at port", PORT)
    httpd.serve_forever()
