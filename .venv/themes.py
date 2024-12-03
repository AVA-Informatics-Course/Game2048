def get_themes():
    themes = {
        "Default": {
            0: "lightgray",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
        },
        "Dark": {
            0: "#3c3c3c",
            2: "#4e4e4e",
            4: "#5e5e5e",
            8: "#7f7f7f",
            16: "#9f9f9f",
            32: "#afafaf",
            64: "#bfbfbf",
            128: "#dfdfdf",
            256: "#efefef",
            512: "#ffffff",
            1024: "#cccccc",
            2048: "#999999",
        },
    }
    return themes

def get_number_schemes():
    number_schemes = {
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
    }
    return number_schemes