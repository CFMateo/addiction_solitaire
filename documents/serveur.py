import http.server


# Récupère le chemin d'un fichier
def read_file(path):
    try:
        with open('.' + path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None

def get_extension(path):
    point = path.rfind('.')
    return '' if point < 0 else path[point:]

def get_mime_type(path):
    ext = get_extension(path)
    return {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'text/javascript',
        '.py': 'text/python',
        '.svg': 'image/svg+xml'
    }.get(ext, 'text/plain')

class ServeurWeb(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == '/':
            path = '/solitaire.html' 

        if get_extension(path) in ['.ico', '.map']:
            return

        contenu = read_file(path)
        if contenu is None:
            self.send_error(404, "Fichier non trouvé")
            return

        self.send_response(200)
        self.send_header('Content-type', get_mime_type(path))
        self.end_headers()
        self.wfile.write(contenu)

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    print("Serveur lancé sur http://localhost:8000")
    http.server.HTTPServer(('localhost', 8000), ServeurWeb).serve_forever()
