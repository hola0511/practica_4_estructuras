import random
from person import Person

class Maze:
    def __init__(self, size, num_people):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
        self.people = []
        self.exits = [
            (random.randint(0, size-1), random.randint(0, size-1)),
            (random.randint(0, size-1), random.randint(0, size-1))
        ]
        self.num_people = num_people
        self.iteration = 0

    def initialize(self):
        self.people = []
        for _ in range(self.num_people):
            while True:
                pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if pos not in self.exits:
                    self.people.append(Person(pos))
                    break

    def add_obstacle(self):
        try:
            x, y = map(int, input("Coordenadas X,Y del bloqueo: ").split(","))
            if 0 <= x < self.size and 0 <= y < self.size:
                self.grid[x][y] = "X"
            else:
                print("❌ Coordenadas fuera del rango del laberinto.")
        except:
            print("⚠️ Entrada inválida. Usa el formato: fila,columna")

    def add_trap(self):
        try:
            x, y = map(int, input("Coordenadas X,Y de la trampa: ").split(","))
            if 0 <= x < self.size and 0 <= y < self.size:
                self.grid[x][y] = "T"
            else:
                print("❌ Coordenadas fuera del rango del laberinto.")
        except:
            print("⚠️ Entrada inválida. Usa el formato: fila,columna")

    def add_delay(self):
        try:
            x, y = map(int, input("Coordenadas X,Y del retrasador: ").split(","))
            if 0 <= x < self.size and 0 <= y < self.size:
                self.grid[x][y] = "R"
            else:
                print("❌ Coordenadas fuera del rango del laberinto.")
        except:
            print("⚠️ Entrada inválida. Usa el formato: fila,columna")

    def next_iteration(self):
        self.iteration += 1
        activos = 0
        for person in self.people:
            pos_anterior = person.pos
            person.take_turn(self.grid, self.exits, self.iteration)
            if person.pos != pos_anterior:
                activos += 1
        if activos == 0:
            print("🎮 Juego terminado: nadie más puede moverse.")
            self.iteration = 0
            return

        num_elementos = random.randint(1, 3)
        for _ in range(num_elementos):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) in self.exits or any(p.pos == (x, y) for p in self.people):
                continue
            tipo = random.choice(["X", "T", "R"])
            self.grid[x][y] = tipo