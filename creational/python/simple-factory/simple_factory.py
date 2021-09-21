class SchoolMember:
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class Teacher(SchoolMember):
    def __str__(self):
        return f"Soy el maestro {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class Student(SchoolMember):
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
        self.degree = args.get('degree', '')

    def __str__(self):
        return f"Soy el alumno {self.name}!, tengo {self.age} años, mi ID es = {self.id_num} y pertenezco a la carrera {self.degree}"
        
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        try:
            return eval(kind.capitalize())(**args)
        except Exception:
            return f"Error! tipo '{kind}' invalido!"
        

def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    _age = input("Qué edad tiene?\n")
    _id = input("Qué ID tiene?\n")
    
    _degree = None
    if kind == 'student':
        _degree = input("Cuál es su carrera?\n")
    
    obj = SchoolMemberFactory.make(kind, name=_name, age=_age, id_num=_id, degree=_degree)
    print(obj)
    
if __name__ == "__main__":
    main()