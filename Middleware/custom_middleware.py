from time import sleep

class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Herhangi bir ön işlemi gerçekleştirin
        print("Middleware'den geçiyor...")
        sleep(1)

        # Uygulama çağrısı
        response = self.app(environ, start_response)

        # Herhangi bir son işlemi gerçekleştirin
        sleep(1)
        print("Middleware işlemi tamamlandı.")

        return response

def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello, World!"]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    app = Middleware(simple_app)
    server = make_server('localhost', 8000, app)
    server.serve_forever()
