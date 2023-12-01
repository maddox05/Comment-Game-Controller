import time
import pyautogui
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

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

# Variable to store the date when the first record was saved
first_record_date = None


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
        return "english"  # Use english <3 as the default if no language is detected


# Function to handle TikTok comments
async def on_ttcomment(event: CommentEvent):
    try:
        comment = event.comment
        detected_language = detect_language(comment)

        if detected_language == "english":
            selected_key_mapping = key_mapping_english
        elif detected_language == "spanish":
            selected_key_mapping = key_mapping_spanish
        else:
            selected_key_mapping = key_mapping_portuguese

        if comment in selected_key_mapping:
            pyautogui.press(selected_key_mapping[comment])
            print("pressed: " + selected_key_mapping[comment])

    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()


if __name__ == "__main__":
    log_file = open("log.txt", 'a', encoding="utf-8")
    log_file.write("Opened\n")

    tiktok_username = input("TikTok username: ")  # Modified the prompt message
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    tiktok_client.run()  # Start the client
