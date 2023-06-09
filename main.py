from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
import keyboard
import time
import asyncio

client = TikTokLiveClient(unique_id="@rqinizkx21551")


@client.on("comment")
async def on_comment(event: CommentEvent):
    try:
        keypress = event.comment.lower()
        if keypress == "up" or keypress == "down" or keypress == "left" or keypress == "right":
            keyboard.press(keypress)
            print(f"{event.user.nickname} -> {event.comment}")
    except Exception as err:
        print(f"{err} Quitting now")
        time.sleep(4)
        quit()


if __name__ == "__main__":
    client.run()
