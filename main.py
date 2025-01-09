def aggiungiUtente():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    utente = {"nome": nome, "cognome": cognome, "prestiti": []}
    return utente
def aggiungiLibro():
    nome = input("Inserisci il nome del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    anno = input("Inserisci l'anno di pubblicazione del libro: ")
    libro = {"nome": nome, "autore": autore, "anno": anno, "prestato": False}
    return libro

def eliminaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome dell'utente da eliminare: ")
    cognome_Utente = input("Inserisci il cognome dell'utente da eliminare: ")
    for x in range(len(listaUtenti) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_Utente and listaLibri[x]['cognome'] == cognome_Utente:
            del listaLibri[x]
    return 0
def eliminaLibro(listaLibri):
    nome_libro = input("Inserisci il nome del libro da eliminare: ")
    for x in range(len(listaLibri) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_libro:
            del listaLibri[x]
    return 0

def cercaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome della persona da cercare: ")
    cognome_Utente = input("Inserisci il cognome della persona da cercare: ")
    for x in range(len(listaUtenti) - 1, -1, -1):
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            print(listaUtenti[x])
    return
def cercaLibro(listaLibri):
    nome_libro = input("Inserisci il nome del libro da cercare: ")
    for x in range(len(listaLibri) - 1, -1, -1):
        if listaLibri[x]['nome'] == nome_libro:
            print(listaLibri[x])
    return

def prestitoLibro(listaUtenti, listaLibri):
    nome_Utente = input("Inserisci il nome dell'utente: ")
    cognome_Utente = input("Inserisci il cognome dell'utente: ")
    libro = input("Inserisci il nome del libro: ")
    for x in range(len(listaUtenti) - 1, -1, -1):
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            for y in range(len(listaLibri) - 1, -1, -1):
                if listaLibri[y]['nome'] == libro:
                    if listaLibri[y]['prestato'] == True:
                        print("Libro non disponibile")
                    else:
                        listaLibri[y]['prestato'] = True
                        listaUtenti[x]['prestiti'].append(libro)
                else:
                    print("Libro non trovato")
        else:
            print("Utente non trovato")
    return
def restituzioneLibro(ListaUtenti, ListaLibri):
    nome_Utente = input("Inserisci il nome dell'utente: ")
    cognome_Utente = input("Inserisci il cognome dell'utente: ")
    libro = input("Inserisci il nome del libro: ")
    for x in range(len(ListaUtenti) - 1, -1, -1):
        if ListaUtenti[x]['nome'] == nome_Utente and ListaUtenti[x]['cognome'] == cognome_Utente:
            for y in range(len(ListaLibri) - 1, -1, -1):
                if ListaLibri[y]['nome'] == libro:
                    if ListaLibri[y]['prestato'] == False:
                        print("Libro non prestato")
                    else:
                        ListaLibri[y]['prestito'] = False
                        ListaUtenti[x]['prestiti'].remove(libro)
                else:
                    print("Libro non trovato")
        else:
            print("Utente non trovato")
    return

#creazione "front-end"
listaLibri = []
listaUtenti = []
while(True):
    x = int(input("1) Aggiungi Libri 2) Aggiungi Utenti 3) Elimina Libri 4) Elimina Utenti 5) Ricerca Libri 6) Cerca Utenti 7) Prestito Libri 8) Restituzione Libri 97) catalogo libri 98) lista utenti 99) exit "))
    match x:
        case 1:
            listaLibri.append(aggiungiLibro())
        case 2:
            listaUtenti.append(aggiungiUtente())
        case 3:
            eliminaLibro(listaLibri)
        case 4:
            eliminaUtente(listaUtenti)
        case 5:
            cercaLibro(listaLibri)
        case 6:
            cercaUtente(listaUtenti)
        case 7:
            prestitoLibro(listaUtenti, listaLibri)
        case 8:
            restituzioneLibro(listaUtenti, listaLibri)
        case 97:
            print(listaLibri)
        case 98:
            print(listaUtenti)
        case 99:
            break
