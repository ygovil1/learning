#
class Planet():
    pass


class Star():
    # store mass and radius in terms of solar mass and radius
    # store name
    def __init__(self, mass=1., radius=1., name='Sol'):
        self.mass = mass
        self.radius = radius
        self.name = name

    # to string method format:
    # name: mass 'M_sun,' radius 'R_sun'
    def __str__(self):
        return '{0} + :  + {1:.2f} +  M_sum,  + {2:.2f} +  R_sun'.format(name, mass,radius)
        


class System():
    pass
