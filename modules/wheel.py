import random
from modules.outcome import Outcome
from modules.bin import Bin

class Wheel:
    ''' The Wheel object is a collection of Bin objects
        It can pick a random Bin to represent the roll of the roulette Wheel.
        It can initialized with a subclass of random.random for
        testing purposes, otherwise it defaults to random. '''
        
    def __init__(self, rng=random):
        self.rng = rng
        self.bins = tuple(Bin() for i in range(38))
        self.all_outcomes = []

    def addOutcome(self, number: int, outcome: Outcome):
        ''' Adds the given Outcome to the Bin with the given number
            index 37 stands for the number '00' '''
        try:
            for oc in outcome:
                self.bins[number].add(oc)
                self.all_outcomes.append(oc)
        except TypeError:
            self.bins[number].add(outcome)
            self.all_outcomes.append(outcome)
            
    def getOutcome(self, name: str):
        return set([oc.__str__() for oc in self.all_outcomes if name in oc.name])

    def next_roll(self):
        ''' Picks a random Bin and returns it '''
        return self.rng.choice(self.bins)

    def get_bin(self, bin_index: int):
        ''' Returns the Bin object of the given index from this Wheel Object'''
        return self.bins[bin_index]

    def binIterator(self):
        ''' Returns a set of all Outcomes
            :returns:
                set'''
        return set(self.all_outcomes)
