import tkinter as tk
from game_logic import Game2048
from themes import get_themes, get_number_schemes
import json

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
        self.current_number_scheme = "Orange"
        self.user_first_name = ""
        self.user_last_name = ""
        self.start_screen()

    def set_dynamic_window_size(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.3)
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

        # Create a frame for the entire start screen
        start_frame = tk.Frame(self.root, bg="#f7f7f7", padx=20, pady=20)
        start_frame.pack(expand=True, fill="both")

        # Title Label
        title_label = tk.Label(
            start_frame,
            text="Welcome to 2048!",
            font=("Arial", 36, "bold"),
            fg="#333",
            bg="#f7f7f7"
        )
        title_label.pack(pady=(0, 20))

        # Theme Selection
        theme_frame = tk.Frame(start_frame, bg="#f7f7f7")
        theme_frame.pack(pady=(10, 10))

        theme_label = tk.Label(
            theme_frame, text="Select Theme:", font=("Arial", 18), fg="#555", bg="#f7f7f7"
        )
        theme_label.pack(anchor="w", pady=(0, 5))

        self.theme_var = tk.StringVar(value=self.current_theme)
        for theme in self.themes.keys():
            theme_radio = tk.Radiobutton(
                theme_frame,
                text=theme,
                variable=self.theme_var,
                value=theme,
                font=("Arial", 14),
                bg="#f7f7f7",
                fg="#333",
                selectcolor="#dcdcdc",
                command=self.set_theme
            )
            theme_radio.pack(side="left", padx=10)

        # Number Scheme Selection
        number_frame = tk.Frame(start_frame, bg="#f7f7f7")
        number_frame.pack(pady=(10, 10))

        number_label = tk.Label(
            number_frame, text="Select Number Scheme:", font=("Arial", 18), fg="#555", bg="#f7f7f7"
        )
        number_label.pack(anchor="w", pady=(0, 5))

        self.number_var = tk.StringVar(value=self.current_number_scheme)
        for scheme in self.number_schemes.keys():
            number_radio = tk.Radiobutton(
                number_frame,
                text=scheme,
                variable=self.number_var,
                value=scheme,
                font=("Arial", 14),
                bg="#f7f7f7",
                fg="#333",
                selectcolor="#dcdcdc",
                command=self.set_number_scheme
            )
            number_radio.pack(side="left", padx=10)

        # User Input Fields
        user_frame = tk.Frame(start_frame, bg="#f7f7f7")
        user_frame.pack(pady=(10, 10))

        user_first_name_label = tk.Label(
            user_frame, text="First Name:", font=("Arial", 14), fg="#555", bg="#f7f7f7"
        )
        self.user_first_name_entry = tk.Entry(user_frame, font=("Arial", 14), width=20)

        user_last_name_label = tk.Label(
            user_frame, text="Last Name:", font=("Arial", 14), fg="#555", bg="#f7f7f7"
        )
        self.user_last_name_entry = tk.Entry(user_frame, font=("Arial", 14), width=20)

        self.user_first_name_entry.insert(0, self.user_first_name)
        self.user_last_name_entry.insert(0, self.user_last_name)

        user_first_name_label.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.user_first_name_entry.grid(row=0, column=1, pady=5, padx=5)
        user_last_name_label.grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.user_last_name_entry.grid(row=1, column=1, pady=5, padx=5)

        # Start Button
        start_button = tk.Button(
            start_frame,
            text="Start Game",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4caf50",
            activebackground="#45a049",
            activeforeground="white",
            command=self.save_user_and_start_game,  # Updated command here
            relief="raised",
            borderwidth=3
        )
        start_button.pack(pady=(20, 0))

    # def start_screen(self):
    #     self.clear_screen()
    #
    #     # Create a frame for the entire start screen
    #     start_frame = tk.Frame(self.root, bg="#f7f7f7", padx=20, pady=20)
    #     start_frame.pack(expand=True, fill="both")
    #
    #     # Title Label
    #     title_label = tk.Label(
    #         start_frame,
    #         text="Welcome to 2048!",
    #         font=("Arial", 36, "bold"),
    #         fg="#333",
    #         bg="#f7f7f7"
    #     )
    #     title_label.pack(pady=(0, 20))
    #
    #     # Theme Selection
    #     theme_frame = tk.Frame(start_frame, bg="#f7f7f7")
    #     theme_frame.pack(pady=(10, 10))
    #
    #     theme_label = tk.Label(
    #         theme_frame, text="Select Theme:", font=("Arial", 18), fg="#555", bg="#f7f7f7"
    #     )
    #     theme_label.pack(anchor="w", pady=(0, 5))
    #
    #     self.theme_var = tk.StringVar(value=self.current_theme)
    #     for theme in self.themes.keys():
    #         theme_radio = tk.Radiobutton(
    #             theme_frame,
    #             text=theme,
    #             variable=self.theme_var,
    #             value=theme,
    #             font=("Arial", 14),
    #             bg="#f7f7f7",
    #             fg="#333",
    #             selectcolor="#dcdcdc",
    #             command=self.set_theme
    #         )
    #         theme_radio.pack(side="left", padx=10)
    #
    #     # Number Scheme Selection
    #     number_frame = tk.Frame(start_frame, bg="#f7f7f7")
    #     number_frame.pack(pady=(10, 10))
    #
    #     number_label = tk.Label(
    #         number_frame, text="Select Number Scheme:", font=("Arial", 18), fg="#555", bg="#f7f7f7"
    #     )
    #     number_label.pack(anchor="w", pady=(0, 5))
    #
    #     self.number_var = tk.StringVar(value=self.current_number_scheme)
    #     for scheme in self.number_schemes.keys():
    #         number_radio = tk.Radiobutton(
    #             number_frame,
    #             text=scheme,
    #             variable=self.number_var,
    #             value=scheme,
    #             font=("Arial", 14),
    #             bg="#f7f7f7",
    #             fg="#333",
    #             selectcolor="#dcdcdc",
    #             command=self.set_number_scheme
    #         )
    #         number_radio.pack(side="left", padx=10)
    #
    #     # User Input Fields
    #     user_frame = tk.Frame(start_frame, bg="#f7f7f7")
    #     user_frame.pack(pady=(10, 10))
    #
    #     user_first_name_label = tk.Label(
    #         user_frame, text="First Name:", font=("Arial", 14), fg="#555", bg="#f7f7f7"
    #     )
    #     self.user_first_name_entry = tk.Entry(user_frame, font=("Arial", 14), width=20)
    #
    #     user_last_name_label = tk.Label(
    #         user_frame, text="Last Name:", font=("Arial", 14), fg="#555", bg="#f7f7f7"
    #     )
    #     self.user_last_name_entry = tk.Entry(user_frame, font=("Arial", 14), width=20)
    #
    #     self.user_first_name_entry.insert(0, self.user_first_name)
    #     self.user_last_name_entry.insert(0, self.user_last_name)
    #
    #     user_first_name_label.grid(row=0, column=0, sticky="w", pady=5, padx=5)
    #     self.user_first_name_entry.grid(row=0, column=1, pady=5, padx=5)
    #     user_last_name_label.grid(row=1, column=0, sticky="w", pady=5, padx=5)
    #     self.user_last_name_entry.grid(row=1, column=1, pady=5, padx=5)
    #
    #     # Start Button
    #     start_button = tk.Button(
    #         start_frame,
    #         text="Start Game",
    #         font=("Arial", 24, "bold"),
    #         fg="white",
    #         bg="#4caf50",
    #         activebackground="#45a049",
    #         activeforeground="white",
    #         command=self.start_game,
    #         relief="raised",
    #         borderwidth=3
    #     )
    #     start_button.pack(pady=(20, 0))


    def user_input(self):
        user_first_name_label = tk.Label(self.root, text="First Name:", font=("Arial", 14))
        self.user_first_name_entry = tk.Entry(self.root, width=20)

        user_last_name_label = tk.Label(self.root, text="Last Name:", font=("Arial", 14))
        self.user_last_name_entry = tk.Entry(self.root, width=20)

        def save_user_info():
            self.user_first_name = self.user_first_name_entry.get()
            self.user_last_name = self.user_last_name_entry.get()
            if not self.user_first_name:
                self.user_first_name = "Unknown"
            if not self.user_last_name:
                self.user_last_name = "Player"

            self.fetch_user_data()
            self.start_game()

        start_button = tk.Button(
            self.root,
            text="Start Game",
            font=("Arial", 24),
            command=lambda: [save_user_info(), self.start_game()]
        )

        user_first_name_label.pack()
        self.user_first_name_entry.pack()
        user_last_name_label.pack()
        self.user_last_name_entry.pack()
        start_button.pack(pady=20)

    def save_user_and_start_game(self):
        self.user_first_name = self.user_first_name_entry.get()
        self.user_last_name = self.user_last_name_entry.get()

        if not self.user_first_name:
            self.user_first_name = "Unknown"
        if not self.user_last_name:
            self.user_last_name = "Player"

        self.fetch_user_data()  # Save the user data
        self.start_game()  # Start the game

    def fetch_user_data(self):
        file_name = 'user_info.json'
        try:
            with open(file_name, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        user_key = f"{self.user_first_name} {self.user_last_name}"

        # Add user data if not present
        if user_key not in user_data:
            user_data[user_key] = {
                "first name": self.user_first_name,
                "last name": self.user_last_name,
                "scores": 0
            }

        # Save updated data back to the file
        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)

    def start_game(self):
        self.game = Game2048()  # Initialize game first
        self.clear_screen()  # Clear all existing widgets
        self.build_grid()  # Create a fresh grid

        # Create the info frame at the top
        self.info_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        self.info_frame.pack(fill="x")

        self.name_label = tk.Label(
            self.info_frame,
            text=f"Player: {self.user_first_name} {self.user_last_name}",
            font=("Arial", 16),
            bg="lightblue"
        )
        self.name_label.pack()

        self.score_label = tk.Label(
            self.info_frame,
            text="Score: 0",
            font=("Arial", 16),
            bg="lightblue"
        )
        self.score_label.pack()

        # Add control buttons below the game
        self.add_control_buttons()

        # Now save the updated user score
        self.save_user_score()

        # Start game with updated UI
        self.update_ui()
        self.root.bind("<Key>", self.handle_keypress)

    def add_control_buttons(self):
        # Create Header Frame
        header_frame = tk.Frame(self.root, bg="#f7f7f7", pady=30)
        header_frame.pack(fill="x")

        # Create a Button Frame for Centering
        button_frame = tk.Frame(header_frame, bg="#f7f7f7")
        button_frame.pack(expand=True, anchor="center")

        # Main Menu Button
        main_menu_button = tk.Button(
            button_frame,
            text="Main Menu",
            font=("Arial", 14),
            fg="white",
            bg="#4caf50",
            activebackground="#45a049",
            command=self.start_screen,
            relief="raised",
            borderwidth=3
        )
        main_menu_button.pack(side="left", padx=10)

        # New Game Button
        new_game_button = tk.Button(
            button_frame,
            text="New Game",
            font=("Arial", 14),
            fg="white",
            bg="#4caf50",
            activebackground="#45a049",
            command=self.start_game,
            relief="raised",
            borderwidth=3
        )
        new_game_button.pack(side="left", padx=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_grid(self):
        # Clear the tiles list before rebuilding the grid
        self.tiles = []
        self.frame = tk.Frame(self.root, bg="gray", padx=5, pady=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        for r in range(self.grid_size):
            row = []
            for c in range(self.grid_size):
                tile = tk.Label(self.frame, text="", bg="lightgray", font=("Arial", 24, "bold"), width=4, height=2,
                                relief="groove", borderwidth=2)
                tile.grid(row=r, column=c, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

    def update_ui(self):
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                value = self.game.grid[r][c]
                self.tiles[r][c].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))
        self.score_label.config(text=f"Score: {self.game.score}")
        self.save_user_score()

    def get_tile_color(self, value):
        # Get the base color from the current theme
        base_color = self.themes[self.current_theme].get(value, "#cdc1b4")

        # Get the number color from the current number scheme if it's not the "Default" scheme
        if self.current_number_scheme != "Default":
            number_color = self.number_schemes[self.current_number_scheme].get(value, "#ffffff")
            # Combine the number color with the base color for visible contrast
            if value > 0:
                # Adjust brightness or contrast for the combination
                return number_color
        # Fallback to the base color
        return base_color

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
        game_over_label.pack(pady=50, side="bottom")
        self.root.unbind("<Key>")

    def save_user_score(self):
        file_name = 'user_info.json'

        try:
            with open(file_name, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        user_key = f"{self.user_first_name} {self.user_last_name}"
        if user_key not in user_data:
            user_data[user_key] = {
                "first name": self.user_first_name,
                "last name": self.user_last_name,
                "scores": 0
            }

        user_data[user_key]["scores"] = self.game.score

        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)

    def show_high_scores(self):
        high_score_window = tk.Toplevel(self.root)
        high_score_window.title("High Scores")

        try:
            with open('user_info.json', 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}

        if user_data:
            high_scores = [(key, data["scores"]) for key, data in user_data.items()]

            sorted_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)

            for index, (name, score) in enumerate(sorted_scores):
                score_label = tk.Label(high_score_window, text=f"{index + 1}. {name} - {score}", font=("Arial", 14))
                score_label.pack()
        else:
            no_scores_label = tk.Label(high_score_window, text="No scores yet.", font=("Arial", 14))
            no_scores_label.pack()

        close_button = tk.Button(high_score_window, text="Close", command=high_score_window.destroy)
        close_button.pack(pady=10)