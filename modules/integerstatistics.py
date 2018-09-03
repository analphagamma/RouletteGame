from statistics import mean, stdev

class IntegerStatistics():
    ''' Computes simple integer statistics from list inputs
        Its methods are static methods so no instances have to be
        created. '''

    @staticmethod
    def mean(values: list):
        ''' Calculates the arithmetic mean of the integer elements
            of the list.

            :returns:
                float '''
        return round(mean(values), 5)
    
    def stdev(values: list):
        ''' Calculates the standard deviation of the integer
            elements of the list.

            :returns:
                float '''
        return round(stdev(values), 5)
