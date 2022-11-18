class WaveManager():
     
    def __init__(self, window, waves):
        self.window = window
        self.waves = waves
        self.wavesCount = len(self.waves)
        
        self.current = -1
        self.wave = None
        self.nextWave()


    def nextWave(self):
        if (self.current == self.wavesCount):
            return

        self.current += 1
        self.wave = self.waves[self.current]
        

    def loop(self):
        if (self.current == self.wavesCount):
            return

        aliveEnemies = self.wave.loop()

        if (aliveEnemies == 0):
            self.nextWave()

    def draw(self):
        self.wave.draw()

        