class CrewMember:
    def __init__(self):
        self.control = 0
        self.attack = 0
        self.defence = 0
        self.accelerate = 0
        self.decelerate = 0

class Psycho(CrewMember):
    def __init__(self):
        self.name = 'Psycho'
        self.description = ''''''
        self.cost = 150
        self.attack = 1
        self.accelerate = 2
        self.decelerate = -1

class AverageJoe(CrewMember):
    def __init__(self):
        self.name = 'Average Joe'
        self.description = ''''''
        self.cost = 0

class TheProfessional(CrewMember):
    def __init__(self):
        self.name = 'The Professional'
        self.description = ''''''
        self.cost = 150
        self.defence = 1
        self.accelerate = 1
        self.decelerate = 1

class SteadyEddie(CrewMember):
    def __init__(self):
        self.name = 'Steady Eddie'
        self.description = ''''''
        self.cost = 75
        self.control = 1
        self.decelerate = 2

class Leadfoot(CrewMember):
    def __init__(self):
        self.name = 'Leadfoot'
        self.description = ''''''
        self.cost = 75
        self.accelerate = 3

class CoolHand(CrewMember):
    def __init__(self):
        self.name = 'Cool Hand'
        self.description = ''''''
        self.cost = 175
        self.control = 1

class Outcast(CrewMember):
    def __init__(self):
        self.name = 'Outcast'
        self.description = ''''''
        self.cost = 125
        self.control = 1
        self.attack = 1
        self.defence = 1
        self.accelerate = 1
        self.decelerate = 1

class DeadEye(CrewMember):
    def __init__(self):
        self.name = 'Dead Eye'
        self.description = ''''''
        self.cost = 100
        self.attack = 1

class Sarge(CrewMember):
    def __init__(self):
        self.name = 'Sarge'
        self.description = ''''''
        self.cost = 175
        self.attack = 2
        self.defence = 1

class HotStuff(CrewMember):
    def __init__(self):
        self.name = 'Hot Stuff'
        self.description = ''''''
        self.cost = 125

class GetawayDriver(CrewMember):
    def __init__(self):
        self.name = 'Getaway Driver'
        self.description = ''''''
        self.cost = 175
        self.control = 3
        self.accelerate = 3
        self.decelerate = 3

class AIModule(CrewMember):
    def __init__(self):
        self.name = 'AI Module'
        self.description = ''''''
        self.cost = 225
        self.control = 2
        self.attack = 1
        self.accelerate = 1
        self.decelerate = 2

class GreaseMonkey(CrewMember):
    def __init__(self):
        self.name = 'Grease Monkey'
        self.description = ''''''
        self.cost = 50
        self.control = 1
