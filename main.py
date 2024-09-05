# -*- coding: utf-8 -*-
import requests
import json
import telebot
import threading
import time

# Token do bot
api = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot
chat_id = "6045775620"  # Substitua pelo ID correto do grupo ou chat

# Inicializa o bot
bot = telebot.TeleBot(api)

# Variáveis de controle
analise_sinal = False
entrada = 0
max_gale = 2  # Quantidade de gale que o bot vai mandar

resultado = []
check_resultado = []

win_count = 0
loss_count = 0
running = False
selected_patterns = set()  # Armazenar IDs dos padrões selecionados
user_type = None

# Definição dos padrões com IDs
patterns = {
    1: {'name': '🥷🏽 Samurai 🥷🏽', 'pattern': ['V', 'P']},  # Padrão 1: V seguido de P
    2: {'name': '🎯 Tiro Certo 🎯', 'pattern': ['P', 'V', 'V', 'V', 'V']},  # Padrão 2: P seguido de quatro V
    3: {'name': '👑 King 👑', 'pattern': ['V', 'P', 'V']},  # Padrão 3: V, P, V
    4: {'name': '🎯 Sniper Branco 🎯', 'pattern': ['B', 'V']}  # Padrão 4: B seguido de V
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
        bot.send_message(chat_id, text=f"⚠️ Gale {entrada} ⚠️")
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
    bot.send_message(chat_id, text="✅ Vitória!")
    win_count += 1

def loss():
    global loss_count
    bot.send_message(chat_id, text="❌ Derrota!")
    loss_count += 1

def correcao(results, color):
    if results[0:1] == ['P'] and color == '⚫️':
        win()
        reset()
    elif results[0:1] == ['V'] and color == '🛑':
        win()
        reset()
    elif results[0:1] == ['P'] and color == '🛑':
        martingale()
    elif results[0:1] == ['V'] and color == '⚫️':
        martingale()
    elif results[0:1] == ['B']:
        win()
        reset()

def enviar_sinal(cor, padrao):
    bot.send_message(chat_id, text=f'''
🚨 Sinal encontrado 🚨

⏯️ Padrão: {padrao}

💶 Entrar no {cor}

🦾 Proteger no ⚪️

🐓 2 martingale: (opcional)''')

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
        for num, pat in patterns.items():  # Itera sobre todos os padrões definidos
            if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padrão da lista de cores corresponde a um padrão definido
                cor_sinal = '🛑' if pat['pattern'][0] in ['P', 'V'] else '⚫️'  # Define a cor com base no primeiro elemento do padrão
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
        for num, pat in patterns.items():  # Itera sobre todos os padrões definidos
            if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padrão da lista de cores corresponde a um padrão definido
                cor_sinal = '🛑' if pat['pattern'][0] in ['P', 'V'] else '⚫️'  # Define a cor com base no primeiro elemento do padrão
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
        for num in selected_patterns:  # Itera sobre os padrões selecionados para o usuário CUSTOM
            if num in patterns:
                pat = patterns[num]
                if cores[:len(pat['pattern'])] == pat['pattern']:  # Verifica se o padrão da lista de cores corresponde a um padrão selecionado
                    cor_sinal = '🛑' if pat['pattern'][0] in ['P', 'V'] else '⚫️'  # Define a cor com base no primeiro elemento do padrão
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
        time.sleep(2)  # Pequeno intervalo entre as verificações

def stop_monitoring():
    global running
    running = False
    bot.send_message(chat_id, text=f"🏁 Encerramento da Sessão 🏁\n\n✅ Wins: {win_count}\n❌ Losses: {loss_count}\n\nObrigado por usar nosso serviço! Até a próxima sessão.")
    print(f"Relatório:\nWins: {win_count}\nLosses: {loss_count}")
    time.sleep(5)  # Aguardar 5 segundos antes de encerrar o sistema

def choose_user_type():
    global user_type
    while True:
        user = input("Qual usuário será usado? (BOT/ADM/CUSTOM): ").strip().upper()
        if user in ["BOT", "ADM", "CUSTOM"]:
            user_type = user
            if user == "CUSTOM":
                display_patterns()
                configure_custom_patterns()
            break
        else:
            print("Usuário inválido. Por favor, escolha 'BOT', 'ADM' ou 'CUSTOM'.")

def display_patterns():
    print("\nPadrões disponíveis:")
    for num, pat in patterns.items():
        print(f"ID {num}: {pat['name']}")

def configure_custom_patterns():
    global selected_patterns
    print("Configure os padrões personalizados para o usuário CUSTOM.")
    while True:
        try:
            ids = input("Digite os IDs dos padrões separados por vírgula (ex: 1,2,4): ").strip()
            selected_patterns = {int(id.strip()) for id in ids.split(',')}
            if all(id in patterns for id in selected_patterns):
                print(f"Padrões selecionados: {', '.join(map(str, selected_patterns))}")
                break
            else:
                print("IDs inválidos. Verifique e tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente com IDs numéricos.")

if __name__ == '__main__':
    choose_user_type()
    start_monitoring()
