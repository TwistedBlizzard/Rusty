class Hardpoint:
    pass

class CraneArm(Hardpoint):
    def __init__(self):
        self.cost = 50

class BigCraneArm(Hardpoint):
    def __init__(self):
        self.cost = 75

class Turret(Hardpoint):
    def __init__(self):
        self.cost = 200

class SwivelMount(Hardpoint):
    def __init__(self):
        self.cost = 125

class Front(Hardpoint):
    def __init__(self):
        self.cost = 25

class Rear(Hardpoint):
    def __init__(self):
        self.cost = 25

class Left(Hardpoint):
    def __init__(self):
        self.cost = 25

class Right(Hardpoint):
    def __init__(self):
        self.cost = 25

class Concealed(Hardpoint):
    def __init__(self):
        self.cost = 75
