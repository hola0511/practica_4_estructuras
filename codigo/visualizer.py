from colorama import Fore, Style

def display_maze(maze):
    print(f"\nIteración: {maze.iteration}")
    for i in range(maze.size):
        row = ""
        for j in range(maze.size):
            pos = (i, j)
            if pos == maze.exit:
                row += f"{Fore.GREEN}🏁{Style.RESET_ALL}"
            elif any(p.pos == pos for p in maze.people):
                row += f"{Fore.BLUE}🧍{Style.RESET_ALL}"
            else:
                cell = maze.grid[i][j]
                if cell == "X":
                    row += f"{Fore.BLACK}X{Style.RESET_ALL}"
                elif cell == "T":
                    row += f"{Fore.MAGENTA}T{Style.RESET_ALL}"
                elif cell == "R":
                    row += f"{Fore.YELLOW}R{Style.RESET_ALL}"
                else:
                    row += "."
        print(row)