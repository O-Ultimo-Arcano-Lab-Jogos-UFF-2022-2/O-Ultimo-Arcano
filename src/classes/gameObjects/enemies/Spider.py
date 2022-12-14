from src.classes.gameObjects.Enemy import Enemy
from src.pplay.sprite import Sprite
from src.classes.utils.Vector import Vector
from src.helpers.random import randomNumber
from math import cos, sin, radians
from src.classes.gameObjects.CircularHitbox import CircularHitbox


class Spider(Enemy):
    """ Vida do Spider. Este valor pode ser ajustado. """
    MAX_HP = 20

    """ Intervalo entre as explosões (em segundos). """
    EXPLOSION_COOLDOWN = 2.5

    def __init__(self, wave):
        super().__init__(wave)

        """ Velocidade base do Spider. """
        self.baseSpeed = Vector(140, 140)

        """ Gera uma direção inicial aleatória. """
        self.direction = self.randomDirection()

        """ Offset do arco que representa as direções 
        para qual o Spider pode virar. """
        self.arcOffset = 10

        """ Dano da explosão """
        self.explosionDamage = 20

        """ Duração da explosão (em frames) """
        self.explosionDuration = 16

        """ Booleana indicando se o Spider deve virar
        ou não. Normalmente isso é True quando a aranha
        está para colidir com a parede. """
        self.shouldTurn = False

        self.timer = self.EXPLOSION_COOLDOWN

        self.speed = self.baseSpeed\
            .copy()\
            .setDirection(self.direction)

        """ @TODO Trocar o sprite pro da aranha """
        self.gameObject = Sprite('./assets/images/spider.png', 1)

    """ Vira o Spider na direção do jogador.  """

    def turn(self):
        vectorToPlayer = Vector.fromObjects(
            self, self.wave.game.player.gameObject)
        rotationAngle = randomNumber(-self.arcOffset, self.arcOffset)

        self.speed = self.baseSpeed\
            .copy()\
            .setDirection(vectorToPlayer.rotateBy(rotationAngle))

    def randomDirection(self, arcStart=0, arcEnd=360):
        randDegrees = radians(randomNumber(arcStart, arcEnd))
        return Vector(cos(randDegrees), sin(randDegrees))

    def handleExplosionCollision(self, collisions):
        player = self.wave.game.player
        player.takeHit(self.explosionDamage)

    def createExplosion(self):
        player = self.wave.game.player
        hit = CircularHitbox(
            120,
            [player],
            self.explosionDuration,
            self.handleExplosionCollision,
            Sprite('./assets/images/spider_web.png', 1)
        )
        hit.x = self.x - hit.width / 2 + self.width / 2
        hit.y = self.y - hit.height / 2 + self.height / 2

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
        super().loop()

        player = self.wave.game.player
        window = self.wave.window

        # PROVISÓRIO
        if (self.shouldTurn):
            self.turn()
            self.shouldTurn = False

        if (self.timer <= 0):
            self.createExplosion()
            self.timer = self.EXPLOSION_COOLDOWN

        self.timer -= window.delta_time()
        self.shouldTurn = self.willBeInWindownEdge()
        self.x += self.speed.x * window.delta_time()
        self.y += self.speed.y * window.delta_time()
