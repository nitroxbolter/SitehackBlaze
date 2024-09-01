import requests
import json
import telebot
import threading
import time

# Token do bot
api = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot
chat_id = "-1002217215777"  # Substitua pelo ID correto do grupo ou chat

# Inicializa o bot
bot = telebot.TeleBot(api)

analise_sinal = False
entrada = 0
max_gale = 2  # Quantidade de gale que o bot vai mandar

resultado = []
check_resultado = []  # Inicializa check_resultado como uma lista vazia

win_count = 0
loss_count = 0
running = False

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
    req = requests.get('https://blaze.com/api/roulette_games/recent')
    a = json.loads(req.content)
    jogo = [x['roll'] for x in a]
    resultado = jogo
    return jogo

def win():
    global win_count
    bot.send_message(chat_id, text="?")
    win_count += 1

def loss():
    global loss_count
    bot.send_message(chat_id, text="?")
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

?? Padrão: {padrao}

?? Entrar no {cor}

?? Proteger no ??

?? 2 martingale: (opcional)''')

def estrategy(resultado):
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
    import requests
import json
import telebot
import threading
import time

# Token do bot
api = "7277223979:AAFL1497sJw25z6L-rXuH96wzTa6uGZPJhk"  # Substitua pelo seu token do bot
chat_id = "-1002217215777"  # Substitua pelo ID correto do grupo ou chat 6045775620 edu chat -1002217215777

# Inicializa o bot
bot = telebot.TeleBot(api)

analise_sinal = False
entrada = 0
max_gale = 2  # Quantidade de gale que o bot vai mandar

resultado = []
check_resultado = []

win_count = 0
loss_count = 0
running = False

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
    req = requests.get('https://blaze.com/api/roulette_games/recent')
    a = json.loads(req.content)
    jogo = [x['roll'] for x in a]
    resultado = jogo
    return jogo

def win():
    global win_count
    bot.send_message(chat_id, text="?")
    win_count += 1

def loss():
    global loss_count
    bot.send_message(chat_id, text="?")
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

?? Padrão: {padrao}

?? Entrar no {cor}

?? Proteger no ??

?? 2 martingale: (opcional)''')

def estrategy(resultado):
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
        if cores[0:5] == ['P', 'V', 'V', 'V', 'V']:
            cor_sinal = '??'
            padrao = '?? Tiro Certo ??'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True
            print('Sinal enviado')

        elif cores[0:4] == ['V', 'P']:
            cor_sinal = '??'
            padrao = '????Samurai2????'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True
            print('Sinal enviado')
        
        elif cores[0:3] == ['V', 'P', 'V']:
            cor_sinal = '??'
            padrao = '??King??'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True
            print('Sinal enviado')
        
        elif cores[0:2] == ['V', 'P']:
            cor_sinal = '??'
            padrao = '????Samurai????'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True
            print('Sinal enviado')

        elif cores[0:2] == ['B', 'V']:
            cor_sinal = '??'
            padrao = '??Sniper Branco??'
            enviar_sinal(cor_sinal, padrao)
            analise_sinal = True
            print('Sinal enviado')

def start_monitoring():
    global running
    running = True
    bot.send_message(chat_id, text="Sistema iniciado! Prepare-se para os sinais.")
    while running:
        fetch_api()
        if resultado != check_resultado:
            check_resultado[:] = resultado  # Atualiza a lista check_resultado
            estrategy(resultado)
        time.sleep(2)  # Pequeno intervalo entre as verificações

def stop_monitoring():
    global running
    running = False
    bot.send_message(chat_id, text=f"?? Encerramento da Sessão ??\n\n? Wins: {win_count}\n? Losses: {loss_count}\n\nObrigado por usar nosso serviço! Até a próxima sessão.")
    print(f"Relatório:\nWins: {win_count}\nLosses: {loss_count}")

def main():
    while True:
        command = input("Digite um comando (iniciar/parar): ").strip().lower()
        if command == "iniciar":
            if not running:
                monitoring_thread = threading.Thread(target=start_monitoring)
                monitoring_thread.start()
            else:
                print("O sistema já está em execução.")
        elif command == "parar":
            if running:
                stop_monitoring()
            else:
                print("O sistema já está parado.")
        else:
            print("Comando inválido. Use 'iniciar' para começar ou 'parar' para parar.")

if __name__ == "__main__":
    main()


def start_monitoring():
    global running
    global check_resultado  # Declare check_resultado como global
    running = True
    bot.send_message(chat_id, text="Sistema iniciado! Prepare-se para os sinais.")
    while running:
        fetch_api()
        if resultado != check_resultado:
            check_resultado = resultado.copy()  # Atualize o valor de check_resultado
            estrategy(resultado)
        time.sleep(2)  # Pequeno intervalo entre as verificações

def stop_monitoring():
    global running
    running = False
    bot.send_message(chat_id, text=f"?? Encerramento da Sessão ??\n\n? Wins: {win_count}\n? Losses: {loss_count}\n\nObrigado por usar nosso serviço! Até a próxima sessão.")
    print(f"Relatório:\nWins: {win_count}\nLosses: {loss_count}")

def main():
    while True:
        command = input("Digite um comando (iniciar/parar): ").strip().lower()
        if command == "iniciar":
            if not running:
                monitoring_thread = threading.Thread(target=start_monitoring)
                monitoring_thread.start()
            else:
                print("O sistema já está em execução.")
        elif command == "parar":
            if running:
                stop_monitoring()
            else:
                print("O sistema já está parado.")
        else:
            print("Comando inválido. Use 'iniciar' para começar ou 'parar' para parar.")

if __name__ == "__main__":
    main()
