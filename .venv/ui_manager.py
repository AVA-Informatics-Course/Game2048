import tkinter as tk
from game_logic import Game2048
from themes import get_themes, get_number_schemes
from user_manager import UserManager

class Game2048UI:
    """
    Handles the UI for the 2048 game, including themes, user interactions, and grid updates.
    """

    def __init__(self, root):

        """
        Initializes the main window, game settings, and displays the start screen.
        """

        self.root = root
        self.root.title("2048 Game")

        self.user_manager = UserManager()  # Initialize UserManager
        self.game = None

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
        self.win_score = 2048

    def set_dynamic_window_size(self):
        """Sets the window size dynamically based on the screen resolution."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.4)
        height = int(screen_height * 0.8)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.center_window(width, height)

    def center_window(self, width, height):
        """Centers the window on the screen."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def start_screen(self):
        """Displays the start screen with theme and user options."""

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
            command=self.save_user_and_start_game,
            relief="raised",
            borderwidth=3
        )
        start_button.pack(pady=(20, 0))

    def clear_screen(self):
        """
        Clears all widgets from the main window.
        """

        for widget in self.root.winfo_children():
            widget.destroy()

    def start_game(self):
        """
        Initializes a new game, sets up the UI with a fresh grid, player information,
        and control buttons, then starts the game with key bindings.
        """

        self.game = Game2048()
        self.clear_screen()
        self.build_grid()

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

        # Add control buttons
        self.add_control_buttons()

        # Save the updated user score
        self.save_user_score()

        # Start game with updated UI
        self.update_ui()
        self.root.bind("<Key>", self.handle_keypress)

    def add_control_buttons(self):
        """
        Adds control buttons for navigating to the main menu and starting a new game.
        """
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

    def build_grid(self):
        """
        Builds the game grid as a grid of tiles and initializes the tiles list.
        """

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
        """
        Updates the UI by refreshing the grid tiles and score display, and saves the current score.
        """
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                value = self.game.grid[r][c]
                self.tiles[r][c].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))
        self.score_label.config(text=f"Score: {self.game.score}")
        self.save_user_score()

        if self.game.get_max_tile() == self.win_score:
            self.show_win_message()

    def get_tile_color(self, value):
        """
        Returns the tile color based on the value, current theme, and number scheme.
        """

        # Get the base color from the current theme
        base_color = self.themes.get(self.current_theme, "lightgray")

        # Get the number color from the current number scheme if it's not defined
        if self.current_number_scheme is not None:
            number_color = self.number_schemes[self.current_number_scheme].get(value, "#ffffff")

            if value > 0:
                return number_color

        return base_color

    def handle_keypress(self, event):
        """
        Handles keypress events to control the game, checks for game-over conditions,
        and updates the UI after each move.
        """
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
        """
        Updates the current theme based on the selected option.
        """
        self.current_theme = self.theme_var.get()

    def set_number_scheme(self):
        """
        Updates the current number scheme based on the selected option.
        """
        self.current_number_scheme = self.number_var.get()

    def show_game_over(self):
        """
        Displays a 'Game Over' message and disables key bindings.
        """
        game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 24), bg="red", fg="white")
        game_over_label.pack(pady=50, side="bottom")
        self.root.unbind("<Key>")

    def show_win_message(self):

        """
        Displays a 'Congratulations!' message and disables key bindings.
        """
        game_over_label = tk.Label(self.root, text="Congratulations!", font=("Arial", 24), bg="green", fg="white")
        game_over_label.pack(pady=50, side="bottom")
        self.root.unbind("<Key>")

    def save_user_and_start_game(self):
        """
        Saves the user's first and last name (or defaults if blank) and starts the game.
        """

        self.user_first_name = self.user_first_name_entry.get()
        self.user_last_name = self.user_last_name_entry.get()

        if not self.user_first_name:
            self.user_first_name = "Unknown"
        if not self.user_last_name:
            self.user_last_name = "Player"

        self.fetch_user_data()
        self.start_game()

    def save_user_and_start_game(self):
        """
        Saves the user's first and last name (or defaults if blank) and starts the game.
        """
        self.user_first_name = self.user_first_name_entry.get()
        self.user_last_name = self.user_last_name_entry.get()

        if not self.user_first_name:
            self.user_first_name = "Unknown"
        if not self.user_last_name:
            self.user_last_name = "Player"

        self.user_manager.fetch_user_data(self.user_first_name, self.user_last_name)  # Call UserManager
        self.start_game()

    def save_user_score(self):
        """
        Saves the current user's score using UserManager.
        """
        self.user_manager.save_user_score(self.user_first_name, self.user_last_name, self.game.score)
