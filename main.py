import libreria

#creo le liste di dizionari libri e utenti
listaLibri = []
listaUtenti = []

#ciclo principale con la funzione di break
while(True):
    try:
        x = int(input("1) Aggiungi Libri 2) Aggiungi Utenti 3) Elimina Libri 4) Elimina Utenti 5) Ricerca Libri 6) Cerca Utenti 7) Prestito Libri 8) Restituzione Libri 97) catalogo libri 98) lista utenti 99) exit "))
        match x:
            case 1:
                listaLibri.append(libreria.aggiungiLibro())
            case 2:
                listaUtenti.append(libreria.aggiungiUtente())
            case 3:
                libreria.eliminaLibro(listaLibri)
            case 4:
                libreria.eliminaUtente(listaUtenti)
            case 5:
                libreria.cercaLibro(listaLibri)
            case 6:
                libreria.cercaUtente(listaUtenti)
            case 7:
                libreria.prestitoLibro(listaUtenti, listaLibri)
            case 8:
                libreria.restituzioneLibro(listaUtenti, listaLibri)
            case 97:
                print(listaLibri)
            case 98:
                print(listaUtenti)
            case 99:
                break
            case _:
                print("Scelta non valida")
    except:
        print("Scelta non valida")
