import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
import pytchat
import threading

key_events = {"up", "down", "left", "right", "a", "b", "x", "y"}


# @tiktok_client.on("comment")
async def on_ttcomment(event: CommentEvent):
    try:
        keypress = event.comment.lower()
        if keypress in key_events:
            keyboard.press(keypress)
            time.sleep(.3)  # await asyncio.sleep(.3)
            keyboard.release(keypress)
            log_file.write(f"{event.author.name} -> {event.message}\n")
        print(f"{event.user.nickname} -> {event.comment}")
    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()


def on_ytcomment():
    while yt_chat.is_alive():
        for event in yt_chat.get().sync_items():
            try:
                keypress = event.message.lower()
                if keypress in key_events:
                    keyboard.press(keypress)
                    time.sleep(.3)  # await asyncio.sleep(.3)
                    keyboard.release(keypress)
                    log_file.write(f"{event.author.name} -> {event.message}\n")
                print(f"{event.author.name} -> {event.message}")
            except Exception as err:
                print(f"{err}\n Quitting now")
                time.sleep(4)
                quit()


if __name__ == "__main__":
    log_file = open("log.txt", 'a')
    log_file.write("Opened\n")
    choice_tt = input("Would you like to stream to tiktok? Y/N: ")
    choice_yt = input("Would you like to stream to youtube? Y/N: ")
    if choice_tt.lower() == "y":
        tiktok_username = input("Paste your TIKTOK username: ")
        tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
        on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
        tiktok_client.run()
    if choice_yt.lower() == "y":
        yt_url_full = input("Type your video url: ")
        head, sep, yt_id = yt_url_full.partition('=')
        yt_chat = pytchat.create(video_id=yt_id)
        thread1 = threading.Thread(target=on_ytcomment())
        thread1.start()

    # have log.txt files
