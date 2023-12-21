import unittest

from chain_of_responsibility import *

class ChainOfResponsibilityTest(unittest.TestCase):
    def test_request_success(self):
        request = {
            "user": "DAS",
            "pass": "Sistemas123",
            "access": "admin"
        }
        handler_1 = ValidationConcreteHandler()
        handler_2 = AuthenticationConcreteHandler()
        handler_3 = AuthorizationConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual("Access Granted!", handler_1.handle(request))
    
    def test_request_failed_validation(self):
        request = {
            "user": "<sql INSERT INTO;#456;>",
            "pass": "Sistemas123"
        }
        handler_1 = ValidationConcreteHandler()
        handler_2 = AuthenticationConcreteHandler()
        handler_3 = AuthorizationConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual("Failed validation", handler_1.handle(request))
        
    def test_request_failed_authentication(self):
        request = {
            "user": "este men",
            "pass": "no existe :O"
        }
        handler_1 = ValidationConcreteHandler()
        handler_2 = AuthenticationConcreteHandler()
        handler_3 = AuthorizationConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual("Failed authentication", handler_1.handle(request))

    def test_request_failed_authorization(self):
        request = {
            "user": "DAS",
            "pass": "Sistemas123",
            "access": "normal"
        }
        handler_1 = ValidationConcreteHandler()
        handler_2 = AuthenticationConcreteHandler()
        handler_3 = AuthorizationConcreteHandler()
        handler_1.set_next(handler_2)
        handler_2.set_next(handler_3)
        self.assertEqual("Failed authorization", handler_1.handle(request))


if __name__ == "__main__":
    unittest.main()
