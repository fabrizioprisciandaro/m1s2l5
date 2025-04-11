print("Benvenuto su Assistente Virtuale creato da Fabrizio.\n")

import datetime

def assistente_virtuale(opzione):
    if opzione == "1":
        oggi = datetime.date.today()
        risposta = "\nLa data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif opzione == "2":
        ora_attuale = datetime.datetime.now().strftime("%H:%M")
        risposta = "\nL'ora attuale è " + ora_attuale
    elif opzione == "3":
        risposta = "\nMi chiamo Assistente Virtuale"
    else:
        risposta = "\nInserisci una delle opzioni disponibili. Riprova."
    return risposta

def mostra_menu():
    print("\nCosa vuoi sapere?\n")
    print("1. Qual è la data di oggi?")
    print("2. Che ore sono?")
    print("3. Come mi chiamo?")
    print("4. Esci")

while True:
    mostra_menu()
    scelta = input("\nSeleziona un'opzione (1-4): ").strip()
    if scelta == "4":
        print("\nArrivederci!")
        break
    else:
        print(assistente_virtuale(scelta))