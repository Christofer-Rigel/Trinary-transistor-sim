class Transistor:
    def __init__(self, tid=""):
        self.id = tid
        self.state = 0  
        self.allowed_states = [-1, 0, 1] 

class And:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = (a + b - (a - b) * (a - b)) / 2

class Or:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = (a + b + (a - b) * (a - b)) / 2

class Not:
    def __init__(self, a):
        self.a = a
        self.output = -a

class Nand:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = -((a + b - (a - b) * (a - b)) / 2)

class Nor:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = -((a + b + (a - b) * (a - b)) / 2)

class Nxor:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = (a - b) * (1 - (a * b) * (a * b))

class Xor:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.output = -((a - b) * (1 - (a * b) * (a * b)))
