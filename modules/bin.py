class Bin:
    ''' The Bin object represents a result, a bin on the Wheel
        It contains all the possible Outcomes that includes this result'''
        
    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        ''' Adds an additional Outcome to the frozenset'''
        self.outcomes |= set([outcome])

    def __eq__(self, other: object):
        if self.outcomes == other.outcomes:
            return True
        else:
            return False

    def __str__(self):
        ''' Returns all the Outcome objects'''
        return ', '.join(map(str, self.outcomes))
