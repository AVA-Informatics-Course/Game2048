"""
Provides pre-defined themes and number schemes for the 2048 game.

- `get_themes()`: Returns color themes for tile backgrounds based on their values.
- `get_number_schemes()`: Returns color schemes for tile numbers based on their values.
"""

def get_themes():
    themes = {
        "Default": "#D3D3D3",
        "Slightly Dark": "#a9a9a9",
        "Dark": "#545454"
        }

    return themes

def get_number_schemes():
    number_schemes = {
        "Orange": {
            2: "#ffe5d9",
            4: "#ffc1a1",
            8: "#ff9f6d",
            16: "#ff7d41",
            32: "#ff5b17",
            64: "#e64a00",
            128: "#cc3e00",
            256: "#b33200",
            512: "#992700",
            1024: "#801e00",
            2048: "#661400",
        },
        "Blue": {
            2: "#d0e1f9",
            4: "#4d90fe",
            8: "#1d3fbb",
            16: "#003f88",
            32: "#002e66",
            64: "#001f44",
            128: "#001333",
            256: "#000b22",
            512: "#000611",
            1024: "#000306",
            2048: "#000103",
        },
        "Green": {
            2: "#e6f9e7",
            4: "#c3f0c8",
            8: "#91d99b",
            16: "#5db965",
            32: "#46a44f",
            64: "#2d7d38",
            128: "#206128",
            256: "#144618",
            512: "#0c2c0d",
            1024: "#061906",
            2048: "#020f03",
        },
        "Purple": {
            2: "#f5e6f9",
            4: "#e3c4f0",
            8: "#d19fe6",
            16: "#b573d9",
            32: "#9e4ccf",
            64: "#7b39a6",
            128: "#612d82",
            256: "#47205f",
            512: "#30163f",
            1024: "#1d0d26",
            2048: "#0f0613"
        },
        "Red": {
            2: "#fde6e6",
            4: "#fbbaba",
            8: "#f88989",
            16: "#f25959",
            32: "#e33030",
            64: "#c21919",
            128: "#961313",
            256: "#6b0d0d",
            512: "#4a0808",
            1024: "#2e0505",
            2048: "#170202"
        }

    }
    return number_schemes