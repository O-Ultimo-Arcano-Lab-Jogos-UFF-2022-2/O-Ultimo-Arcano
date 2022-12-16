class WaveManager():

    def __init__(self, window, waves):
        self.window = window
        self.waves = waves
        self.wavesCount = len(self.waves)

        self.current = 0
        self.wave = None
        self.nextWave()

    def nextWave(self):
        self.wave = self.waves[self.current]

    def loop(self):
        aliveEnemies = self.wave.loop()

        if (aliveEnemies == 0):
            if (self.current == self.wavesCount - 1):
                self.window.gameOver = True
                self.window.playerHasWon = True
            else:
                self.current += 1
                self.nextWave()

    def draw(self):
        self.wave.draw()
