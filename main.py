import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

key_mappings = {
    "arriba": "z",
    "up": "z",
    "abajo": "x",
    "down": "x",
    "izquierda": "c",
    "left": "c",
    "derecha": "v",
    "right": "v",
    "botona": "b",
    "buttona": "b",
    "botonb": "n",
    "buttonb": "n",
    "start": "m",
    "select": "l"
}

# Función para ejecutar un evento de tecla
def execute_key_event(key_event):
    keyboard.press(key_event)
    time.sleep(0.3)
    keyboard.release(key_event)

# @tiktok_client.on("comment")
async def on_ttcomment(event: CommentEvent):
    try:
        keypress = event.comment.lower()
        if keypress in key_mappings:
            keypress = key_mappings[keypress]
            execute_key_event(keypress)
            log_file.write(f"{event.user.nickname} -> {event.comment}\n")
        print(f"{event.user.nickname} -> {event.comment}")
    except Exception as err:
        print(f"{err}\n Cerrando")
        time.sleep(4)
        quit()

def press_start_periodically():
    while True:
        execute_key_event(key_mappings["start"])
        time.sleep(300)  # Presionar "start" cada 5 minutos

if __name__ == "__main__":
    log_file = open("log.txt", 'a', encoding="utf-8")
    log_file.write("Abierto\n")
    tiktok_username = input("TikTok username: ")
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("Conectado a TikTok exitosamente!")
    tiktok_client.run()

    # Iniciar un hilo para presionar "start" periódicamente
    thread_start_press = threading.Thread(target=press_start_periodically)
    thread_start_press.start()

    # Loop para verificar si la conexión está activa
    while tiktok_client.is_connected():
        time.sleep(60)  # Verificar cada 60 segundos
    print("Desconectado de TikTok!")
