from maze import Maze
from visualizer import display_maze
from person import print_decision_tree

def menu():
    try:
        size_input = input("🔧 Tamaño del laberinto (Enter para usar 10x10): ")
        size = int(size_input) if size_input.strip() else 10
    except ValueError:
        size = 10

    maze = Maze(size=size, num_people=3)

    while True:
        print("🌳 The Maze of Terror 🌀")
        print("1. Iniciar simulación")
        print("2. Colocar bloqueos")
        print("3. Colocar trampas")
        print("4. Colocar retrasadores")
        print("5. Visualizar estado actual")
        print("6. Ejecutar siguiente iteración")
        print("7. Ver árbol de decisiones de cada persona")
        print("8. Salir")
        opc = input("Elige una opción: ")

        if opc == "1":
            maze.initialize()
            display_maze(maze)

        elif opc == "2":
            maze.add_obstacle()

        elif opc == "3":
            maze.add_trap()

        elif opc == "4":
            maze.add_delay()

        elif opc == "5":
            display_maze(maze)

        elif opc == "6":
            maze.next_iteration()
            display_maze(maze)

        elif opc == "7":
            for i, person in enumerate(maze.people):
                print(f"\n📜 Árbol de decisiones de Persona {i+1}:")
                print_decision_tree(person.history)
                print("\n" + "-"*40)

        elif opc == "8":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
