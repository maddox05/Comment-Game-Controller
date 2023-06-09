from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
import keyboard
import time
import asyncio

client = TikTokLiveClient(unique_id="@pablo040120")

key_events = {"up", "down", "left", "right"}


@client.on("comment")
async def on_comment(event: CommentEvent):
    try:
        keypress = event.comment.lower()
        if keypress in key_events:
            keyboard.press(keypress)
            print(f"{event.user.nickname} -> {event.comment}")
    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()


if __name__ == "__main__":
    client.run()
