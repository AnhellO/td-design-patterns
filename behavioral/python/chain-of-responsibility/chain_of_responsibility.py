import abc

# Interfaz handler
class Handler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, request):
        pass
    
    @abc.abstractmethod
    def set_next(self):
        pass

# Clase base handler
class BaseHandler(Handler):
    def set_next(self, next_handler: Handler) -> None:
        self.next = next_handler
        
    def handle(self, request):
        if self.next != None:
            return self.next.handle(request)

# Handler concreto 1
class ValidationConcreteHandler(BaseHandler):
    def handle(self, request):
        # Valida que los valores de la petición cumplen con ciertas reglas de validación
        if not isinstance(request, dict):
            return "Failed validation"
            
        if not isinstance(request['user'], str) or not isinstance(request['pass'], str):
            return "Failed validation"
        
        if '<' in request['user'] or '>' in request['user']:
            return "Failed validation"
        
        if '<' in request['pass'] or '>' in request['pass']:
            return "Failed validation"
        
        return super().handle(request)

# Handler concreto 2
class AuthenticationConcreteHandler(BaseHandler):
    def __init__(self):
        # Cargamos registros desde la base de datos
        self.base_de_datos = {
            'user': "DAS",
            'pass': "Sistemas123"
        }
    
    def handle(self, request):
        # Obtén información de la base de datos y verifica si el usuario existe
        if request['user'] != self.base_de_datos['user'] or request['pass'] != self.base_de_datos['pass']:
            return "Failed authentication"
        
        return super().handle(request)
    
# Handler concreto 3
class AuthorizationConcreteHandler(BaseHandler):
    def handle(self, request):
        # Evaluar si el usuario/petición tiene los roles de autorización permitidos para el acceso
        if request['access'] not in ['admin', 'super']:
            return "Failed authorization"
        
        return "Access Granted!"
    
    