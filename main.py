# -*- coding: utf-8 -*-
import requests
import json
import telebot
import threading
import time

# Token do bot
api = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot

# Inicializa o bot
bot = telebot.TeleBot(api)

# Vari�veis de controle
analise_sinal = False
entrada = 0
max_gale = 2  # Quantidade de gale que o bot vai mandar

resultado = []
check_resultado = []

win_count = 0
loss_count = 0
running = False
selected_patterns = set()  # Armazenar IDs dos padr�es selecionados
user_type = None
chat_id = None

# Defini��o dos padr�es com IDs
patterns = {
    1: {'name': '???? Samurai ????', 'pattern': ['V', 'P']},  # Padr�o 1: V seguido de P
    2: {'name': '?? Tiro Certo ??', 'pattern': ['P', 'V', 'V', 'V', 'V']},  # Padr�o 2: P seguido de quatro V
    3: {'name': '?? King ??', 'pattern': ['V', 'P', 'V']},  # Padr�o 3: V, P, V
    4: {'name': '?? Sniper Branco ??', 'pattern': ['B', 'V']}  # Padr�o 4: B seguido de V
}

def reset():
    global analise_sinal
    global entrada
    entrada = 0
    analise_sinal = False

def martingale():
    global entrada
    entrada += 1
    if entrada <= max_gale:
        bot.send_message(chat_id, text=f"?? Gale {entrada} ??")
    else:
        loss()
        reset()

def fetch_api():
    global resultado
    try:
        req = requests.get('https://blaze.com/api/roulette_games/recent')
        a = json.loads(req.content)
        jogo = [x['roll'] for x in a]
        resultado = jogo
        return jogo
    except Exception as e:
        print(f"Erro ao buscar dados da API: {e}")

def win():
    global win_count
    bot.send_message(chat_id, text="? Vit�ria!")
    win_count += 1

def loss():
    global loss_count
    bot.send_message(chat_id, text="? Derrota!")
    loss_count += 1

def correcao(results, color):
    if results[0:1] == ['P'] and color == '??':
        win()
        reset()
    elif results[0:1] == ['V'] and color == '??':
        win()
        reset()
    elif results[0:1] == ['P'] and color == '??':
        martingale()
    elif results[0:1] == ['V'] and color == '??':
        martingale()
    elif results[0:1] == ['B']:
        win()
        reset()

def enviar_sinal(cor, padrao):
    bot.send_message(chat_id, text=f'''
?? Sinal encontrado ??

?? Padr�o: {padrao}

?? Entrar no {cor}

?? Proteger no ??

?? 2 martingale: (opcional)''')

def estrategy_bot(resultado):
    global analise_sinal
    global cor_sinal
    global cores
    
    cores = []
    for x in resultado:
        if x >= 1 and x <= 7:
            color = 'V'
            cores.append(color)
        elif x >= 8 and x <= 14:
            color = 'P'
            cores.append(color)
        else:
            color = 'B'
            cores.append(color)
    print(cores)
    
    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        for num, pat in patterns.items():  # Itera sobre todos os padr�es definidos
            if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padr�o da lista de cores corresponde a um padr�o definido
                cor_sinal = '??' if pat['pattern'][0] in ['P', 'V'] else '??'  # Define a cor com base no primeiro elemento do padr�o
                enviar_sinal(cor_sinal, pat['name'])  # Envia o sinal encontrado
                analise_sinal = True
                print(f'Sinal {pat["name"]} enviado')
                break

def estrategy_adm(resultado):
    global analise_sinal
    global cor_sinal
    global cores
    
    cores = []
    for x in resultado:
        if x >= 1 and x <= 7:
            color = 'V'
            cores.append(color)
        elif x >= 8 and x <= 14:
            color = 'P'
            cores.append(color)
        else:
            color = 'B'
            cores.append(color)
    print(cores)
    
    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        for num, pat in patterns.items():  # Itera sobre todos os padr�es definidos
            if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padr�o da lista de cores corresponde a um padr�o definido
                cor_sinal = '??' if pat['pattern'][0] in ['P', 'V'] else '??'  # Define a cor com base no primeiro elemento do padr�o
                enviar_sinal(cor_sinal, pat['name'])  # Envia o sinal encontrado
                analise_sinal = True
                print(f'Sinal ADM {pat["name"]} enviado')
                break

def estrategy_custom(resultado):
    global analise_sinal
    global cor_sinal
    global cores
    
    cores = []
    for x in resultado:
        if x >= 1 and x <= 7:
            color = 'V'
            cores.append(color)
        elif x >= 8 and x <= 14:
            color = 'P'
            cores.append(color)
        else:
            color = 'B'
            cores.append(color)
    print(cores)
    
    if analise_sinal:
        correcao(cores, cor_sinal)
    else:
        for num in selected_patterns:  # Itera sobre os padr�es selecionados para o usu�rio CUSTOM
            if num in patterns:
                pat = patterns[num]
                if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padr�o da lista de cores corresponde a um padr�o selecionado
                    cor_sinal = '??' if pat['pattern'][0] in ['P', 'V'] else '??'  # Define a cor com base no primeiro elemento do padr�o
                    enviar_sinal(cor_sinal, pat['name'])  # Envia o sinal encontrado
                    analise_sinal = True
                    print(f'Sinal Custom {num} ({pat["name"]}) enviado')
                    break

def start_monitoring():
    global running
    global check_resultado  # Declare check_resultado como global
    running = True
    bot.send_message(chat_id, text="Sistema iniciado! Prepare-se para os sinais.")
    while running:
        fetch_api()
        if resultado != check_resultado:
            check_resultado = resultado.copy()  # Atualize o valor de check_resultado
            if user_type == "BOT":
                estrategy_bot(resultado)
            elif user_type == "ADM":
                estrategy_adm(resultado)
            elif user_type == "CUSTOM":
                estrategy_custom(resultado)
        time.sleep(2)  # Pequeno intervalo entre as verifica��es

def stop_monitoring():
    global running
    running = False
    bot.send_message(chat_id, text=f"?? Encerramento da Sess�o ??\n\n? Wins: {win_count}\n? Losses: {loss_count}\n\nObrigado por usar nosso servi�o! At� a pr�xima sess�o.")
    print(f"Relat�rio:\nWins: {win_count}\nLosses: {loss_count}")
    time.sleep(5)  # Aguardar 5 segundos antes de encerrar o sistema

def choose_user_type():
    global user_type
    print("\n============================")
    print("Escolha o n�mero referente ao perfil:")
    print("1: [BOT]")
    print("2: [ADM]")
    print("3: [CUSTOM]")
    print("============================")
    while True:
        try:
            choice = int(input("Digite o n�mero do perfil desejado: ").strip())
            if choice == 1:
                user_type = "BOT"
                break
            elif choice == 2:
                user_type = "ADM"
                break
            elif choice == 3:
                user_type = "CUSTOM"
                configure_custom_chat_id()
                display_patterns()
                configure_custom_patterns()
                break
            else:
                print("N�mero inv�lido. Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inv�lida. Por favor, insira um n�mero.")

def configure_custom_chat_id():
    global chat_id
    print("\n============================")
    print("Escolha o chat_id para o perfil CUSTOM:")
    print("1: Sala (ID: 98989898)")
    print("2: ADM (ID: 6045775620)")
    print("============================")
    while True:
        try:
            choice = int(input("Digite o n�mero do chat_id desejado: ").strip())
            if choice == 1:
                chat_id = 98989898
                break
            elif choice == 2:
                chat_id = 6045775620
                break
            else:
                print("N�mero inv�lido. Por favor, escolha 1 ou 2.")
        except ValueError:
            print("Entrada inv�lida. Por favor, insira um n�mero.")

def display_patterns():
    print("\n============================")
    print("Padr�es dispon�veis:")
    for num, pat in patterns.items():
        print(f"{num}: {pat['name']}")
    print("============================")

def configure_custom_patterns():
    global selected_patterns
    selected_patterns = set()
    print("\nSelecione os padr�es CUSTOM que deseja usar (separe os n�meros por v�rgula):")
    while True:
        try:
            choices = input("Digite os n�meros dos padr�es (ex.: 1,2,3): ").strip()
            selected_patterns = {int(choice) for choice in choices.split(',')}
            if selected_patterns.issubset(patterns.keys()):
                break
            else:
                print("Um ou mais n�meros n�o correspondem aos padr�es dispon�veis.")
        except ValueError:
            print("Entrada inv�lida. Por favor, insira n�meros separados por v�rgula.")

def main():
    print("Digite um comando (start, finalizar):")
    while True:
        comando = input().strip().lower()
        if comando == 'start':
            choose_user_type()
            threading.Thread(target=start_monitoring).start()
        elif comando == 'finalizar':
            stop_monitoring()
            break
        else:
            print("Comando inv�lido. Por favor, digite 'start' ou 'finalizar'.")

if __name__ == "__main__":
    main()
