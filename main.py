import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
import pytchat
import threading

tiktok_username = input("Type your username: ")
tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)

yt_url = input("Type your video url (end id): ")
yt_chat = pytchat.create(video_id=yt_url)

key_events = {"up", "down", "left", "right", "a", "b"}


@tiktok_client.on("comment")
async def on_ttcomment(event: CommentEvent):
    try:
        keypress = event.comment.lower()
        if keypress in key_events:
            keyboard.press(keypress)
            time.sleep(.3)  # await asyncio.sleep(.3)
            keyboard.release(keypress)
            print(f"{event.user.nickname} -> {event.comment}")
    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()


def on_ytcomment():
    while yt_chat.is_alive():
        for i in yt_chat.get().sync_items():
            try:
                keypress = i.message.lower()
                if keypress in key_events:
                    keyboard.press(keypress)
                    time.sleep(.3)  # await asyncio.sleep(.3)
                    keyboard.release(keypress)
                    print(f"{i.author.name} -> {i.message}")
            except Exception as err:
                print(f"{err}\n Quitting now")
                time.sleep(4)
                quit()


if __name__ == "__main__":
    thread1 = threading.Thread(target=on_ytcomment())
    thread1.start()
    tiktok_client.run()

# add ability to merge tiktok and youtube comments into one.
