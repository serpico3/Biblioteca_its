#lavoriamo a dizionario


def creazioneUtente():
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    #verificare che la password sia uguale
    return username, password

def eliminaUtente():
    return

def cercaUtente():
    return

def aggiungiLibro():
    nome = input("Inserisci il nome del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    anno = input("Inserisci l'anno di pubblicazione del libro: ")
    libro = {"nome": nome, "autore": autore, "anno": anno}
    return libro

def eliminaLibro():
    return

def ricercaLibro():
    return

def prestitoLibro():
    return

def restituzioneLibro():
    return

def gestioneLibri():
    return



#creazione "front-end"
listaLibri = []
listaLibri.append(aggiungiLibro())

listaUtenti = []


#listaUtenti.append(creazioneUtente())

