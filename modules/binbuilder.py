from modules.outcome import Outcome

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
