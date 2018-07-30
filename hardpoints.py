class Hardpoint:
    pass

class CraneArm(Hardpoint):
    def __init__(self):
        self.name = 'Crane Arm'
        self.description = ''''''
        self.cost = 50

class BigCraneArm(Hardpoint):
    def __init__(self):
        self.name = 'Big Crane Arm'
        self.description = ''''''
        self.cost = 75

class Turret(Hardpoint):
    def __init__(self):
        self.name = 'Turret'
        self.description = ''''''
        self.cost = 200

class SwivelMount(Hardpoint):
    def __init__(self):
        self.name = 'Swivel Mount'
        self.description = ''''''
        self.cost = 125

class Front(Hardpoint):
    def __init__(self):
        self.name = 'Front Hardpoint'
        self.description = ''''''
        self.cost = 25

class Rear(Hardpoint):
    def __init__(self):
        self.name = 'Rear Hardpoint'
        self.description = ''''''
        self.cost = 25

class Left(Hardpoint):
    def __init__(self):
        self.name = 'Left Hardpoint'
        self.description = ''''''
        self.cost = 25

class Right(Hardpoint):
    def __init__(self):
        self.name = 'Right Hardpoint'
        self.description = ''''''
        self.cost = 25

class Concealed(Hardpoint):
    def __init__(self):
        self.name = 'Concealed Hardpoint'
        self.description = ''''''
        self.cost = 75
