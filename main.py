#lavoriamo a dizionario


def creazioneUtente():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    utente = {"nome": nome, "cognome": cognome}
    return utente

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

def eliminaLibro(listaLibri):
    del listaLibri['nome' == input("Inserisci il nome del libro da eliminare: ")]
    return 0

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
listaUtenti = []
while(True):
    x = int(input("1) Aggiungi Libri 2) Aggiungi Utenti 3) Elimina Libri 4) Elimina Utenti 97) catalogo libri 98) lista utenti 99) exit "))
    match x:
        case 1:
            listaLibri.append(aggiungiLibro())
        case 2:
            listaUtenti.append(creazioneUtente())
        case 3:
            eliminaLibro(listaLibri)
        case 4:
            eliminaUtente()
        case 97:
            print(listaLibri)
        case 98:
            print(listaUtenti)
        case 99:
            break
