import unittest
from context import wheel, binbuilder, table, roulettegame, players
from wheeltest import NonRandom

class RouletteGameTest(unittest.TestCase):
    
    def test1_win(self):
        ''' Tests winning process. '''

        nrnd = NonRandom(2)
        wh = wheel.Wheel(nrnd)
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)
        pl.setStake(100)
        pl.setRounds(10)

        self.assertEqual(pl.stake, 100)
        game.cycle(pl)
        self.assertEqual(pl.stake, 110)

    def test2_loss(self):
        ''' Tests losing process. '''
        
        nrnd = NonRandom(1)
        wh = wheel.Wheel(nrnd)
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)
        pl.setStake(100)
        pl.setRounds(10)

        self.assertEqual(pl.stake, 100)
        game.cycle(pl)
        self.assertEqual(pl.stake, 90)

    def test3_outofmoney(self):
        ''' Tests if the cycle breaks when the Player's stake is zero '''

        nrnd = NonRandom(1)
        wh = wheel.Wheel(nrnd)
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)
        pl.setStake(100)
        pl.setRounds(10)

        while pl.playing():
            game.cycle(pl)

        self.assertEqual(pl.stake, 0)

    def test4_nomorerounds(self):
        nrnd = NonRandom(2)
        wh = wheel.Wheel(nrnd)
        bb = binbuilder.BinBuilder()
        bb.buildBins(wh)
        t = table.Table(100)
        game = roulettegame.RouletteGame(wh, t)        
        pl = players.Passenger57(t)
        pl.setStake(100)
        pl.setRounds(10)
       
        while pl.playing():
            game.cycle(pl)

        self.assertEqual(pl.roundsToGo, 0)

if __name__ == '__main__':
    unittest.main()
