
#funzione per la creazione dell'utente, chiede nome e cognome mentre invece crea in automatico una lista di libri in prestito inizialmemte vuota
def aggiungiUtente():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    utente = {"nome": nome, "cognome": cognome, "prestiti": []}
    return utente
#funzione per la creazione del libro, chiede nome, autore e anno e crea in automatico il booleano prestato come False (di base il libro è disponibile)
def aggiungiLibro():
    nome = input("Inserisci il nome del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    anno = input("Inserisci l'anno di pubblicazione del libro: ")
    libro = {"nome": nome, "autore": autore, "anno": anno, "prestato": False}
    return libro

def eliminaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome dell'utente da eliminare: ")
    cognome_Utente = input("Inserisci il cognome dell'utente da eliminare: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(listaUtenti) - 1, -1, -1):
        #controlla che l'utente da eliminare esista e se esiste lo elimina
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            del listaUtenti[x]
    return 0

def eliminaLibro(listaLibri):
    
    nome_libro = input("Inserisci il nome del libro da eliminare: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(listaLibri) - 1, -1, -1):
        #controlla che il libro da eliminare esista e se esiste lo elimina
        if listaLibri[x]['nome'] == nome_libro:
            del listaLibri[x]
    return 0

#un utente è caratterizzato da nome e cognome, non abbiamo implementato sistemi per eliminare il problema dell'omonimia
def cercaUtente(listaUtenti):
    nome_Utente = input("Inserisci il nome della persona da cercare: ")
    cognome_Utente = input("Inserisci il cognome della persona da cercare: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(listaUtenti) - 1, -1, -1):
        #controlla che l'utente da cercare esiste e se esiste lo mostra
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            print(listaUtenti[x])
    return

#identifichiamo i libri unicamente dal nome, non abbiamo implementato un sistema che permetta di avere più libri uguali
def cercaLibro(listaLibri):
    nome_libro = input("Inserisci il nome del libro da cercare: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(listaLibri) - 1, -1, -1):
        #controlla se il libro richiesto esiste e se esiste lo mostra
        if listaLibri[x]['nome'] == nome_libro:
            print(listaLibri[x])
    return

def prestitoLibro(listaUtenti, listaLibri):
    nome_Utente = input("Inserisci il nome dell'utente: ")
    cognome_Utente = input("Inserisci il cognome dell'utente: ")
    libro = input("Inserisci il nome del libro: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(listaUtenti) - 1, -1, -1):
        #controllo che l'utente esista
        if listaUtenti[x]['nome'] == nome_Utente and listaUtenti[x]['cognome'] == cognome_Utente:
            # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
            for y in range(len(listaLibri) - 1, -1, -1):
                #controllo che il libro esista
                if listaLibri[y]['nome'] == libro:
                    #controllo che il libro non sia prestato
                    if listaLibri[y]['prestato'] == True:
                        print("Libro non disponibile")
                    #se il libro esiste, l'utente esiste ed è disponibile allora lo rendo "non disponibile" e lo assegno all'utente
                    else:
                        listaLibri[y]['prestato'] = True
                        listaUtenti[x]['prestiti'].append(libro)
    return

def restituzioneLibro(ListaUtenti, ListaLibri):
    nome_Utente = input("Inserisci il nome dell'utente: ")
    cognome_Utente = input("Inserisci il cognome dell'utente: ")
    libro = input("Inserisci il nome del libro: ")
    # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
    for x in range(len(ListaUtenti) - 1, -1, -1):
        #controllo che l'utente esista
        if ListaUtenti[x]['nome'] == nome_Utente and ListaUtenti[x]['cognome'] == cognome_Utente:
            # Itera dalla fine all'inizio della lista per evitare problemi durante l'eliminazione degli elementi
            for y in range(len(ListaLibri) - 1, -1, -1):
                #controllo che il libro esista
                if ListaLibri[y]['nome'] == libro:
                    #controllo che il libro sia prestato
                    if ListaLibri[y]['prestato'] == False:
                        print("Libro non prestato")
                    #se il libro esiste, l'utente esiste ed è prestato allora lo rendo "disponibile" e lo rimuovo dall'utente
                    else:
                        ListaLibri[y]['prestato'] = False
                        ListaUtenti[x]['prestiti'].remove(libro)
    return

def stampaListe(lista):
    for dizionario in lista:
        for chiave, valore in dizionario.items():
            print(f"{chiave}: {valore}")
        print()
