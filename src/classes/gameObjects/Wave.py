# Propriedades
# 1. maxEnemies: number - Número máximo de inimigos vivos simuntâneamente
# 2. life: number - A vida da wave. Inicia com o número total de inimigos
#    e diminui em 1 para cada inimigo derrotado.
# 3. enemies: Enemy[] - Uma lista com as classes dos inimigos que serão
# spawnados em ordem.

# -> Instância
# 1. Recebe uma lista de inimigos
# 2. Guarda contagem para verificação
# 3. Para cada inimigo, gera uma instância, posiciona e passa
#    a instância da Wave atual.

# -> Loop
# 1. Verifica a contagem de inimigos (ini_n)
# (if) Se ini_n == 0 -> SAIDA 1
#
# 2. Verifica a contagem de inimigos vivos (ini_v_n)
# (if) Se ini_v_n == limite -> PASSO 1
# (else) -> PASSO 3
#
# 3. Verifica o timer (timer)
# (if) timer > 0 -> PASSO 3.1
# (else) -> PASSO 4
#
# 3.1 timer -= delta_time
# 3.2 -> PASSO 1
#
# 4. Spawna um inimigo em uma posição aleatória
# 5. ini_v_n += 1
# 6. timer = intervalo_entre_spawns
#
# SAIDA 1. Retorna uma booleana indicando que a wave terminou

from random import randint


class Wave():
    """ 
    Tempo de intervalo entre os spawns dos
    inimigos em segundos. 
    """
    spawnInterval = 0.75

    def __init__(self, game, window, maxEnemiesAlive, enemies, weapon):
        self.game = game
        self.window = window

        self.weapon = weapon

        self.enemies = enemies

        """
        Representa as vidas da wave. Ela perde 1 de vida
        para cada inimigo que é derrotado, até chegar a 
        a 0.
        """
        self.life = len(enemies)
        self.maxAliveEnemies = maxEnemiesAlive

        """
        Representa o índice do último inimigo spawanado.
        """
        self.lastSpawnIndex = 0

        """ 
        Contagem de inimigos vivos.
        """
        self.aliveEnemiesCount = 0

        """ 
        Timer interno para contar o intervalo entre
        os spawns de inimigo. Ele progride de modo
        decrescente, até chegar à 0.
        """
        self.timer = Wave.spawnInterval
        self.aliveEnemies = []

    """
    Spawna o próximo inimigo disponível e move
    o cursor (lastSpawnIndex) para o próximo índice
    da lista de inimigos.
    """

    def spawnEnemy(self, x=None, y=None):
        if (self.aliveEnemies == self.maxAliveEnemies):
            return

        if (self.lastSpawnIndex == len(self.enemies)):
            return

        x = randint(0, self.window.width) if x is None else x
        y = randint(0, self.window.height) if y is None else y

        enemy = self.enemies[self.lastSpawnIndex](self)
        enemy.x = x
        enemy.y = y
        self.aliveEnemies.append(enemy)
        self.aliveEnemiesCount += 1
        self.lastSpawnIndex += 1

        return enemy

    """
    Remove um inimigo da lista de inimigos e atualiza
    a contagem de inimigos vivos. Este método é acessado
    diretamente pelo inimigo quando ele identifica que 
    foi destruido.
    """

    def destroyEnemy(self, target):
        self.aliveEnemies = [
            enemy for enemy in self.aliveEnemies if enemy != target
        ]

        self.aliveEnemiesCount -= 1
        self.life -= 1

    def updateEnemies(self):
        for enemy in self.aliveEnemies:
            enemy.loop()

    def resetTimer(self):
        self.timer = Wave.spawnInterval

    # O tempo de intervalo entre os spawns só
    # começa a contar quando há algum slot para o
    # inimigo nascer.
    # Cada loop retorna a quantidade de inimigos
    # para que seja possível identificar quando a have
    # acabou.
    def loop(self):
        if (self.life == 0):
            return 0

        self.updateEnemies()

        if (self.aliveEnemiesCount < self.maxAliveEnemies or
                self.lastSpawnIndex < len(self.aliveEnemies)):
            self.timer -= self.window.delta_time()

            if (self.timer <= 0):
                self.spawnEnemy()
                self.resetTimer()

        for enemy in self.aliveEnemies:
            if self.weapon.gameObject.collided(enemy.gameObject) and (self.weapon.returning or self.weapon.flying) and (self.weapon.visible):
                enemy.takeHit(self.weapon.damage)

        return self.life

    def draw(self):
        for enemy in self.aliveEnemies:
            enemy.draw()
