from src.classes.gameObjects.Enemy import Enemy
from src.classes.utils.Vector import Vector
from src.pplay.sprite import Sprite
from src.classes.gameObjects.projectiles.GhostProjectile import GhostProjectile
from random import randint

class Ghost(Enemy):

    STATES = {
        'IDLE': 0,
        'HIDDEN': 1,
        'ATTACKING': 2,
    }

    def __init__(self, wave):
        super().__init__(wave)
        
        """ Vida do Ghost """
        self.life = 10

        """ Booleana """
        self.hidden = False
        
        """ Velocidade do fantasma """
        self.baseSpeed = Vector(0, 0)

        """ Estado do Ghost """
        self.state = Ghost.STATES.get('IDLE')
        
        """ Duração do modo escondido """
        self.invencibilityDuration = 3.5

        """ Duração do modo idle """
        self.idleDuration = 1.8

        """ Intervalo até o disparo do projetil """
        self.attackDelay = 1.2

        self.timer = self.idleDuration
        self.projectileDistance = 500
        self.projectileSpeed = 200

        self.gameObject = Sprite('./assets/images/ghost.png')

    def setState(self, state):
        self.state = Ghost.STATES[state]

    def inState(self, state):
        return self.state == Ghost.STATES[state]

    def getRandomPosition(self):
        window = self.wave.window
        randomX = randint(0, window.width - self.width)
        randomY = randint(0, window.height - self.height)

        return Vector(
            randomX,
            randomY
        ) 

    def draw(self):
        if (not self.inState('HIDDEN')):
            self.gameObject.draw()
    
    # -> Loop do Ghost
    # 1. 
    def loop(self):
        super().loop()

        window = self.wave.window
        player = self.wave.game.player

        if(self.timer <= 0):
            if (self.inState('IDLE')):
                self.setState('HIDDEN')
                self.timer = self.invencibilityDuration

            elif (self.inState('HIDDEN')):
                randomPosition = self.getRandomPosition()
                self.x = randomPosition.x
                self.y = randomPosition.y
                self.setState('ATTACKING')
                self.timer = self.attackDelay

            elif (self.inState('ATTACKING')):
                rect = self.getRect()
                proj = GhostProjectile(self.wave.game)
                proj.x = rect.center[0]
                proj.y = rect.center[1]
                proj.launch()

                self.setState('IDLE')
                self.timer = self.idleDuration


        self.timer -= window.delta_time()
