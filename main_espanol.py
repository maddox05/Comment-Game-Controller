# -*- coding: utf-8 -*-
import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from colorama import Fore, Style
from datetime import datetime, timedelta

# Define el mapeo de teclas en inglés
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

# Define el mapeo de teclas en español
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

# Define el mapeo de teclas en portugués
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

# Variable para almacenar la fecha en la que se guardó el primer registro
first_record_date = None

# Función para detectar el idioma en base al comentario
def detect_language(comment):
    # Lista de palabras clave para cada idioma
    english_keywords = set(key_mapping_english.keys())
    spanish_keywords = set(key_mapping_spanish.keys())
    portuguese_keywords = set(key_mapping_portuguese.keys())
    
    # Convertir el comentario a minúsculas para hacer coincidencias sin distinción de mayúsculas y minúsculas
    comment = comment.lower()
    
    # Comprobar qué palabras clave del idioma se encuentran en el comentario
    spanish_matches = spanish_keywords.intersection(comment.split())
    english_matches = english_keywords.intersection(comment.split())
    portuguese_matches = portuguese_keywords.intersection(comment.split())
    
    # Determinar el idioma en función de las coincidencias
    if spanish_matches:
        return "spanish"
    elif english_matches:
        return "english"
    elif portuguese_matches:
        return "portuguese"
    else:
        return "spanish"  # Usar español por defecto si no se detecta ningún idioma

# Función para obtener la fecha y hora actual en el formato deseado
def get_current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("[%d/%m/%Y %H:%M]")
    return formatted_datetime

# Función para obtener la fecha en el formato deseado
def get_date_string(date):
    return date.strftime("%d/%m/%Y")

# Función para guardar el registro de movimientos en log2.txt
def save_key_mapping_usage(key_mapping_usage):
    global first_record_date  # Accede a la variable global
    
    # Si es la primera vez que se guarda el registro, guarda la fecha actual
    if first_record_date is None:
        first_record_date = datetime.now()
    
    current_date = datetime.now()
    
    # Calcula la diferencia de días entre la fecha actual y la primera fecha de registro
    days_difference = (current_date - first_record_date).days
    
    with open("log2.txt", "w") as log2_file:
        log2_file.write(f"Registro de movimientos ejecutados desde {get_date_string(first_record_date)} - {get_date_string(current_date)}\n")
        for keyword, count in key_mapping_usage.items():
            log2_file.write(f"{keyword}: {count} veces\n")

# Función para manejar comentarios de TikTok
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
            selected_key_mapping = key_mapping_spanish  # Usar español por defecto
        
        keypress = comment.lower()  # Convertir a minúsculas
        formatted_username = Fore.GREEN + event.user.nickname + Style.RESET_ALL
        formatted_comment = Fore.WHITE + comment + Style.RESET_ALL
        
        # Inicializar un diccionario para el registro de las sentencias del key_mapping
        key_mapping_usage = {keyword: 0 for keyword in selected_key_mapping}
        
        # Buscar palabras clave en el comentario y formatearlas en rojo
        for keyword, key_action in selected_key_mapping.items():
            if keyword in keypress:
                formatted_comment = formatted_comment.replace(keyword, Fore.RED + keyword + Style.RESET_ALL)
                key_mapping_usage[keyword] += 1
        
        if keypress in selected_key_mapping:
            mapped_key = selected_key_mapping[keypress]
            keyboard.press(mapped_key)
            time.sleep(0.3)
            keyboard.release(mapped_key)
            formatted_datetime = get_current_datetime()
            log_file.write(f"{formatted_datetime} {formatted_username} -> {formatted_comment}\n")
        
        # Guardar el registro de las sentencias del key_mapping en log2.txt
        save_key_mapping_usage(key_mapping_usage)
        
        print(f"{formatted_datetime} {formatted_username} -> {formatted_comment}")
    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()

if __name__ == "__main__":
    log_file = open("log.txt", 'a', encoding="utf-8")
    log_file.write("Opened\n")
    
    tiktok_username = input("TikTok username: ")  # Modificado el mensaje de solicitud
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("Connected")
    tiktok_client.run()
