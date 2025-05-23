import random
from person import Person

class Maze:
    def __init__(self, size, num_people):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
        self.people = []
        self.exit = (random.randint(0, size-1), random.randint(0, size-1))
        self.num_people = num_people
        self.iteration = 0

    def initialize(self):
        self.people = []
        for _ in range(self.num_people):
            while True:
                pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if pos != self.exit:
                    self.people.append(Person(pos))
                    break

    def add_obstacle(self):
        x, y = map(int, input("Coordenadas X,Y del bloqueo: ").split(","))
        self.grid[x][y] = "X"

    def add_trap(self):
        x, y = map(int, input("Coordenadas X,Y de la trampa: ").split(","))
        self.grid[x][y] = "T"

    def add_delay(self):
        x, y = map(int, input("Coordenadas X,Y del retrasador: ").split(","))
        self.grid[x][y] = "R"

    def next_iteration(self):
        self.iteration += 1
        activos = 0
        for person in self.people:
            pos_anterior = person.pos
            person.take_turn(self.grid, self.exit, self.iteration)
            if person.pos != pos_anterior:
                activos += 1
        if activos == 0:
            print("🎮 Juego terminado: nadie más puede moverse.")
            self.iteration = 0
            return

        # Agregar entre 1 y 3 elementos aleatorios
        num_elementos = random.randint(1, 3)
        for _ in range(num_elementos):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) == self.exit or any(p.pos == (x, y) for p in self.people):
                continue
            tipo = random.choice(["X", "T", "R"])
            self.grid[x][y] = tipo
