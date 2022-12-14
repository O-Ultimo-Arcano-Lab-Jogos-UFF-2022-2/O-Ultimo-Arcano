from src.classes.gameObjects.Enemy import Enemy
from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from src.helpers.random import randomNumber
from math import cos, sin, radians

class Spider(Enemy):

    def __init__(self, wave):
        super().__init__(wave)

        """ Vida do Spider """
        self.life = 20

        """ Velocidade base do Spider. """
        self.baseSpeed = Vector(140, 140)

        """ Gera uma direção inicial aleatória. """
        self.direction = self.randomDirection()

        """ Offset do arco que representa as direções 
        para qual o Spider pode virar. """
        self.arcOffset = 10

        """ Booleana indicando se o Spider deve virar
        ou não. Normalmente isso é True quando a aranha
        está para colidir com a parede. """
        self.shouldTurn = False

        self.speed = self.baseSpeed\
            .copy()\
            .setDirection(self.direction)

        """ @TODO Trocar o sprite pro da aranha """
        self.gameObject = Sprite('./assets/images/goblin.png', 1)

    """ Vira o Spider na direção do jogador.  """
    def turn(self):
        vectorToPlayer = Vector.fromObjects(self, self.wave.game.player.gameObject)
        rotationAngle = randomNumber(-self.arcOffset, self.arcOffset) 

        self.speed = self.baseSpeed\
            .copy()\
            .setDirection(vectorToPlayer.rotateBy(rotationAngle))
        
    
    def randomDirection(self, arcStart = 0, arcEnd = 360):
        randDegrees = radians(randomNumber(arcStart, arcEnd))
        return Vector(cos(randDegrees), sin(randDegrees))

    # -> Loop do spider:
    # 1. Verifica se o Spider enconstou na parede
    # (if colidiu) Muda a direção para tentar acertar o jogador
    # 
    # 2. Verifica se o Spider colidiu com o jogador
    # (if colidiu) Aplica um dano ao jogador
    #
    # 3. Verifica se o intervalo entre as explosões (explosionCooldown) 
    # ja terminou
    # (if explosionCooldown == 0) Gera uma nova explosão e reseta o cd.
    #
    # 4. Anda na direção que está escolhida como atualmente.
    def loop(self):
        player = self.wave.game.player.gameObject
        window = self.wave.window

        # PROVISÓRIO
        if (self.shouldTurn):
            self.turn()
            self.shouldTurn = False

        self.shouldTurn = self.willBeInWindownEdge()
        self.x += self.speed.x * window.delta_time()
        self.y += self.speed.y * window.delta_time()

        
