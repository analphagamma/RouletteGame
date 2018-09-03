import sys
from modules import *

class InvalidTableLimit(Exception):
    pass
    
def main():
    table_limit, strategy = sys.argv[1], sys.argv[2]
    
    try:
        int(table_limit)
    except ValueError:
        print('Table limit is not a number!\nExiting!')
        sys.exit(1)
        
    all_players = {}
    for pl_sc in players.Player.__subclasses__():
        all_players[pl_sc.__name__] = pl_sc

    try:
        all_players[strategy]
    except KeyError:
        print('Player strategy not defined!\nExiting!')
        sys.exit(1)
    
    wh = wheel.Wheel()
    bb = binbuilder.BinBuilder()
    bb.buildBins(wh)
    t = table.Table(int(table_limit))
    game = roulettegame.RouletteGame(wh, t)
    pl = all_players[strategy](t)

    sim = simulator.Simulator(pl, game)
    result = sim.gather()
    print('Rounds played:{}\nMaximum stakes:{}'.format(result[0], result[1]))
    print('Average game length: {}, Deviation: {}'.format(integerstatistics.IntegerStatistics.mean(result[0]), integerstatistics.IntegerStatistics.stdev(result[0])))
    print('Average stake: {}, Deviation: {}'.format(integerstatistics.IntegerStatistics.mean(result[1]), integerstatistics.IntegerStatistics.stdev(result[1])))

if __name__ == '__main__':
    main()
