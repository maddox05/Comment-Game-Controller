# -*- coding: utf-8 -*-
import time
import keyboard
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent
from colorama import Fore, Style
from datetime import datetime, timedelta

# Define o mapeamento de teclas em inglês
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

# Define o mapeamento de teclas em espanhol
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

# Define o mapeamento de teclas em português
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

# Variável para armazenar a data em que o primeiro registro foi salvo
first_record_date = None

# Função para detectar o idioma com base no comentário
def detect_language(comment):
    # Listas de palavras-chave para cada idioma
    english_keywords = set(key_mapping_english.keys())
    spanish_keywords = set(key_mapping_spanish.keys())
    portuguese_keywords = set(key_mapping_portuguese.keys())
    
    # Converter o comentário para letras minúsculas para corresponder sem distinção entre maiúsculas e minúsculas
    comment = comment.lower()
    
    # Verificar quais palavras-chave do idioma estão no comentário
    spanish_matches = spanish_keywords.intersection(comment.split())
    english_matches = english_keywords.intersection(comment.split())
    portuguese_matches = portuguese_keywords.intersection(comment.split())
    
    # Determinar o idioma com base nas correspondências
    if spanish_matches:
        return "spanish"
    elif english_matches:
        return "english"
    elif portuguese_matches:
        return "portuguese"
    else:
        return "spanish"  # Use o espanhol como padrão se nenhum idioma for detectado

# Função para obter a data e hora atual no formato desejado
def get_current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("[%d/%m/%Y %H:%M]")
    return formatted_datetime

# Função para obter a data no formato desejado
def get_date_string(date):
    return date.strftime("%d/%m/%Y")

# Função para salvar o registro de uso do mapeamento de teclas em log2.txt
def save_key_mapping_usage(key_mapping_usage):
    global first_record_date  # Acessa a variável global
    
    # Se for a primeira vez que o registro está sendo salvo, armazene a data atual
    if first_record_date is None:
        first_record_date = datetime.now()
    
    current_date = datetime.now()
    
    # Calcule a diferença de dias entre a data atual e a data do primeiro registro
    days_difference = (current_date - first_record_date).days
    
    with open("log2.txt", "w") as log2_file:
        log2_file.write(f"Registro de uso do mapeamento de teclas de {get_date_string(first_record_date)} a {get_date_string(current_date)}\n")
        for keyword, count in key_mapping_usage.items():
            log2_file.write(f"{keyword}: {count} vezes\n")

# Função para lidar com comentários do TikTok
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
            selected_key_mapping = key_mapping_spanish  # Use o espanhol como padrão
        
        keypress = comment.lower()  # Converter para letras minúsculas
        formatted_username = Fore.GREEN + event.user.nickname + Style.RESET_ALL
        formatted_comment = Fore.WHITE + comment + Style.RESET_ALL
        
        # Inicializar um dicionário para o registro de uso do mapeamento de teclas
        key_mapping_usage = {keyword: 0 for keyword in selected_key_mapping}
        
        # Encontrar palavras-chave no comentário e formatá-las em vermelho
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
        
        # Salvar o registro de uso do mapeamento de teclas em log2.txt
        save_key_mapping_usage(key_mapping_usage)
        
        print(f"{formatted_datetime} {formatted_username} -> {formatted_comment}")
    except Exception as err:
        print(f"{err}\n Quitting now")
        time.sleep(4)
        quit()

if __name__ == "__main__":
    log_file = open("log.txt", 'a', encoding="utf-8")
    log_file.write("Opened\n")
    
    tiktok_username = input("TikTok username: ")  # Mensagem modificada
    tiktok_client = TikTokLiveClient(unique_id="@" + tiktok_username)
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("Connected")
    tiktok_client.run()
