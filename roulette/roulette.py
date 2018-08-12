import random


class Outcome:
    ''' The Outcome object holds a bet's name and its odds
        It can return the amount won if the bet was successful '''
        
    def __init__(self, name: str, odds: int):
        self.name = name
        self.odds = odds

    def winAmount(self, amount: int):
        return amount * self.odds

    def __eq__(self, other: object):
        if self.name == other.name:
            return True
        else:
            return False

    def __ne__(self, other: object):
        if self.name != other.name:
            return True
        else:
            return False

    def __str__(self):
        return '{} (odds {}:1)'.format(self.name, self.odds)

    def __hash__(self):
        return 0

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

class BinBuilder:

    def generateStraightBets(self, number: str):
        ''' Returns an Outcome for a bet
            on a single number '''
        return Outcome('Number ' + number, 35)

    def generateSplitBets(self, number: str):
        ''' Returns Outcomes for a bet
            on 2 numbers '''
        down = str(int(number)+3)
        up = str(int(number)-3)
        right = str(int(number)+1)
        left = str(int(number)-1)


        # case 1
        if number == '1':
            return (Outcome('Split ' + '-'.join([number, right]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        # case 2
        elif number == '2':
            return (Outcome('Split ' + '-'.join([left, number]), 17),
                    Outcome('Split ' + '-'.join([number, right]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        # case 3
        elif number == '3':
            return (Outcome('Split ' + '-'.join([left, number]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        # case 34
        elif number == '34':
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([number, right]), 17))
        # case 35
        elif number == '35':
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([left, number]), 17),
                    Outcome('Split ' + '-'.join([number, right]), 17))
        # case 36
        elif number == '36':
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([left, number]), 17))
        # case left column
        elif int(number) % 3 == 1:
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([number, right]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        # case middle column
        elif int(number) % 3 == 2:
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([left, number]), 17),
                    Outcome('Split ' + '-'.join([number, right]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        # case right column
        elif int(number) % 3 == 0:
            return (Outcome('Split ' + '-'.join([up, number]), 17),
                    Outcome('Split ' + '-'.join([left, number]), 17),
                    Outcome('Split ' + '-'.join([number, down]), 17))
        
            
    def generateStreetBets(self, number: str):
        ''' Returns Outcomes for a bet on
            3 numbers in a row'''
        streets = [[i+k for i in range(3)] for k in range(1, 37, 3)]
        for street in streets:
            if int(number) in street:
                return Outcome('Street ' + '-'.join([str(street[0]),
                                                     str(street[1]),
                                                     str(street[2])]), 11)
        
    def generateCornerBets(self, number: str):
        ''' Returns Outcomes for a bet on
            4 adjacent numbers in a corner'''
        topright = [str(int(number)-1),
                    number,
                    str(int(number)+2),
                    str(int(number)+3)]
        topleft = [number,
                   str(int(number)+1),
                   str(int(number)+3),
                   str(int(number)+4)]
        bottomright = [str(int(number)-4),
                       str(int(number)-3),
                       str(int(number)-1),
                       number]
        bottomleft = [str(int(number)-3),
                      str(int(number)-2),
                      number,
                      str(int(number)+1)]

        # case 1
        if number == '1':
            return Outcome('Corner ' + '-'.join(topleft), 11)
        # case 2
        elif number == '2':
            return (Outcome('Corner ' + '-'.join(topright), 11),
                    Outcome('Corner ' + '-'.join(topleft), 11))
        # case 3
        elif number == '3':
            return Outcome('Corner ' + '-'.join(topright), 11)
        # case 34
        elif number == '34':
            return Outcome('Corner ' + '-'.join(bottomleft), 11)
        # case 35
        elif number == '35':
            return (Outcome('Corner ' + '-'.join(bottomright), 11),
                    Outcome('Corner ' + '-'.join(bottomleft), 11))
        # case 36
        elif number == '36':
            return Outcome('Corner ' + '-'.join(bottomright), 11)
        # case left column
        elif int(number) % 3 == 1:
            return (Outcome('Corner ' + '-'.join(bottomleft), 11),
                    Outcome('Corner ' + '-'.join(topleft), 11))
        # case middle column
        elif int(number) % 3 == 2:
            return (Outcome('Corner ' + '-'.join(bottomright), 11),
                    Outcome('Corner ' + '-'.join(bottomleft), 11),
                    Outcome('Corner ' + '-'.join(topright), 11),
                    Outcome('Corner ' + '-'.join(topleft), 11))
        # case right column
        elif int(number) % 3 == 0:
            return (Outcome('Corner ' + '-'.join(bottomright), 11),
                    Outcome('Corner ' + '-'.join(topright), 11))

    def generateLineBets(self, number: str):
        ''' Returns Outcomes for a bet on
            2 lines (6 numbers)'''
        lines = [[i+k for i in range(6)] for k in range(1, 37, 3)]
        lines = [list(map(str, (n for n in line))) for line in lines]
        # case 5 items with wildcards
        if number in ['0', '00']:
           return Outcome('Line 0-00-1-2-3', 5)
        # case 1-2-3
        elif int(number) < 4:
            return (Outcome('Line 0-00-1-2-3', 5),
                    Outcome('Line 1-2-3-4-5-6', 5))
        # case 34-35-36
        elif int(number) > 33:
            return Outcome('Line 31-32-33-34-35-36', 5)
        # other regular cases
        else:
            outcome_lines = []
            for line in lines:
                if number in line:
                    outcome_lines.append(line)
            outcomes = tuple(Outcome('Line ' + '-'.join(oc), 5) for oc in outcome_lines)
            return outcomes    

    def generateDozenBets(self, number: str):
        ''' Return Outcomes for a bet on
            12 numbers of one of the 3 groups'''
        if 0 < int(number) < 13:
            d = '1'
        elif 12 < int(number) < 25:
            d = '2'
        elif 24 < int(number) < 37:
            d = '3'

        return Outcome('Dozen ' + d, 2)

    def generateColumnBets(self, number: str):
        ''' Returns Outcomes for a bet on
            a whole column of numbers'''
        if int(number) % 3 == 1:
            col = '1'
        elif int(number) % 3 == 2:
            col = '2'
        else:
            col = '3'
        return Outcome('Column ' + col, 2)

    def generateRedBlackBets(self, number: str):
        ''' Returns an Outcome for a Red or Black bet'''
        reds = [1,3,5,7,9,12,14,16,18,
                19,21,23,25,27,30,32,34,36]
        reds = list(map(str, (n for n in reds)))
        if number in reds:
            return Outcome('Red', 1)
        else:
            return Outcome('Black', 1)

    def generateEvenOddBets(self, number: str):
        ''' Returns an Outcome for an Even or Odd bet'''
        if number in ['0', '00']:
            return (Outcome('Even', 1),
                    Outcome('Odd', 1))
        elif int(number) % 2 == 0:
            return Outcome('Even', 1)
        else:
            return Outcome('Odd', 1)
            
    def generateHighLowBets(self, number: str):
        ''' Returns an Outcome for a High or a Low bet'''
        if int(number) < 19:
            return Outcome('Low', 1)
        else:
            return Outcome('High', 1)
         
    def buildBins(self, wheel):
        ''' Creates Outcome instances and adds each Outcome
            in the appropriate Bins of the given Wheel'''

        bets = [self.generateStraightBets, self.generateSplitBets,
                self.generateStreetBets, self.generateCornerBets,
                self.generateLineBets, self.generateDozenBets,
                self.generateColumnBets, self.generateRedBlackBets,
                self.generateEvenOddBets, self.generateHighLowBets]
        for i in range(1, 37):
            for bet in bets:
                wheel.addOutcome(i, bet(str(i)))

        for index, number in [(0, '0'), (37, '00')]:
                wheel.addOutcome(index, self.generateStraightBets(number))
                wheel.addOutcome(index, self.generateLineBets(number))
                wheel.addOutcome(index, self.generateEvenOddBets(number))

class Bet:
    ''' Constructed by the Player class
        It contains an Outcome and the amount '''

    def __init__(self, amountBet: int, outcome: Outcome):
        self.amountBet = amountBet
        self.outcome = outcome

    def winAmount(self):
        ''' Returns the amount won:
            the amount bet multiplied by the outcome odds '''
        return self.outcome.winAmount(self.amountBet)

    def loseAmount(self):
        ''' Returns the amount lose '''
        return -(self.amountBet)

    def __str__(self):
        return '${} on {}'.format(self.amountBet, self.outcome)

    def __eq__(self, other: object):
        if self.amountBet == other.amountBet and self.outcome == other.outcome:
            return True
        else:
            return False
    
class Table:
    ''' Contains all the Bets created by the Player object
        It is defined by the betting limit '''

    def __init__(self, limit: int):
        self.limit = limit
        self.bets = []

    def isValid(self, bet: Bet):
        ''' Checks whether the sum of all bets including the added Bet
            is under the bet limit '''
            
        if sum(bet.amountBet for bet in self.bets) + bet.amountBet <= self.limit:
            return True
        else:
            return False

    def placeBet(self, bet: Bet):
        ''' Checks whether the addition of the new bet is valid
            and if it is it adds the bet to self.bets
            if it is invalid it raises InvalidBet '''
            
        if self.isValid(bet):
            self.bets.append(bet)
        else:
            raise InvalidBet('The addition of this bet is invalid because it exceeds the Table limit')

    def clearBets(self):
        self.bets = []
        
    def __iter__(self):
        all_bets = (bet for bet in self.bets)
        return all_bets

    def __str__(self):
        bet_lst = []
        for bet in self.__iter__():
            bet_lst.append(bet.__str__())
        return ', '.join(bet_lst)

class InvalidBet(Exception):
    ''' Custom exception for the cases when and invalid bet is placed '''
    pass

class RouletteGame:
    ''' Main game class
        It's made up of a Wheel and a Table object
        It's used by Player to make Bets '''
        
    def __init__(self, wheel: Wheel, table: Table):
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        ''' Main game loop
            first Bets are placed by Players,
            then the Wheel is spun,
            then the Outcomes are compared '''

        # Bets placed if Player is still playing  
        if not player.playing():
            return

        self.table.clearBets() # clear the table
        player.placeBets() # place bets
        roll = self.wheel.next_roll() # Roll
        player.roundsToGo -= 1
        player.winners(roll.outcomes) # sends winner Outcomes to Player
        
        # Outcomes are compared
        for bet in self.table:
            player.stake -= bet.amountBet
            if player.stake < 0:
                player.stake = 0
                return
            if bet.outcome in roll.outcomes:
                return player.win(bet)
            else:
                return player.lose(bet)

class Player:
    ''' This class is responsible to create Bets from valid Outcomes
        and within the Table's limit.
        It manages its account'''
        
    def __init__(self, table: Table):
        self.table = table
        self.roundsToGo = 0
        self.stake = 0

    def setStake(self, stake: int):
        ''' Sets the Player's stake. '''
        self.stake = stake

    def setRounds(self, rounds: int):
        ''' Sets the number of rounds the Player
            would play. '''
        self.roundsToGo = rounds
        
    def placeBets(self):
        ''' No body for super class. '''
        pass

    def playing(self):
        ''' Returns True if the Player is still active. '''
        if self.stake <= 0 or self.roundsToGo == 0:
            return False
        else:
            return True

    def winners(self, outcomes: set):
        ''' Returns the set of the most recent cycle's
            winner Outcomes.
            In this parent class this method simply returns the
            Outcomes.
            :returns:
                set. '''
        pass

    def win(self, bet: Bet):
        ''' When notified by Game it increases the Player's
            stake by using the Bet's winAmount() method'''
        self.stake += bet.winAmount() + bet.amountBet

    def lose(self, bet: Bet):
        ''' Because the amount bet is already deducted from the
            stake this method does nothing for now. '''
        pass

class Passenger57(Player):
    ''' A Player class that only bets on Black. '''
    
    def __init__(self, table: Table):
        
        self.table = table
        self.black = Outcome('Black', 1)
        self.stake = 0
        self.roundsToGo = 0

    def placeBets(self):
        ''' Places $10 on Black. '''
        self.table.placeBet(Bet(10, self.black))

        
class Martingale(Player):
    ''' Subclass of Player
        This Player uses the Martingale strategy, that is
        doubling the bet after every loss and returning to the default
        bet after every win until reaching the Table limit. '''

    # number of losses. It updates the self.betMultiple variable
    
    
    def __init__(self, table):
        # Starts at 1 and is reset to 1 on each win and is
        # doubled with in each loss.
        self.table = table
        self.stake = 0
        self.roundsToGo = 0
        self.lossCount = 0
        self.betMultiple = 1
        self.black = Outcome('Black', 1)

    def placeBets(self):
        self.table.placeBet(Bet(self.betMultiple, self.black))

    def win(self, bet: Bet):
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)
        super(Martingale, self).win(bet)

    def lose(self, bet: Bet):
        self.lossCount += 1
        if pow(2, self.lossCount) < self.table.limit:
            self.betMultiple = pow(2, self.lossCount)
        super(Martingale, self).lose(bet)

class SevenReds(Player):
    ''' This Player waits for seven Red wins in a row and then bets
        black.
        There are 2 states of this class: waiting, and betting. '''

    def __init__(self, table):
        self.table = table
        self.redCount = 0
        self.lossCount = 0
        self.betMultiple = 1
        self.black = Outcome('Black', 1)
               
    def winners(self, outcomes: set):

        for oc in outcomes:
            if oc.name == 'Red':
                self.redCount += 1

    def placeBets(self):
        if self.redCount == 7:
            self.table.placeBet(Bet(self.betMultiple, self.black))

    def win(self, bet: Bet):
        self.lossCount = 0
        self.betMultiple = pow(2, self.lossCount)
        super(SevenReds, self).win(bet)

    def lose(self, bet: Bet):
        self.lossCount += 1
        if pow(2, self.lossCount) < self.table.limit:
            self.betMultiple = pow(2, self.lossCount)
        super(SevenReds, self).lose(bet)

class Simulator():
    ''' Main body of the application.
        Creates Wheel, Table and Game objects.
        Simulates sessions
        Initializes Players and Games
        Outputs a final statistical summary of the results. '''


    def __init__(self, player: Player, game):
        self.player = player
        self.game = game

        self.initDuration = 250 # maximum number of bets in a game cycle
        self.initStake = 100 # starting amount of betting money
        self.samples = 50 # number of game cycles to simulate
        
    def session(self):
        ''' Executes a single game sessions.
            It runs until the player.playing() is false.
            
            :returns:
                list '''
        stakeVals = []
        self.player.setStake(self.initStake)
        self.player.setRounds(self.initDuration)

        while self.player.playing():
            self.game.cycle(self.player)
            stakeVals.append(self.player.stake)
        
        return stakeVals

    def gather(self):
        ''' Executes a number of games sessions in samples.

            :returns:
                tuple of 2 lists '''
        durations = [] # list of length the player remained in the game
        maxima = [] # list of maximum stakes for each player

        for n in range(self.samples):
            stakes = self.session()
            durations.append(self.player.roundsToGo)
            maxima.append(max(stakes))

        return (durations, maxima)

def main(table_limit, strategy):
    player_types = ['Passenger57', 'Martingale', 'SevenReds']
    players = {}
    for pt, sc in zip(player_types, Player.__subclasses__()):
        players[pt] = sc
    
    wh = Wheel()
    bb = BinBuilder()
    bb.buildBins(wh)
    t = Table(table_limit)
    game = RouletteGame(wh, t)
    pl = players[strategy](t)

    sim = Simulator(pl, game)
    result = sim.gather()
    print('Rounds left:{}\nMaximum stakes:{}'.format(result[0], result[1]))
