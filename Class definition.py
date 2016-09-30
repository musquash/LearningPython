# Class definition
#verbessere hier den Fehler und erzeuge eine eigene Klasse.

class Car(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, factory, number_wheels):
        self.name = name
        self.factory = factory
        self.number_wheels = number_wheels

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

Opel = Car("Corsa", "Opel", 4)
giraffe = Animal("Bruce", 1, False)
panda = Car("Skoda", "Yeti", 5)

print Opel.name, Opel.age, Opel.number_wheels
#print giraffe.name, giraffe.age, giraffe.is_hungry
#print panda.name, panda.age, panda.is_hungry
