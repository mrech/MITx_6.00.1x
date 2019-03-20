class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print(self.time)


boston_clock = Clock('5:30')
# Aliasing: two identifier referencing the same object
# mutable objects: change the attribute of both object are referencing
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # special method that returns a string that looks like a valid Python expression
    # that could be used to recreate an object with the same value
    def __repr__(self):
        return 'Coordinate(' + str(self.getX())+','+str(self.getY())+')'

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'


c1 = Coordinate(3, 2)
# print in __str__ method
print(c1)
c2 = Coordinate(3, 4)
# Add an __eq__ method that returns True if coordinates refer to same point in the plane
c1 == c2
c3 = Coordinate(3, 4)
c3 == c2
# Return the canonical string representation of the object.
repr(c1)
eval(repr(c1)) == c1


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    # not passed an initial value for vals
    def __init__(self, vals=None):
        """Create an empty set of integers"""
        if vals == None:
            self.vals = []
        else:
            self.vals = vals

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def getVals(self):
        return self.vals

    # retruns a new inSet containing elements that appear in both sets
    def intersect(self, other):
        return intSet({i for i in self.vals if i in other.getVals()})

    # Add the appropriate method(s) so that len(s) returns the number of elements in s
    def __len__(self):
        return len(self.vals)


s = intSet()
print(s)
s.insert(1)
s.insert(4)
s1 = {-19, -17, -11, -7, -3, 3, 8, 9, 15, 18}
s.intersect(s1)
len(s)

setA = intSet()
setA.insert(-20)
setA.insert(-14)
setA.insert(8)
setA.insert(10)

setB = intSet()
setB.insert(-11)
setB.insert(4)
setB.insert(8)
setB.insert(10)

setC = setA.intersect(setB)
setC.getVals()

# HIERARCHY


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
