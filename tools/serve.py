"""Serve site/ at http://localhost:4173 (opening site/index.html directly also works).

    python3 tools/serve.py [port]
"""
import functools
import http.server
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
port = int(sys.argv[1]) if len(sys.argv) > 1 else 4173
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
    print(f"qrup-596: http://localhost:{port}/  (Ctrl+C to stop)")
    httpd.serve_forever()
