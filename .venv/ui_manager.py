import tkinter as tk
from game_logic import Game2048
from themes import get_themes, get_number_schemes

class Game2048UI:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game")

        # Set window size dynamically based on screen size
        self.set_dynamic_window_size()

        self.game = None
        self.grid_size = 4
        self.tiles = []
        self.themes = get_themes()
        self.number_schemes = get_number_schemes()
        self.current_theme = "Default"
        self.current_number_scheme = "DefaultColors"
        self.start_screen()

    def set_dynamic_window_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.5)
        height = int(screen_height * 0.6)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.center_window(width, height)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def start_screen(self):
        self.clear_screen()
        start_button = tk.Button(self.root, text="Start Game", font=("Arial", 24), command=self.start_game)
        start_button.pack(pady=20)

        theme_label = tk.Label(self.root, text="Select Theme:", font=("Arial", 18))
        theme_label.pack()
        self.theme_var = tk.StringVar(value="Default")
        for theme in self.themes.keys():
            theme_radio = tk.Radiobutton(self.root, text=theme, variable=self.theme_var, value=theme, font=("Arial", 14), command=self.set_theme)
            theme_radio.pack(pady=5)

        number_label = tk.Label(self.root, text="Select Number Scheme:", font=("Arial", 18))
        number_label.pack()
        self.number_var = tk.StringVar(value="DefaultColors")
        for scheme in ["DefaultColors", *self.number_schemes.keys()]:
            number_radio = tk.Radiobutton(self.root, text=scheme, variable=self.number_var, value=scheme, font=("Arial", 14), command=self.set_number_scheme)
            number_radio.pack(pady=5)

    def start_game(self):
        self.game = Game2048()
        self.clear_screen()
        self.build_grid()
        self.update_ui()
        self.root.bind("<Key>", self.handle_keypress)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_grid(self):
        self.frame = tk.Frame(self.root, bg="gray", padx=5, pady=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the game frame in the environment
        for r in range(self.grid_size):
            row = []
            for c in range(self.grid_size):
                tile = tk.Label(self.frame, text="", bg="lightgray", font=("Arial", 24), width=4, height=2)
                tile.grid(row=r, column=c, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

    def update_ui(self):
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                value = self.game.grid[r][c]
                self.tiles[r][c].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        base_color = self.themes[self.current_theme].get(value, "#cdc1b4")
        if self.current_number_scheme == "DefaultColors":
            return base_color
        number_color = self.number_schemes[self.current_number_scheme].get(value, "#ffffff")
        return number_color if value > 0 else base_color

    def handle_keypress(self, event):
        if event.keysym == "Left":
            self.game.move_left()
        elif event.keysym == "Right":
            self.game.move_right()
        elif event.keysym == "Up":
            self.game.move_up()
        elif event.keysym == "Down":
            self.game.move_down()

        if not self.game.can_move():
            self.show_game_over()
        else:
            self.game.generate_tile()
            self.update_ui()

    def set_theme(self):
        self.current_theme = self.theme_var.get()

    def set_number_scheme(self):
        self.current_number_scheme = self.number_var.get()

    def show_game_over(self):
        game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 24), bg="red", fg="white")
        game_over_label.pack()
        self.root.unbind("<Key>")
