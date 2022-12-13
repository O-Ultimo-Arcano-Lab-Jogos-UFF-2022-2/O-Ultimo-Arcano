from src.classes.gameObjects.Enemy import Enemy
from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from time import sleep


class Goblin(Enemy):
    """ 
    # Estados do Goblin:
    Normal => Ele está so andando na direção do player
    esperando para poder começar o dash.

    Charging => O Goblin desacelera e começa a carregar
    o dash.

    Dashing => O Goblin está dando o dash em alta velocidade.
    """
    STATES = {
        'NORMAL': 0,
        'CHARGING': 1,
        'DASHING': 2
    }

    def __init__(self, wave):
        super().__init__(wave)

        """ Vida do Goblin. Este valor pode ser ajustado. """
        self.life = 10

        """ Velocidade base do Goblin. É em cima dele que 
        os cálculos de velocidade serão feitos. Este valor
        não deve ser alterado em tempo de execução. """
        self.baseSpeed = Vector(140, 140)

        """ O vetor da velocidade. Em cada loop ele é 
        atualizado. """
        self.speed = Vector(0, 0)

        """ Distância em px que o dash irá percorrer. """
        self.dashDistance = 240

        """ Porcentagem de slow o Goblin irá sofrer enquanto
        estiver carregando. """
        self.slowPercentage = 0.7

        """ O tempo em segundos que o charge irá durar. """
        self.chargeDuration = 1.2

        """ Tempo em segundos que o Goblin levará para
        completar o dash. """
        self.dashDuration = 0.3

        """ Vetor de direção do dash. Quando o charge termina
        este valor é atualizado com a direção do dash. """
        self.dashDirection = None

        """ Tempo em segundos que o Goblin irá esperar para
        começar a carregar o próximo dash. """
        self.dashCooldown = 2

        """ Timer interno do Goblin. Quando necessário, recebe
        um tempo para contar de forma decrescrente, até chegar
        no 0"""
        self.timer = 0

        """ O estado atual do Goblin. """
        self.state = Goblin.STATES['NORMAL']

        # @TODO Trocar o sprite
        self.gameObject = Sprite('./assets/images/goblin.png', 1)

    """ 
    Getters & Setters
    """

    def getSlowedSpeed(self):
        return self.baseSpeed * (1 - self.slowPercentage)

    def getDashSpeed(self):
        speed = self.dashDistance / self.dashDuration
        return Vector(speed, speed)

    def setState(self, state: str):
        self.state = Goblin.STATES[state]

    """ 
    Misc
    """

    def inState(self, state: str):
        return self.state == Goblin.STATES[state]

    # Loop do Goblin:

    def loop(self):
        player = self.wave.game.player.gameObject
        window = self.wave.window

        # Gera um vetor unitário que vai deste inimigo
        # ao player para pegar a direção da velocidade.
        vectorDirection = Vector.fromObjects(self, player).unit()

        # Quando o Goblin estiver normal, ele irá...
        if (self.inState('NORMAL')):
            if (self.timer <= 0 and self.distance_to(player) < self.dashDistance * 0.8):
                # Se puder, começar a carregar o dash...
                self.setState('CHARGING')
                self.timer = self.chargeDuration
            else:
                # Se não, irá continuar seguindo o player.
                self.speed = self.baseSpeed.copyDirection(vectorDirection)

        # Se ele estiver carregando o dash...
        if (self.inState('CHARGING')):
            # Irá se desacelerar...
            slowedSpeed = self.getSlowedSpeed()

            if (self.timer <= 0):
                # Começar o dash, se terminou de carregar...
                self.setState('DASHING')
                self.dashDirection = vectorDirection
                self.timer = self.dashDuration
            else:
                # Ou irá continuar carregando se ainda não terminou
                # de carregar.
                self.speed = slowedSpeed.setDirection(vectorDirection)

        # Por fim, se estiver dando dash...
        if (self.inState('DASHING')):
            # Receberá uma alta velocidade enquanto não chegar
            # no final...
            self.speed = self\
                .getDashSpeed()\
                .copyDirection(self.dashDirection)

            # E então, irá voltar ao normal.
            if (self.timer <= 0):
                self.setState('NORMAL')
                self.timer = self.dashCooldown

        self.timer -= window.delta_time()
        self.x += self.speed.x * window.delta_time()
        self.y += self.speed.y * window.delta_time()
