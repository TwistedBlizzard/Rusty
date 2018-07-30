class Vehicle:
    def __init__(self):
        self.ve_turns = True
        self.e_turns = True
        self.m_turns = True
        self.h_turns = True
        self.vh_turns = True
        self.i_turns = True
    def set_name(self, name):
        self.name = name
    def set_description(self, description):
        self.description = description

class Motorcycle(Vehicle):
    def __init__(self):
        self.name = 'Motorcycle'
        self.description = ''''''
        self.cost = 100
        self.crew = 1
        self.hardpoints = 1
        self.targeting = -2

class Dunebuggy(Vehicle):
    def __init__(self):
        self.name = 'Dunebuggy'
        self.description = ''''''
        self.cost = 200
        self.crew = 2
        self.hardpoints = 2
        self.targeting = -1

class AverageCar(Vehicle):
    def __init__(self):
        self.name = 'AverageCar'
        self.description = ''''''
        self.cost = 300
        self.crew = 3
        self.hardpoints = 3
        self.targeting = 0

class LargePickup(Vehicle):
    def __init__(self):
        self.name = 'Large Pickup'
        self.description = ''''''
        self.cost = 400
        self.crew = 4
        self.hardpoints = 4
        self.targeting = 1
        self.h_turns = False
        self.vh_turns = False
        self.i_turns = False

class BigRig(Vehicle):
    def __init__(self):
        self.name = 'Big Rig'
        self.description = ''''''
        self.cost = 500
        self.crew = 5
        self.hardpoints = 5
        self.targeting = 2
        self.m_turns = False
        self.h_turns = False
        self.vh_turns = False
        self.i_turns = False
