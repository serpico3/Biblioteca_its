import libreria
import os
#creo le liste di dizionari libri e utenti
listaLibri = [
    {"nome": "Il Signore degli Anelli", "autore": "Tolkien", "anno": 1954, "prestato": False},
    {"nome": "Harry Potter", "autore": "Rowling", "anno": 1997, "prestato": False},
    {"nome": "le cronache di narnia", "autore": "C.S. Lewis", "anno": 1950, "prestato": False},
    {"nome": "percy jackson", "autore": "Rick Riordan", "anno": 2005, "prestato": False}
]
listaUtenti = [
    {"nome": "Giuseppe", "cognome": "Verdi", "prestiti": []},
    {"nome": "Mario", "cognome": "Rossi", "prestiti": []},
    {"nome": "Giulio", "cognome": "Bianchi", "prestiti": []},
    {"nome": "Andrea", "cognome": "Neri", "prestiti": []}
]

#ciclo principale con la funzione di break
while(True):
    try:
    
        x = int(input("1) Opzioni Libri 2) Opzioni Utente 99) Esci "))
        match x:
            case 1:
                os.system('clear')
                match int(input("1) Aggiungi Libro 2) Elimina Libro 3) Cerca Libro 4) Mostra Libri ")):
                    case 1:
                        listaLibri.append(libreria.aggiungiLibro())
                    case 2:
                        libreria.eliminaLibro(listaLibri)
                    case 3:
                        libreria.cercaLibro(listaLibri)
                    case 4:
                        libreria.stampaListe(listaLibri)
            case 2:
                os.system('clear')
                match int(input("1) Aggiungi Utente 2) Elimina Utente 3) Cerca Utente 4) Prestito Libro 5) Restituzione Libro 6) Mostra Utenti ")):
                    case 1:
                        listaUtenti.append(libreria.aggiungiUtente())
                    case 2:
                        libreria.eliminaUtente(listaUtenti)
                    case 3:
                        libreria.cercaUtente(listaUtenti)
                    case 4: 
                        libreria.prestitoLibro(listaUtenti, listaLibri)
                    case 5:
                        libreria.restituzioneLibro(listaUtenti, listaLibri)
                    case 6:
                        libreria.stampaListe(listaUtenti)
            case 99:
                break
            case _:
                print("Scelta non valida")
    except:
        print("Scelta non valida")
