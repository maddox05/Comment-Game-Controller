import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

tiktok_username = input("Type your username: ")
tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)

key_events = {"up", "down", "left", "right", "a", "b"}


@tiktok_client.on("comment")
async def on_comment(event: CommentEvent):
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


if __name__ == "__main__":
    tiktok_client.run()

# add ability to merge tiktok and youtube comments into one.
