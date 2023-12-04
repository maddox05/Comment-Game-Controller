import time
import pyautogui
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from languages import *
import datetime
from gui import guiStart


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
        else:
            selected_key_mapping = key_mapping_english

        if comment in selected_key_mapping:
            pyautogui.press(selected_key_mapping[comment])
            print("pressed: " + selected_key_mapping[comment])

    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()


if __name__ == "__main__":

    log_file = open("log.txt", 'a', encoding="utf-8")
    current_time = datetime.datetime.now()
    current_time.strftime("%Y-%m-%d %H:%M:%S")
    log_file.write("Opened. Session started at " + current_time.__str__())
    username = guiStart()
    print(username)
    tiktok_client = TikTokLiveClient(unique_id=username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)  # smth for the on_ttcomment above;

    try:
        tiktok_client.run()  # Start the client

    except Exception as e:

        print(f"{e}\n"
              "1. User Not Found or User is not live\n"
              "2. Make sure to use the correct username (the one with the @)\n"
              "3. Make sure to add @ symbol")
        print(e.with_traceback())

