def creazioneUtente():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    utente = {"nome": nome, "cognome": cognome}
    return utente

def eliminaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome dell'utente da eliminare: ")
    cognome_Utente = input("Inserisci il cognome dell'utente da eliminare: ")
    for x in range(len(listaUtenti) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_Utente and listaLibri[x]['cognome'] == cognome_Utente:
            del listaLibri[x]
    return 0

def cercaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome della persona da cercare: ")
    cognome_Utente = input("Inserisci il cognome della persona da cercare: ")
    for x in range(len(listaUtenti) - 1, -1, -1):
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            print(listaUtenti[x])
    return

def aggiungiLibro():
    nome = input("Inserisci il nome del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    anno = input("Inserisci l'anno di pubblicazione del libro: ")
    libro = {"nome": nome, "autore": autore, "anno": anno}
    return libro

def eliminaLibro(listaLibri):
    nome_libro = input("Inserisci il nome del libro da eliminare: ")
    for x in range(len(listaLibri) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_libro:
            del listaLibri[x]
    return 0

def ricercaLibro(listaLibri):
    nome_libro = input("Inserisci il nome del libro da cercare: ")
    for x in range(len(listaLibri) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_libro:
            print(listaLibri[x])
    return

def prestitoLibro():
    return

def restituzioneLibro():
    return





#creazione "front-end"
listaLibri = []
listaUtenti = []
while(True):
    x = int(input("1) Aggiungi Libri 2) Aggiungi Utenti 3) Elimina Libri 4) Elimina Utenti 5) Ricerca Libri 6) Cerca Utenti  97) catalogo libri 98) lista utenti 99) exit "))
    match x:
        case 1:
            listaLibri.append(aggiungiLibro())
        case 2:
            listaUtenti.append(creazioneUtente())
        case 3:
            eliminaLibro(listaLibri)
        case 4:
            eliminaUtente(listaUtenti)
        case 5:
            ricercaLibro(listaLibri)
        case 6:
            cercaUtente(listaUtenti)
        case 97:
            print(listaLibri)
        case 98:
            print(listaUtenti)
        case 99:
            break
