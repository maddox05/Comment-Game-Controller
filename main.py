import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from colorama import Fore, Style
from datetime import datetime, timedelta

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
            return "english"
    for key in key_mapping_portuguese.keys():
        if comment in key:
            return "english"
    else:
        return "english"  # Use english <3 as the default if no language is detected


# Function to get the current date and time in the desired format
def get_current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("[%d/%m/%Y %H:%M]")
    return formatted_datetime


# Function to get the date in the desired format
def get_date_string(date):
    return date.strftime("%d/%m/%Y")


# Function to save the key mapping usage record to log2.txt
def save_key_mapping_usage(key_mapping_usage):
    global first_record_date  # Access the global variable

    # If it's the first time saving the record, store the current date
    if first_record_date is None:
        first_record_date = datetime.now()

    current_date = datetime.now()

    # Calculate the difference in days between the current date and the first record date
    days_difference = (current_date - first_record_date).days

    with open("log2.txt", "w") as log2_file:
        log2_file.write(
            f"Key Mapping Usage Record from {get_date_string(first_record_date)} - {get_date_string(current_date)}\n")
        for keyword, count in key_mapping_usage.items():
            log2_file.write(f"{keyword}: {count} times\n")


# Function to handle TikTok comments
async def on_ttcomment(event: CommentEvent):
    try:
        comment = event.comment
        detected_language = detect_language(comment)

        if detected_language == "english":
            selected_key_mapping = key_mapping_english
        elif detected_language == "spanish":
            selected_key_mapping = key_mapping_spanish
        elif detected_language == "portuguese":
            selected_key_mapping = key_mapping_portuguese
        else:  # not possible to get to this else statement
            selected_key_mapping = key_mapping_english  # Use English as the default

        keypress = comment.lower()  # Convert to lowercase
        formatted_username = Fore.GREEN + event.user.nickname + Style.RESET_ALL  # colorama is cool.
        formatted_comment = Fore.WHITE + comment + Style.RESET_ALL

        # Initialize a dictionary for key mapping usage record
        key_mapping_usage = {keyword: 0 for keyword in selected_key_mapping}

        # Find keywords in the comment and format them in red
        for keyword, key_action in selected_key_mapping.items():
            if keyword in keypress:
                formatted_comment = formatted_comment.replace(keyword, Fore.RED + keyword + Style.RESET_ALL)
                key_mapping_usage[keyword] += 1

        if keypress in selected_key_mapping:
            mapped_key = selected_key_mapping[keypress]
            keyboard.press(mapped_key) # press the key
            time.sleep(0.3)
            keyboard.release(mapped_key) # release the key
            formatted_datetime = get_current_datetime()
            log_file.write(f"{formatted_datetime} {formatted_username} -> {formatted_comment}\n")

        # Save the key mapping usage record to log2.txt
        save_key_mapping_usage(key_mapping_usage)

        print(f"{formatted_datetime} {formatted_username} -> {formatted_comment}")
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
    print("Connected")
    tiktok_client.run()
