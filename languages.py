# Define the key mapping in English
key_mapping_english = {
    "up": "z",
    "down": "x",
    "left": "c",
    "right": "v",
    "buttona": "a",
    "buttonb": "b",
    "start": "m",
    "select": "l"
}

# Define the key mapping in Spanish
key_mapping_spanish = {
    "arriba": "z",
    "abajo": "x",
    "izquierda": "c",
    "derecha": "v",
    "botona": "a",
    "botonb": "b",
    "start": "m",
    "select": "l"
}

# Define the key mapping in Portuguese
key_mapping_portuguese = {
    "cima": "z",
    "baixo": "x",
    "esquerda": "c",
    "direita": "v",
    "botaoa": "a",
    "botaob": "b",
    "iniciar": "m",
    "selecionar": "l"
}


# Function to detect the language based on the comment
def detect_language(comment):
    # Lists of keywords for each language
    comment = comment.lower()
    for key in key_mapping_english.keys():
        if comment in key:
            return "english"
    for key in key_mapping_spanish.keys():
        if comment in key:
            return "spanish"
    for key in key_mapping_portuguese.keys():
        if comment in key:
            return "portuguese"
    else:
        return "error"  # Use english <3 as the default if no language is detected
