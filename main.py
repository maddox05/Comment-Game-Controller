import time
import pyautogui
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from languages import *


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
